# projeto/analisador/questionario.py

def executar_questionario():
    """
    Executa o Modo Questionário via CLI e retorna as características em um dicionário.
    """
    print("\n" + "-"*40)
    print(" MODO QUESTIONÁRIO")
    print("-"*40)
    print("Responda às perguntas abaixo para descrever o problema:\n")
    
    try:
        tamanho = int(input("1. Quantos elementos existem (aproximadamente)? "))
    except ValueError:
        print("Valor inválido. Assumindo tamanho = 1000.")
        tamanho = 1000 
        
    ordenado_str = input("2. Os dados já estão parcialmente ordenados? (s/n): ").strip().lower()
    quase_ordenado = ordenado_str == 's'
    
    duplicatas_str = input("3. Há muitos valores repetidos? (s/n): ").strip().lower()
    muitas_duplicatas = duplicatas_str == 's'
    
    estabilidade_str = input("4. A estabilidade é necessária? (s/n): ").strip().lower()
    estabilidade = estabilidade_str == 's'
    
    memoria_str = input("5. Existe restrição severa de memória? (s/n): ").strip().lower()
    restricao_memoria = memoria_str == 's'
    
    return {
        "tamanho": tamanho,
        "quase_ordenado": quase_ordenado,
        "muitas_duplicatas": muitas_duplicatas,
        "estabilidade": estabilidade,
        "restricao_memoria": restricao_memoria
    }