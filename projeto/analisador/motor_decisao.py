

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
        "aviso": "Faz muitas comparações, ineficiente para arrays grandes."
    },
    "Bubble Sort": {
        "complexidade": "O(n²)",
        "aviso": "Geralmente o mais lento, usado apenas para fins didáticos."
    }
}

def gerar_recomendacao(pontuacoes, caracteristicas):
    """
    Seleciona o algoritmo com maior pontuação e exibe a justificativa.
    """
    # Ordena os algoritmos pela pontuação (do maior para o menor)
    algoritmos_ordenados = sorted(pontuacoes.items(), key=lambda x: x[1], reverse=True)
    
    melhor_algoritmo, melhor_pontuacao = algoritmos_ordenados[0]
    alternativas = [alg[0] for alg in algoritmos_ordenados[1:3]] 
    
    info = INFO_ALGORITMOS.get(melhor_algoritmo, {"complexidade": "N/A", "aviso": "N/A"})
    
    # Montando as justificativas
    justificativas = []
    if caracteristicas.get("tamanho", 0) > 100000 and melhor_algoritmo in ["Merge Sort", "Quick Sort", "Heap Sort"]:
        justificativas.append("conjunto de dados grande; requer algoritmo eficiente")
    if caracteristicas.get("estabilidade", False) and melhor_algoritmo in ["Merge Sort", "Insertion Sort"]:
        justificativas.append("necessidade de estabilidade atendida")
    if caracteristicas.get("quase_ordenado", False) and melhor_algoritmo == "Insertion Sort":
        justificativas.append("excelente desempenho para arrays quase ordenados")
    
    if not justificativas:
        justificativas.append("melhor equilíbrio de desempenho para as condições atuais")

    # Exibe a saída no formato exigido
    print("\n" + "="*50)
    print(" RECOMENDAÇÃO DO SELETOR ADAPTATIVO")
    print("="*50)
    print(f"Algoritmo recomendado: {melhor_algoritmo}")
    print(f"Pontuação: {melhor_pontuacao}/100")
    print(f"Complexidade esperada: {info['complexidade']}")
    
    print("\nJustificativas:")
    for j in justificativas:
        print(f" - {j}")
        
    print("\nAvisos:")
    print(f" - {info['aviso']}")
    
    print("\nAlternativas:")
    for alt in alternativas:
        print(f" - {alt}")
    print("="*50 + "\n")