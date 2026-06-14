# projeto/analisador/motor_decisao.py

# ─────────────────────────────────────────────────────────────────────────────
# Motor de Decisão — Seletor Adaptativo de Algoritmos
# Projeto Final de Pesquisa e Ordenação de Dados (POD) — 2026.1
#
# Responsabilidade: receber as características do problema (geradas pelo
# questionário ou pelo analisador direto) e calcular a pontuação de cada
# algoritmo, aplicando bônus e penalidades conforme as condições detectadas.
#
# Entrada esperada (dicionário de características):
#   {
#       "tamanho":           int,   # quantidade de elementos
#       "quase_ordenado":    bool,  # True se o array já está parcialmente ordenado
#       "muitas_duplicatas": bool,  # True se há muitos valores repetidos
#       "estabilidade":      bool,  # True se a estabilidade é necessária
#       "restricao_memoria": bool   # True se há restrição severa de memória
#   }
#
# Saída: dicionário { nome_algoritmo: pontuacao } passado para gerar_recomendacao()
# ─────────────────────────────────────────────────────────────────────────────

# ---------------------------------------------------------------------------
# Informações descritivas de cada algoritmo (usadas em gerar_recomendacao)
# ---------------------------------------------------------------------------
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box

INFO_ALGORITMOS = {
    "Merge Sort": {
        "complexidade": "O(n log n)",
        "aviso": "Uso de memória auxiliar extra (não in-place).",
    },
    "Quick Sort": {
        "complexidade": "O(n log n) médio, O(n²) no pior caso",
        "aviso": "Pode ser instável e degradar o desempenho se o pivô for mal escolhido.",
    },
    "Heap Sort": {
        "complexidade": "O(n log n)",
        "aviso": "Não é um algoritmo estável.",
    },
    "Insertion Sort": {
        "complexidade": "O(n) melhor, O(n²) pior",
        "aviso": "Muito lento para conjuntos de dados grandes.",
    },
    "Selection Sort": {
        "complexidade": "O(n²)",
        "aviso": "Faz muitas comparações, ineficiente para arrays grandes.",
    },
    "Bubble Sort": {
        "complexidade": "O(n²)",
        "aviso": "Geralmente o mais lento, usado apenas para fins didáticos.",
    },
}

# Algoritmos com complexidade O(n²) — eliminados para datasets grandes
_ALGORITMOS_QUADRATICOS = {"Insertion Sort", "Selection Sort", "Bubble Sort"}

# Algoritmos instáveis — penalizados quando estabilidade é exigida
_ALGORITMOS_INSTAVEIS = {"Quick Sort", "Heap Sort", "Selection Sort"}

# Limiar para considerar dataset "grande"
_LIMITE_GRANDE = 100_000


# ---------------------------------------------------------------------------
# Pontuações base
# ---------------------------------------------------------------------------

_PONTUACOES_BASE = {
    "Insertion Sort": 50,
    "Selection Sort": 40,
    "Bubble Sort":    35,
    "Merge Sort":     65,
    "Quick Sort":     70,
    "Heap Sort":      65,
}


# ---------------------------------------------------------------------------
# Função principal: calcular_pontuacoes
# ---------------------------------------------------------------------------

def calcular_pontuacoes(caracteristicas: dict) -> dict:
    """
    Recebe o dicionário de características e devolve um dicionário
    { nome_algoritmo: pontuacao (int, 0–100) } para todos os algoritmos.

    Regras aplicadas
    ----------------
    1. n > 100.000  → algoritmos O(n²) são eliminados (pontuação = 0).
    2. quase_ordenado = True  → +35 pts para Insertion Sort,
                                +15 pts para Bubble Sort.
    3. muitas_duplicatas = True  → +10 pts para Merge Sort,
                                   −10 pts para Quick Sort.
    4. estabilidade = True  → −20 pts para Quick Sort, Heap Sort,
                               Selection Sort.
    5. restricao_memoria = True  → −25 pts para Merge Sort.

    Todas as pontuações são fixadas entre 0 e 100 após os ajustes.
    """
    pontuacoes = dict(_PONTUACOES_BASE)  # cópia das notas base

    tamanho           = caracteristicas.get("tamanho", 0)
    quase_ordenado    = caracteristicas.get("quase_ordenado", False)
    muitas_duplicatas = caracteristicas.get("muitas_duplicatas", False)
    estabilidade      = caracteristicas.get("estabilidade", False)
    restricao_memoria = caracteristicas.get("restricao_memoria", False)

    # ── Regra 1: eliminar O(n²) para datasets grandes ──────────────────
    if tamanho > _LIMITE_GRANDE:
        for alg in _ALGORITMOS_QUADRATICOS:
            pontuacoes[alg] = 0

    # ── Regra 2: array quase ordenado ──────────────────────────────────
    if quase_ordenado:
        pontuacoes["Insertion Sort"] += 35
        pontuacoes["Bubble Sort"]    += 15

    # ── Regra 3: muitas duplicatas ─────────────────────────────────────
    if muitas_duplicatas:
        pontuacoes["Merge Sort"]  += 10
        pontuacoes["Quick Sort"]  -= 10

    # ── Regra 4: necessidade de estabilidade ───────────────────────────
    if estabilidade:
        for alg in _ALGORITMOS_INSTAVEIS:
            pontuacoes[alg] -= 20

    # ── Regra 5: restrição de memória ──────────────────────────────────
    if restricao_memoria:
        pontuacoes["Merge Sort"] -= 25

    # ── Clamp: garante 0 ≤ pontuação ≤ 100 ────────────────────────────
    pontuacoes = {alg: max(0, min(100, pts)) for alg, pts in pontuacoes.items()}

    return pontuacoes


