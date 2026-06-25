import sys
import os
import time
import statistics

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
raiz_projeto = os.path.abspath(os.path.join(diretorio_atual, ".."))
sys.path.insert(0, raiz_projeto)

from utils.benchmark import AvaliadorDesempenho
from utils.gerador import (
    gerar_array_aleatorio,
    gerar_array_quase_ordenado,
    gerar_array_invertido,
    gerar_array_com_duplicatas
)

from analisador.caracteristicas import Caracteristicas
from analisador.motor_decisao import calcular_pontuacoes
from main import  adaptar_caracteristicas
from validacao.gerar_graficos import gerar_todos_os_graficos

from algoritimos.ordenacao.quick_sort import quick_sort
from algoritimos.ordenacao.merge_sort import merge_sort
from algoritimos.ordenacao.heap_sort import heap_sort
from algoritimos.ordenacao.insertion_sort import insertion_sort
from algoritimos.ordenacao.selection_sort import selection_sort
from algoritimos.ordenacao.bubble_sort import bubble_sort


ALGORITMOS = {
    "Quick Sort": quick_sort,
    "Merge Sort": merge_sort,
    "Heap Sort": heap_sort,
    "Insertion Sort": insertion_sort,
    "Selection Sort": selection_sort,
    "Bubble Sort": bubble_sort
}

CENARIOS = [
    ("Aleatório", gerar_array_aleatorio),
    ("Quase Ordenado", gerar_array_quase_ordenado),
    ("Invertido", gerar_array_invertido),
    ("Duplicatas", gerar_array_com_duplicatas)
]

TAMANHOS = [1000, 5000, 10000]



def benchmark_completo(vetor):

    """Roda todos os algoritmos de ordenacao no mesmo array
    resultado={nome_algoritmo: {tempo_medio, comparacoes_medias, trocas_medias}}."""

    resultados = {}
    for nome, funcao in ALGORITMOS.items():
        avaliador = AvaliadorDesempenho(funcao, num_execucoes=3)
        metricas = avaliador.executar(vetor)
        resultados[nome] = metricas
    return resultados


def obter_top2(resultados):

    """seleciona os dois algoritmos com menor tempo medio real """

    ranking = sorted(resultados.items(), key=lambda item: item[1]["tempo_medio"])
    return [ranking[0][0], ranking[1][0]]



def executar_seletor(vetor):
    """Cronometra so a decisao do seletor (analise + pontuacao, sem
    incluir a ordenacao [ Tdecisao = Tanalise + Tpontuacao])."""

    inicio = time.perf_counter()

    caracteristicas = Caracteristicas().analisa(vetor)
    caracteristicas_adaptadas = adaptar_caracteristicas(caracteristicas)
    pontuacoes = calcular_pontuacoes(caracteristicas_adaptadas)
    recomendado = max(pontuacoes, key=pontuacoes.get)

    tempo_decisao = time.perf_counter() - inicio

    return {
        "recomendado": recomendado,
        "tempo_decisao": tempo_decisao,
        "caracteristicas": caracteristicas,
        "caracteristicas_adaptadas": caracteristicas_adaptadas,
        "pontuacoes": pontuacoes
    }


def validar_cenario(vetor):
    """Junta o benchmark de todos os algoritmos com a decisao do seletor
    num unico resultado: recomendacao, acerto Top-2 e overhead."""
    resultados = benchmark_completo(vetor)
    top2 = obter_top2(resultados)
    decisao = executar_seletor(vetor)

    tempo_algoritmo = resultados[decisao["recomendado"]]["tempo_medio"]

    # Overhead = (Tseletor - Talgoritmo) / Talgoritmo x 100%
    # Tseletor = tempo_decisao + tempo_algoritmo
    overhead = (decisao["tempo_decisao"] / tempo_algoritmo) * 100

    return {
        **decisao,
        "resultados": resultados,
        "top2": top2,
        "acertou": decisao["recomendado"] in top2,
        "overhead": overhead
    }




def inicializar_contador_cenario(acertos_por_tipo, nome_cenario):
    """Cria o contador de acertos/total para um tipo de cenario novo."""

    acertos_por_tipo[nome_cenario] = {"acertos": 0, "total": 0}


