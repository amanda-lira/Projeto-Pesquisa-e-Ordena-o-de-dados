def montar_heap(arr, n, i, contadores):
    maior = i
    esq = 2 * i + 1
    dir = 2 * i + 2

    if esq < n:
        contadores['comparacoes'] += 1
        if arr[esq] > arr[maior]:
            maior = esq

    if dir < n:
        contadores['comparacoes'] += 1
        if arr[dir] > arr[maior]:
            maior = dir

    if maior != i:
        arr[i], arr[maior] = arr[maior], arr[i]
        contadores['trocas'] += 1
        montar_heap(arr, n, maior, contadores)

def heap_sort(arr):
    n = len(arr)
    contadores = {'comparacoes': 0, 'trocas': 0}

    # max-heap
    for i in range(n // 2 - 1, -1, -1):
        montar_heap(arr, n, i, contadores)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        contadores['trocas'] += 1
        montar_heap(arr, i, 0, contadores)

    return arr, contadores['comparacoes'], contadores['trocas']
