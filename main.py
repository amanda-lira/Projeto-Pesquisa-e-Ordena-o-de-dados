# projeto/main.py

import sys

from analisador.questionario import executar_questionario
from analisador.caracteristicas import Caracteristicas
from analisador.motor_decisao import (
	calcular_pontuacoes,
	gerar_recomendacao
)


def adaptar_caracteristicas(dados_brutos):
	"""
	Converte as características numéricas obtidas do array
	para o formato esperado pelo motor de decisão.
	"""

	return {
		"tamanho": dados_brutos["tamanho"],
		"quase_ordenado": dados_brutos["grau_ordenacao"] > 0.8,
		"muitas_duplicatas": dados_brutos["duplicatas"] > 0.3,
		"estabilidade": False,
		"restricao_memoria": False
	}


def modo_direto():

	print("\n" + "-" * 40)
	print(" MODO DIRETO")
	print("-" * 40)

	entrada = input(
		"Digite os números do array separados por espaço: "
	)

	try:

		array = [int(x) for x in entrada.split()]

		if len(array) < 2:
			print(
				"Erro: Digite pelo menos dois números válidos."
			)
			return

	except ValueError:

		print(
			"Erro: Digite números válidos (ex: 5 2 9 1)."
		)
		return

	analisador = Caracteristicas()

	dados_brutos = analisador.analisa(array)

	caracteristicas = adaptar_caracteristicas(
		dados_brutos
	)

	pontuacoes = calcular_pontuacoes(
		caracteristicas
	)

	gerar_recomendacao(
		pontuacoes,
		caracteristicas
	)


def modo_questionario():

	caracteristicas = executar_questionario()

	pontuacoes = calcular_pontuacoes(
		caracteristicas
	)

	gerar_recomendacao(
		pontuacoes,
		caracteristicas
	)


def main():

	while True:

		print("\n" + "=" * 40)
		print("⚙️  SELETOR ADAPTATIVO DE ALGORITMOS ⚙️")
		print("=" * 40)
		print("1. Modo Direto (Fornecer Array)")
		print("2. Modo Questionário (Responder Perguntas)")
		print("0. Sair")

		opcao = input(
			"\nEscolha uma opção: "
		).strip()

		if opcao == "1":
			modo_direto()

		elif opcao == "2":
			modo_questionario()

		elif opcao == "0":
			print(
				"Encerrando o sistema..."
			)
			sys.exit(0)

		else:
			print(
				"Opção inválida. Tente novamente."
			)


if __name__ == "__main__":
	main()
