def busca_sequencial(arr, elemento):
    comparacoes = 0
    for i in range(len(arr)):
        comparacoes += 1
        if arr[i] == elemento:
            return i, comparacoes, 0 # Retorna índice, comparações, trocas (0 para busca)
    return -1, comparacoes, 0 # Elemento não encontrado