def atualizar_contadores(resultado, nome_cenario, acertos_por_tipo):
    """Soma 1 ao total do tipo, e mais 1 aos acertos se o seletor acertou"""

    acertos_por_tipo[nome_cenario]["total"] += 1
    if resultado["acertou"]:
        acertos_por_tipo[nome_cenario]["acertos"] += 1


def registrar_metricas(resultado, overheads, tempos_decisao):
    """Guarda overhead e tempo de decisao deste cenario pras medias finais"""

    overheads.append(resultado["overhead"])
    tempos_decisao.append(resultado["tempo_decisao"])


def registrar_dados_graficos(linhas_algoritmos, linhas_cenarios, resultado, nome_cenario, tamanho):
    """Monta as duas listas em memoria para alimentar gerar_todos_os_graficos"""

    linhas_cenarios.append({
        "tipo_cenario": nome_cenario,
        "tamanho": tamanho,
        "recomendado": resultado["recomendado"],
        "acertou": resultado["acertou"],
        "overhead": resultado["overhead"],
        "tempo_decisao": resultado["tempo_decisao"]
    })

    for nome_alg, dados in resultado["resultados"].items():
        linhas_algoritmos.append({
            "tipo_cenario": nome_cenario,
            "tamanho": tamanho,
            "algoritmo": nome_alg,
            "tempo_medio": dados["tempo_medio"],
            "comparacoes_medias": dados["comparacoes_medias"],
            "trocas_medias": dados["trocas_medias"]
        })

# 4 metricas

def calcular_metricas(acertos_por_tipo, overheads, tempos_decisao):

    """Taxa de acerto geral/por tipo, overhead medio, tempo medio de
    decisao e impacto do tipo de dataset."""

    total_acertos = sum(dados["acertos"] for dados in acertos_por_tipo.values())
    total_cenarios = sum(dados["total"] for dados in acertos_por_tipo.values())

    taxas_por_tipo = {
        nome: (dados["acertos"] / dados["total"]) * 100
        for nome, dados in acertos_por_tipo.items()
    }

    return {
        "taxa_acerto_geral": (total_acertos / total_cenarios) * 100,
        "taxa_acerto_por_tipo": taxas_por_tipo,
        "impacto_tipo_dataset": max(taxas_por_tipo.values()) - min(taxas_por_tipo.values()),
        "overhead_medio": statistics.mean(overheads),
        "tempo_decisao_medio": statistics.mean(tempos_decisao)
    }


def exibir_metricas(metricas):
    print("\n" + "=" * 50)
    print("METRICAS  ")
    print("=" * 50)
    print(f"1. Taxa de acerto Top-2:        {metricas['taxa_acerto_geral']:.1f}%   (meta >= 80%)")
    print(f"2. Overhead medio:               {metricas['overhead_medio']:.2f}%   (meta < 10%)")
    print(f"3. Tempo medio de decisao:        {metricas['tempo_decisao_medio'] * 1000:.3f} ms  (meta < 100 ms)")
    print(f"4. Impacto do tipo de dataset:     {metricas['impacto_tipo_dataset']:.1f} pontos percentuais   (meta < 30%)")

    print("\nTaxa de acerto por tipo de cenario:")
    for nome, taxa in metricas["taxa_acerto_por_tipo"].items():
        print(f"   {nome}: {taxa:.1f}%")


def executar_validacao():
    acertos_por_tipo = {}
    overheads = []
    tempos_decisao = []
    linhas_algoritmos = []
    linhas_cenarios = []
    

    for nome_cenario, gerador in CENARIOS:

        inicializar_contador_cenario(acertos_por_tipo, nome_cenario)
        print(f"\n{nome_cenario}")

        for tamanho in TAMANHOS:

            vetor = gerador(tamanho)
            resultado = validar_cenario(vetor)

            print(tamanho, resultado["recomendado"], resultado["acertou"])
            atualizar_contadores(resultado, nome_cenario, acertos_por_tipo)
            registrar_metricas(resultado, overheads, tempos_decisao)
            registrar_dados_graficos(linhas_algoritmos, linhas_cenarios, resultado, nome_cenario, tamanho)

    metricas = calcular_metricas(acertos_por_tipo, overheads, tempos_decisao)
    exibir_metricas(metricas)
    gerar_todos_os_graficos(linhas_algoritmos, linhas_cenarios)

    return metricas


if __name__ == "__main__":
    executar_validacao()