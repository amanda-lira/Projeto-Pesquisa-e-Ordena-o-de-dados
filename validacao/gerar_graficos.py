import os
import statistics
from collections import defaultdict

import matplotlib
matplotlib.use("Agg") 
import matplotlib.pyplot as plt

DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
PASTA_GRAFICOS = os.path.join(DIRETORIO_ATUAL, "graficos")
os.makedirs(PASTA_GRAFICOS, exist_ok=True)

ORDEM_ALGORITMOS = ["Insertion Sort", "Selection Sort", "Bubble Sort",
                    "Merge Sort", "Quick Sort", "Heap Sort"]
CORES = plt.get_cmap("tab10").colors


def _salvar(fig, nome_arquivo):
    caminho_png = os.path.join(PASTA_GRAFICOS, nome_arquivo + ".png")
    caminho_pdf = os.path.join(PASTA_GRAFICOS, nome_arquivo + ".pdf")
    fig.savefig(caminho_png, dpi=150, bbox_inches="tight")
    fig.savefig(caminho_pdf, bbox_inches="tight")
    plt.close(fig)
    print(f"  salvo: {os.path.relpath(caminho_png, DIRETORIO_ATUAL)}")
    print(f"  salvo: {os.path.relpath(caminho_pdf, DIRETORIO_ATUAL)}")



def grafico_tempo_por_algoritmo(linhas_algoritmos):

    """
    Média de tempo de todos os tamanhos de array em cada tipo de dataset
    """
    MARCADORES = ["o", "s", "^", "D", "v", "P"]
    ORDEM_CENARIOS = ["Aleatório", "Quase Ordenado", "Invertido", "Duplicatas"]
    dados = defaultdict(lambda: defaultdict(list))

    for row in linhas_algoritmos:
        dados[row["algoritmo"]][row["tipo_cenario"]].append(row["tempo_medio"])

    algoritmos = [a for a in ORDEM_ALGORITMOS if a in dados]
    cenarios = [c for c in ORDEM_CENARIOS if any(c in dados[a] for a in algoritmos)]
    x = list(range(len(cenarios)))

    fig, ax = plt.subplots(figsize=(9, 5))

    for i, alg in enumerate(algoritmos):
        medias = [ statistics.mean(dados[alg][c]) if dados[alg].get(c) else float("nan")
                   for c in cenarios ]
        cor = CORES[i % len(CORES)]
        ax.plot(x, medias,
                color=cor, marker=MARCADORES[i % len(MARCADORES)],
                linewidth=2, markersize=7,label=alg,)
        ultimo = medias[-1]
        if ultimo == ultimo:  
            ax.annotate( f"{ultimo:.4f}s", xy=(x[-1], ultimo),
                         xytext=(6, 0), textcoords="offset points",
                         va="center", fontsize=8, color=cor, )
    ax.set_yscale("log")
    ax.set_xticks(x)
    ax.set_xticklabels(cenarios, fontsize=10)
    ax.set_xlabel("Tipo de dataset", fontsize=11)
    ax.set_ylabel("Tempo medio de execucao (s) - escala log", fontsize=10)
    ax.set_title("Tempo medio de execucao por algoritmo\n(media de todos os tamanhos)",fontsize=12, fontweight="bold")
    ax.grid(axis="y", linestyle="--", alpha=0.4)
    ax.grid(axis="x", linestyle=":", alpha=0.3)
    ax.legend(fontsize=9, loc="upper left", framealpha=0.9)

    fig.tight_layout()
    _salvar(fig, "01_tempo_por_algoritmo")