# ---------------------------------------------------------------------------
# Função de exibição: gerar_recomendacao  (mantém interface já usada no main)
# ---------------------------------------------------------------------------

def gerar_recomendacao(pontuacoes: dict, caracteristicas: dict) -> None:
    """
    Seleciona o algoritmo com maior pontuação e exibe a recomendação
    em um Dashboard formatado no terminal usando a biblioteca 'rich'.
    """
    algoritmos_ordenados = sorted(
        pontuacoes.items(), key=lambda x: x[1], reverse=True
    )

    melhor_algoritmo, melhor_pontuacao = algoritmos_ordenados[0]
    alternativas = [alg for alg, pts in algoritmos_ordenados[1:3] if pts > 0]

    info = INFO_ALGORITMOS.get(
        melhor_algoritmo, {"complexidade": "N/A", "aviso": "N/A"}
    )

    justificativas = []
    tamanho           = caracteristicas.get("tamanho", 0)
    quase_ordenado    = caracteristicas.get("quase_ordenado", False)
    muitas_duplicatas = caracteristicas.get("muitas_duplicatas", False)
    estabilidade      = caracteristicas.get("estabilidade", False)
    restricao_memoria = caracteristicas.get("restricao_memoria", False)

    if tamanho > _LIMITE_GRANDE and melhor_algoritmo in {"Merge Sort", "Quick Sort", "Heap Sort"}:
        justificativas.append("Conjunto de dados grande; requer algoritmo eficiente O(n log n).")
    if estabilidade and melhor_algoritmo in {"Merge Sort", "Insertion Sort"}:
        justificativas.append("Atende à necessidade estrita de estabilidade.")
    if quase_ordenado and melhor_algoritmo == "Insertion Sort":
        justificativas.append("Excelente desempenho para arrays quase ordenados.")
    if muitas_duplicatas and melhor_algoritmo == "Merge Sort":
        justificativas.append("Lida muito bem com arrays contendo várias duplicatas.")
    if restricao_memoria and melhor_algoritmo in {"Heap Sort", "Quick Sort"}:
        justificativas.append("Opera 'in-place', respeitando a forte restrição de memória.")

    if not justificativas:
        justificativas.append("Apresenta o melhor equilíbrio de desempenho para estas condições.")

    #  Dashboard com Rich ───────────────────────────
    console = Console()

    tabela = Table(show_header=False, box=box.SIMPLE)
    tabela.add_column("Atributo", style="cyan", justify="right")
    tabela.add_column("Valor", style="white")

    tabela.add_row("Pontuação", f"[bold green]{melhor_pontuacao}/100[/bold green]")
    tabela.add_row("Complexidade", f"[bold yellow]{info['complexidade']}[/bold yellow]")
    
    just_formatadas = "\n".join([f"• {j}" for j in justificativas])
    tabela.add_row("Justificativas", just_formatadas)
    
    tabela.add_row("Avisos", f"[red]{info['aviso']}[/red]")
    
    alts_formatadas = ", ".join(alternativas) if alternativas else "Nenhuma"
    tabela.add_row("Alternativas", f"[dim]{alts_formatadas}[/dim]")

    # Coloca a tabela dentro de um painel elegante
    painel = Panel(
        tabela,
        title=f" Recomendação: [bold magenta]{melhor_algoritmo}[/bold magenta]",
        expand=False,
        border_style="blue"
    )
    
    print("\n")
    console.print(painel)
    print("\n")