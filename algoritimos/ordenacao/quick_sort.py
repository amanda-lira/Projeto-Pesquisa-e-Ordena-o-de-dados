import sys
# Aumentar o limite de recursão para lidar com arrays maiores e cenários de pior caso
sys.setrecursionlimit(2000)

def quick_sort(arr):
    comparacoes = 0
    trocas = 0

    def particionar(inicio, fim):
        nonlocal comparacoes, trocas
        # usando o elemento do meio para evitar pior caso em arrays já ordenados
        meio = (inicio + fim) // 2
        arr[meio], arr[fim] = arr[fim], arr[meio]
        trocas += 1
        
        pivo = arr[fim]
        i = inicio - 1
        for j in range(inicio, fim):
            comparacoes += 1
            if arr[j] <= pivo:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                trocas += 1
        
        arr[i + 1], arr[fim] = arr[fim], arr[i + 1]
        trocas += 1
        return i + 1

    def _quick_sort(inicio, fim):
        if inicio < fim:
            p = particionar(inicio, fim)
            _quick_sort(inicio, p - 1)
            _quick_sort(p + 1, fim)

    _quick_sort(0, len(arr) - 1)
    return arr, comparacoes, trocas
