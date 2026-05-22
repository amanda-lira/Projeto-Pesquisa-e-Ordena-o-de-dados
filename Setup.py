import os

# Define as pastas do projeto
pastas = [
    "projeto/algoritmos/ordenacao",
    "projeto/algoritmos/busca",
    "projeto/analisador",
    "projeto/validacao",
    "projeto/testes",
    "projeto/utils"
]

# Define os arquivos do projeto
arquivos = [
    "projeto/analisador/caracteristicas.py",
    "projeto/analisador/motor_decisao.py",
    "projeto/analisador/questionario.py",
    "projeto/validacao/validar_seletor.py",
    "projeto/testes/test_seletor.py",
    "projeto/utils/benchmark.py",
    "projeto/utils/gerador.py",
    "projeto/utils/contador.py",
    "projeto/main.py",
    "projeto/README.md"
]

# Cria os diretórios
for pasta in pastas:
    os.makedirs(pasta, exist_ok=True)
    print(f"Pasta criada: {pasta}")

# Cria os arquivos vazios
for arquivo in arquivos:
    with open(arquivo, 'w') as f:
        pass 
    print(f"Arquivo criado: {arquivo}")

print("\n✅ Estrutura do projeto montada com sucesso!")