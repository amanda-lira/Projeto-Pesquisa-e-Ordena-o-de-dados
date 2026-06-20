import sys

from analisador.questionario import executar_questionario
from analisador.motor_decisao import *

# =====================================================================
# SIMULADORES (MOCKS) - irei substituir qdo fizerem o motor de devisao e as caracteristicas.
# =====================================================================
def mock_extrair_caracteristicas(array):
    print("[Sistema] Analisando o array inserido...")
    return {
        "tamanho": len(array),
        "quase_ordenado": False,
        "muitas_duplicatas": False,
        "estabilidade": True,
        "restricao_memoria": False
    }

""" 
def mock_calcular_pontuacoes(caracteristicas):
    print("[Sistema] Calculando pontuações dos algoritmos...")
    # Lógica de mentira só para testar sua tela
    if caracteristicas.get("tamanho", 0) > 10000:
        return {"Merge Sort": 95, "Quick Sort": 85, "Heap Sort": 80, "Insertion Sort": 10}
    elif caracteristicas.get("quase_ordenado"):
        return {"Insertion Sort": 98, "Merge Sort": 70, "Quick Sort": 60}
    else:
        return {"Merge Sort": 85, "Heap Sort": 80, "Quick Sort": 75, "Insertion Sort": 40}
"""
# =====================================================================

def modo_direto():
    print("\n" + "-"*40)
    print("MODO DIRETO")
    print("-"*40)
    entrada = input("Digite os números do array separados por espaço: ")
    
    try:
        array = [int(x) for x in entrada.split()]
        if not array:
            raise ValueError
    except ValueError:
        print("Erro: Digite números válidos (ex: 5 2 9 1).")
        return

    # Chamando função verdadeira
    caracteristicas = mock_extrair_caracteristicas(array)
    pontuacoes = calcular_pontuacoes(caracteristicas)
    
    # Chamando a SUA função (verdadeira)
    gerar_recomendacao(pontuacoes, caracteristicas)

def modo_questionario():
    # Chamando a SUA função (verdadeira)
    caracteristicas = executar_questionario()
    
    # Chamando função verdadeira
    pontuacoes = calcular_pontuacoes(caracteristicas)
    
    # Chamando a SUA função (verdadeira)
    gerar_recomendacao(pontuacoes, caracteristicas)

def main():
    while True:
        print("\n" + "="*40)
        print("⚙️  SELETOR ADAPTATIVO DE ALGORITMOS ⚙️")
        print("="*40)
        print("1. Modo Direto (Fornecer Array)")
        print("2. Modo Questionário (Responder Perguntas)")
        print("0. Sair")
        
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == '1':
            modo_direto()
        elif opcao == '2':
            modo_questionario()
        elif opcao == '0':
            print("Encerrando o sistema...")
            sys.exit(0)
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()