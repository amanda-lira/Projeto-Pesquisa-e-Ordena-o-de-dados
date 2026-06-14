# projeto/analisador/questionario.py

def executar_questionario():
    """
    Executa o Modo Questionário via CLI com validação de erros e dicas de UX.
    """
    print("\n" + "="*55)
    print(" MODO QUESTIONÁRIO AVANÇADO")
    print("="*55)
    print("Responda às perguntas para que o motor de decisão")
    print("encontre o melhor algoritmo para o seu caso.\n")
    
    # 1. Validação de Tamanho (Aceita apenas números maiores que zero)
    while True:
        try:
            tamanho = int(input("1. Quantos elementos existem no dataset? (Ex: 1000, 50000): "))
            if tamanho > 0:
                break
            print(" Erro: Por favor, digite um número maior que zero.\n")
        except ValueError:
            print(" Erro: Entrada inválida. Digite apenas números inteiros.\n")
            
    # 2. Validação de Ordenação
    while True:
        print("\n DICA: Um array 'quase ordenado' tem poucos elementos fora do lugar.")
        resp = input("2. Os dados já estão parcialmente ordenados? (s/n): ").strip().lower()
        if resp in ['s', 'n']:
            quase_ordenado = (resp == 's')
            break
        print(" Erro: Responda apenas com 's' (sim) ou 'n' (não).")
        
    # 3. Validação de Duplicatas
    while True:
        resp = input("\n3. Há muitos valores repetidos no conjunto de dados? (s/n): ").strip().lower()
        if resp in ['s', 'n']:
            muitas_duplicatas = (resp == 's')
            break
        print(" Erro: Responda apenas com 's' (sim) ou 'n' (não).")
        
    # 4. Validação de Estabilidade
    while True:
        print("\n DICA: Estabilidade garante que elementos repetidos mantenham a ordem original.")
        resp = input("4. A estabilidade do algoritmo é obrigatória para você? (s/n): ").strip().lower()
        if resp in ['s', 'n']:
            estabilidade = (resp == 's')
            break
        print(" Erro: Responda apenas com 's' (sim) ou 'n' (não).")
        
    # 5. Validação de Memória
    while True:
        resp = input("\n5. Existe restrição severa de memória RAM no ambiente? (s/n): ").strip().lower()
        if resp in ['s', 'n']:
            restricao_memoria = (resp == 's')
            break
        print(" Erro: Responda apenas com 's' (sim) ou 'n' (não).")
        
    print("\n Respostas registradas com sucesso! Analisando...\n")
    
    return {
        "tamanho": tamanho,
        "quase_ordenado": quase_ordenado,
        "muitas_duplicatas": muitas_duplicatas,
        "estabilidade": estabilidade,
        "restricao_memoria": restricao_memoria
    }