def selection_sort(arr):
    tamanho = len(arr)
    comparacoes = 0
    trocas = 0

    for i in range(tamanho):
        idx_min = i
        for j in range(i + 1, tamanho):
            comparacoes += 1
            if arr[j] < arr[idx_min]:
                idx_min = j
        arr[i], arr[idx_min] = arr[idx_min], arr[i]
        if i != idx_min:
            trocas += 1

    return arr, comparacoes, trocas
