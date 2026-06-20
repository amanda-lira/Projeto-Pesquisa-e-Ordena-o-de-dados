import random

def gerar_array_aleatorio(tamanho):
    return [random.randint(0, tamanho * 10) for _ in range(tamanho)]

def gerar_array_quase_ordenado(tamanho):
    arr = list(range(tamanho))
    for _ in range(tamanho // 10):
        i, j = random.sample(range(tamanho), 2)
        arr[i], arr[j] = arr[j], arr[i]
    return arr

def gerar_array_invertido(tamanho):
    return list(range(tamanho, 0, -1))

def gerar_array_com_duplicatas(tamanho, proporcao_duplicatas=0.3):
    arr = []
    elementos_unicos = list(range(int(tamanho * (1 - proporcao_duplicatas))))
    for _ in range(tamanho):
        arr.append(random.choice(elementos_unicos))
    random.shuffle(arr)
    return arr


# tamanho = 20

# print("Array Aleatório:")
# print(gerar_array_aleatorio(tamanho))

# print("\nArray Quase Ordenado:")
# print(gerar_array_quase_ordenado(tamanho))

# print("\nArray Invertido:")
# print(gerar_array_invertido(tamanho))

# print("\nArray com Duplicatas:")
# print(gerar_array_com_duplicatas(tamanho))