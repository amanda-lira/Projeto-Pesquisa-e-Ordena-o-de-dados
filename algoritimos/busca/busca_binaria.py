def busca_binaria(arr, elemento):
    comparacoes = 0
    inicio = 0
    fim = len(arr) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        comparacoes += 1
        if arr[meio] == elemento:
            return meio, comparacoes, 0
        elif arr[meio] < elemento:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1, comparacoes, 0