def grafico_comparacoes_por_algoritmo(linhas_algoritmos):
    """
    Média de comparaçõesfeitas por cada algoritmo 
    de todos os tamanhos de array em cada tipo de dataset
    """
    MARCADORES = ["o", "s", "^", "D", "v", "P"]
    ORDEM_CENARIOS = ["Aleatório", "Quase Ordenado", "Invertido", "Duplicatas"]

    dados = defaultdict(lambda: defaultdict(list))
    for row in linhas_algoritmos:
        dados[row["algoritmo"]][row["tipo_cenario"]].append(row["comparacoes_medias"])

    algoritmos = [a for a in ORDEM_ALGORITMOS if a in dados]
    cenarios = [c for c in ORDEM_CENARIOS if any(c in dados[a] for a in algoritmos)]
    x = list(range(len(cenarios)))

    fig, ax = plt.subplots(figsize=(9, 5))

    for i, alg in enumerate(algoritmos):
        medias = [statistics.mean(dados[alg][c]) if dados[alg].get(c) else float("nan")
                  for c in cenarios]
        cor = CORES[i % len(CORES)]
        ax.plot(
            x, medias, color=cor,
            marker=MARCADORES[i % len(MARCADORES)],
            linewidth=2, markersize=7, label=alg,
             )
        ultimo = medias[-1]
        if ultimo == ultimo: 
            ax.annotate(
                f"{ultimo:,.0f}".replace(",", "."),
                xy=(x[-1], ultimo), xytext=(6, 0),
                textcoords="offset points",
                va="center",fontsize=8, color=cor,
            )

    ax.set_yscale("log")
    ax.set_xticks(x)
    ax.set_xticklabels(cenarios, fontsize=10)
    ax.set_xlabel("Tipo de dataset", fontsize=11)
    ax.set_ylabel("Numero medio de comparacoes - escala log", fontsize=10)
    ax.set_title( "Comparacoes medias por algoritmo\n(media de todos os tamanhos)",
                   fontsize=12, fontweight="bold" )
    ax.grid(axis="y", linestyle="--", alpha=0.4)
    ax.grid(axis="x", linestyle=":", alpha=0.3)
    ax.legend(fontsize=9, loc="upper left", framealpha=0.9)
    fig.tight_layout()
    _salvar(fig, "02_comparacoes_por_algoritmo")

def grafico_acuracia_por_tipo(linhas_cenarios):
    """
    % de acertos do seletor por tipo de dataset
    """
    acertos_por_tipo = defaultdict(list)
    for l in linhas_cenarios:
        acertos_por_tipo[l["tipo_cenario"]].append(bool(l["acertou"]))

    tipos = list(acertos_por_tipo.keys())
    taxas = [sum(acertos_por_tipo[t]) / len(acertos_por_tipo[t]) * 100 for t in tipos]
    taxa_geral = sum(l["acertou"] for l in linhas_cenarios) / len(linhas_cenarios) * 100

    fig, ax = plt.subplots(figsize=(8, 5))
    barras = ax.bar(tipos, taxas, color=CORES[:len(tipos)])
    ax.axhline(80, color="red", linestyle="--", linewidth=1, label="Meta do projeto (80%)")
    ax.axhline(taxa_geral, color="black", linestyle=":", linewidth=1,
               label=f"Media geral ({taxa_geral:.1f}%)")
    ax.set_ylabel("Taxa de acerto [Top-2] (%)")
    ax.set_ylim(0, 110)
    ax.set_title("Acuracia do seletor por tipo de dataset")
    ax.legend(loc="lower right", fontsize=8)
    plt.setp(ax.get_xticklabels(), rotation=20, ha="right")
    for barra, valor in zip(barras, taxas):
        ax.annotate(f"{valor:.0f}%", (barra.get_x() + barra.get_width() / 2, barra.get_height()),
                    textcoords="offset points", xytext=(0, 4), ha="center", fontsize=8)
    fig.tight_layout()
    _salvar(fig, "03_acuracia_por_tipo")


def grafico_overhead_medio(linhas_cenarios):
    
    overhead_por_tamanho = defaultdict(list)
    for l in linhas_cenarios:
        overhead_por_tamanho[l["tamanho"]].append(l["overhead"])

    tamanhos = sorted(overhead_por_tamanho.keys())
    medias = [statistics.mean(overhead_por_tamanho[t]) for t in tamanhos]
    overhead_geral = statistics.mean(l["overhead"] for l in linhas_cenarios)

    fig, ax = plt.subplots(figsize=(7, 5))
    barras = ax.bar([str(t) for t in tamanhos], medias, color=CORES[:len(tamanhos)])
    ax.axhline(10, color="red", linestyle="--", linewidth=1, label="Meta do projeto (<10%)")
    ax.set_xlabel("Tamanho do array")
    ax.set_ylabel("Overhead medio (%)")
    ax.set_title(f"Overhead medio do seletor por tamanho de array\n(media geral: {overhead_geral:.2f}%)")
    ax.legend(fontsize=8)
    for barra, valor in zip(barras, medias):
        ax.annotate(f"{valor:.2f}%", (barra.get_x() + barra.get_width() / 2, barra.get_height()),
                    textcoords="offset points", xytext=(0, 4), ha="center", fontsize=8)
    fig.tight_layout()
    _salvar(fig, "04_overhead_medio")


