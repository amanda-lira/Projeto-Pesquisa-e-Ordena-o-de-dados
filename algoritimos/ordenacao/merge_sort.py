def merge_sort(arr):
    comparacoes = 0
    trocas = 0

    if len(arr) > 1:
        meio = len(arr) // 2
        metade_esquerda = arr[:meio]
        metade_direita = arr[meio:]

        metade_esquerda, comp_esq, trocas_esq = merge_sort(metade_esquerda)
        metade_direita, comp_dir, trocas_dir = merge_sort(metade_direita)

        comparacoes += comp_esq + comp_dir
        trocas += trocas_esq + trocas_dir

        i = j = k = 0

        while i < len(metade_esquerda) and j < len(metade_direita):
            comparacoes += 1
<<<<<<< HEAD
            if metade_esquerda[i] <= metade_direita[j]:
=======
            if metade_esquerda[i] < metade_direita[j]:
>>>>>>> origin/feature/validacao
                arr[k] = metade_esquerda[i]
                i += 1
            else:
                arr[k] = metade_direita[j]
                j += 1
<<<<<<< HEAD
                trocas += (len(metade_esquerda) - i)
            k += 1
=======
            k += 1
            trocas += 1 # Cada atribuição a arr[k] pode ser considerada uma troca em termos de movimentação de dados
>>>>>>> origin/feature/validacao

        while i < len(metade_esquerda):
            arr[k] = metade_esquerda[i]
            i += 1
            k += 1
<<<<<<< HEAD
=======
            trocas += 1
>>>>>>> origin/feature/validacao

        while j < len(metade_direita):
            arr[k] = metade_direita[j]
            j += 1
            k += 1
<<<<<<< HEAD
=======
            trocas += 1
>>>>>>> origin/feature/validacao

    return arr, comparacoes, trocas
