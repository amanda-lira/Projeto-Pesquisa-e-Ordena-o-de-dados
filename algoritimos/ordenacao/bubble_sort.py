def bubble_sort(arr):
    tamanho = len(arr)
    comparacoes = 0
    trocas = 0

    for i in range(tamanho - 1):
        for j in range(tamanho - i - 1):
            comparacoes += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                trocas += 1

    return arr, comparacoes, trocas