def grafico_comportamento_por_tipo(linhas_algoritmos):
    tempos = defaultdict(lambda: defaultdict(list))  # tipo -> algoritmo -> [tempos]
    tipos_vistos = []
    for l in linhas_algoritmos:
        if l["tipo_cenario"] not in tipos_vistos:
            tipos_vistos.append(l["tipo_cenario"])
        tempos[l["tipo_cenario"]][l["algoritmo"]].append(l["tempo_medio"])

    algoritmos = ORDEM_ALGORITMOS
    largura = 0.13

    fig, ax = plt.subplots(figsize=(11, 6))
    x = list(range(len(tipos_vistos)))
    for i, alg in enumerate(algoritmos):
        valores = [statistics.mean(tempos[t][alg]) if tempos[t].get(alg) else 1e-6 for t in tipos_vistos]
        posicoes = [xi + i * largura for xi in x]
        ax.bar(posicoes, valores, width=largura, label=alg, color=CORES[i % len(CORES)])

    ax.set_xticks([xi + largura * (len(algoritmos) - 1) / 2 for xi in x])
    ax.set_xticklabels(tipos_vistos)
    ax.set_ylabel("Tempo medio de execucao (s) - escala log")
    ax.set_yscale("log")
    ax.set_title("Comportamento dos algoritmos por tipo de conjunto de dados")
    ax.legend(loc="upper left", fontsize=8, ncol=2)
    fig.tight_layout()
    _salvar(fig, "05_comportamento_por_tipo")




def grafico_overhead_por_cenario(linhas_cenarios):
    """
    mostrando como cada cenário
    contribui para o overhead e se comporta conforme o array cresce.
    """
    ORDEM_CENARIOS = ["Aleatório", "Quase Ordenado", "Invertido", "Duplicatas"]
    MARCADORES = ["o", "s", "^", "D"]

    dados = defaultdict(lambda: defaultdict(list))
    for row in linhas_cenarios:
        dados[row["tipo_cenario"]][row["tamanho"]].append(row["overhead"])

    tamanhos = sorted({row["tamanho"] for row in linhas_cenarios})
    cenarios = [c for c in ORDEM_CENARIOS if c in dados]
    x = list(range(len(tamanhos)))

    fig, ax = plt.subplots(figsize=(9, 5))

    for i, cenario in enumerate(cenarios):
        medias = [
            statistics.mean(dados[cenario][t]) if dados[cenario].get(t) else float("nan")
            for t in tamanhos
        ]
        cor = CORES[i % len(CORES)]
        ax.plot(
            x, medias,
            color=cor,
            marker=MARCADORES[i % len(MARCADORES)],
            linewidth=2,
            markersize=7,
            label=cenario,
        )
        ultimo = medias[-1]
        if ultimo == ultimo: 
            ax.annotate(
                f"{ultimo:.1f}%",
                xy=(x[-1], ultimo),
                xytext=(6, 0),
                textcoords="offset points",
                va="center",
                fontsize=8,
                color=cor,
            )
    ax.axhline(10, color="red", linestyle="--", linewidth=1.5, label="Meta (<10%)")

    ax.set_yscale("log")
    ax.set_xticks(x)
    ax.set_xticklabels([f"{t:,}".replace(",", ".") for t in tamanhos], fontsize=10)
    ax.set_xlabel("Tamanho do array", fontsize=11)
    ax.set_ylabel("Overhead medio (%) - escala log", fontsize=10)
    ax.set_title(
        "Overhead do seletor por tipo de dataset e tamanho\n"
        "(quanto menor, mais eficiente o seletor)",
        fontsize=12, fontweight="bold"
    )
    ax.grid(axis="y", linestyle="--", alpha=0.4)
    ax.grid(axis="x", linestyle=":", alpha=0.3)
    ax.legend(fontsize=9, loc="upper right", framealpha=0.9)

    fig.tight_layout()
    _salvar(fig, "06_overhead_por_cenario")


def gerar_todos_os_graficos(linhas_algoritmos, linhas_cenarios):

    print("\nGerando os graficos ...")
    grafico_tempo_por_algoritmo(linhas_algoritmos)
    grafico_comparacoes_por_algoritmo(linhas_algoritmos)
    grafico_acuracia_por_tipo(linhas_cenarios)
    grafico_overhead_medio(linhas_cenarios)
    grafico_comportamento_por_tipo(linhas_algoritmos)
    grafico_overhead_por_cenario(linhas_cenarios)
    print("Graficos salvos com sucesso")
