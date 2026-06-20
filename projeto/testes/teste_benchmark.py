import sys
import os

# Pega o caminho absoluto do diretório onde este script está localizado
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
# Pega o caminho da raiz do projeto (um nível acima)
raiz_projeto = os.path.abspath(os.path.join(diretorio_atual, '..'))

# Adiciona os caminhos necessários ao sys.path para que o Python encontre os módulos
sys.path.append(raiz_projeto)
sys.path.append(os.path.join(raiz_projeto, 'algoritimos', 'ordenacao'))
sys.path.append(os.path.join(raiz_projeto, 'algoritimos', 'busca'))
sys.path.append(os.path.join(raiz_projeto, 'utils'))

from algoritimos.ordenacao.insertion_sort import insertion_sort
from algoritimos.ordenacao.selection_sort  import selection_sort 
from algoritimos.ordenacao.merge_sort  import merge_sort
from algoritimos.ordenacao.bubble_sort  import bubble_sort
from algoritimos.ordenacao.heap_sort  import heap_sort
from algoritimos.ordenacao.quick_sort  import quick_sort

from algoritimos.busca.busca_sequencial import busca_sequencial
from algoritimos.busca.busca_binaria import busca_binaria

from utils.benchmark import AvaliadorDesempenho
from utils.gerador import gerar_array_aleatorio, gerar_array_quase_ordenado, gerar_array_invertido, gerar_array_com_duplicatas

def main():
    algoritmos_ordenacao = {
        "Ordenação por Inserção": insertion_sort,
        "Ordenação por Seleção": selection_sort,
        "Ordenação por Bolha": bubble_sort,
        "Ordenação por Mesclagem": merge_sort,
        "Ordenação Rápida": quick_sort,
        "Ordenação por Heap": heap_sort,
    }

    algoritmos_busca = {
        "Busca Sequencial": busca_sequencial,
        "Busca Binária": busca_binaria,
    }

    tamanhos_array = [3,4,7]
    num_execucoes = 5

    print("Iniciando o benchmarking dos algoritmos de ordenação...")

    for tamanho in tamanhos_array:
        print(f"\n--- Tamanho do Array: {tamanho} ---")

        # Cenário: Array Aleatório
        array_aleatorio = gerar_array_aleatorio(tamanho)
        print("\nCenário: Array Aleatório (Ordenação)")
        for nome, func in algoritmos_ordenacao.items():
            print(array_aleatorio)
            avaliador = AvaliadorDesempenho(func, num_execucoes=num_execucoes)
            resultados = avaliador.executar(array_aleatorio)
            print(f"  {nome}:")
            print(f"    Tempo Médio: {resultados['tempo_medio']:.6f} segundos")
            print(f"    Comparações Médias: {resultados['comparacoes_medias']:.2f}")
            print(f"    Trocas Médias: {resultados['trocas_medias']:.2f}")

        # Cenário: Array Quase Ordenado
        array_quase_ordenado = gerar_array_quase_ordenado(tamanho)
        print("\nCenário: Array Quase Ordenado (Ordenação)")
        for nome, func in algoritmos_ordenacao.items():
            avaliador = AvaliadorDesempenho(func, num_execucoes=num_execucoes)
            resultados = avaliador.executar(array_quase_ordenado)
            print(f"  {nome}:")
            print(f"    Tempo Médio: {resultados['tempo_medio']:.6f} segundos")
            print(f"    Comparações Médias: {resultados['comparacoes_medias']:.2f}")
            print(f"    Trocas Médias: {resultados['trocas_medias']:.2f}")

        # Cenário: Array Invertido
        array_invertido = gerar_array_invertido(tamanho)
        print("\nCenário: Array Invertido (Ordenação)")
        for nome, func in algoritmos_ordenacao.items():
            avaliador = AvaliadorDesempenho(func, num_execucoes=num_execucoes)
            resultados = avaliador.executar(array_invertido)
            print(f"  {nome}:")
            print(f"    Tempo Médio: {resultados['tempo_medio']:.6f} segundos")
            print(f"    Comparações Médias: {resultados['comparacoes_medias']:.2f}")
            print(f"    Trocas Médias: {resultados['trocas_medias']:.2f}")

        # Cenário: Array com Duplicatas
        array_com_duplicatas = gerar_array_com_duplicatas(tamanho)
        print("\nCenário: Array com Duplicatas (Ordenação)")
        for nome, func in algoritmos_ordenacao.items():
            avaliador = AvaliadorDesempenho(func, num_execucoes=num_execucoes)
            resultados = avaliador.executar(array_com_duplicatas)
            print(f"  {nome}:")
            print(f"    Tempo Médio: {resultados['tempo_medio']:.6f} segundos")
            print(f"    Comparações Médias: {resultados['comparacoes_medias']:.2f}")
            print(f"    Trocas Médias: {resultados['trocas_medias']:.2f}")

    print("\nBenchmarking dos algoritmos de ordenação concluído.\n")

    print("Iniciando o benchmarking dos algoritmos de busca...")

    for tamanho in tamanhos_array:
        print(f"\n--- Tamanho do Array: {tamanho} ---")

        # Para busca, precisamos de um array ordenado para Busca Binária e um elemento para buscar
        array_para_busca = sorted(gerar_array_aleatorio(tamanho)) # Garante que o array esteja ordenado
        elemento_existente = array_para_busca[tamanho // 2] # Elemento que existe
        elemento_nao_existente = tamanho * 100 + 1 # Elemento que provavelmente não existe

        print("\nCenário: Busca por Elemento Existente")
        for nome, func in algoritmos_busca.items():
            avaliador = AvaliadorDesempenho(func, num_execucoes=num_execucoes)
            resultados = avaliador.executar(array_para_busca, elemento_existente)
            print(f"  {nome}:")
            print(f"    Tempo Médio: {resultados['tempo_medio']:.6f} segundos")
            print(f"    Comparações Médias: {resultados['comparacoes_medias']:.2f}")
            print(f"    Trocas Médias: {resultados['trocas_medias']:.2f}") # Trocas serão 0 para busca

        print("\nCenário: Busca por Elemento Não Existente")
        for nome, func in algoritmos_busca.items():
            avaliador = AvaliadorDesempenho(func, num_execucoes=num_execucoes)
            resultados = avaliador.executar(array_para_busca, elemento_nao_existente)
            print(f"  {nome}:")
            print(f"    Tempo Médio: {resultados['tempo_medio']:.6f} segundos")
            print(f"    Comparações Médias: {resultados['comparacoes_medias']:.2f}")
            print(f"    Trocas Médias: {resultados['trocas_medias']:.2f}") # Trocas serão 0 para busca

    print("\nBenchmarking concluído.")

if __name__ == "__main__":
    main()
