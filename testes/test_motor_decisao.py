import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'analisador')))

from motor_decisao import calcular_pontuacoes, _PONTUACOES_BASE, _LIMITE_GRANDE, _ALGORITMOS_QUADRATICOS, _ALGORITMOS_INSTAVEIS

class TestMotorDecisao(unittest.TestCase):

    def setUp(self):
        self.pontuacoes_base = dict(_PONTUACOES_BASE)

    def test_pontuacoes_base(self):
        caracteristicas = {
            "tamanho": 1000,
            "quase_ordenado": False,
            "muitas_duplicatas": False,
            "estabilidade": False,
            "restricao_memoria": False
        }
        pontuacoes = calcular_pontuacoes(caracteristicas)
        self.assertEqual(pontuacoes, self.pontuacoes_base)

    def test_regra_1_tamanho_grande(self):
        caracteristicas = {
            "tamanho": _LIMITE_GRANDE + 1,
            "quase_ordenado": False,
            "muitas_duplicatas": False,
            "estabilidade": False,
            "restricao_memoria": False
        }
        pontuacoes = calcular_pontuacoes(caracteristicas)
        for alg in _ALGORITMOS_QUADRATICOS:
            self.assertEqual(pontuacoes[alg], 0, f"Algoritmo {alg} deveria ser 0 para tamanho grande")
        self.assertEqual(pontuacoes["Merge Sort"], 65)
        self.assertEqual(pontuacoes["Quick Sort"], 70)
        self.assertEqual(pontuacoes["Heap Sort"], 65)

    def test_regra_2_quase_ordenado(self):
        caracteristicas = {
            "tamanho": 1000,
            "quase_ordenado": True,
            "muitas_duplicatas": False,
            "estabilidade": False,
            "restricao_memoria": False
        }
        pontuacoes = calcular_pontuacoes(caracteristicas)
        self.assertEqual(pontuacoes["Insertion Sort"], self.pontuacoes_base["Insertion Sort"] + 35)
        self.assertEqual(pontuacoes["Bubble Sort"], self.pontuacoes_base["Bubble Sort"] + 15)
        self.assertEqual(pontuacoes["Merge Sort"], self.pontuacoes_base["Merge Sort"])

    def test_regra_3_muitas_duplicatas(self):
        caracteristicas = {
            "tamanho": 1000,
            "quase_ordenado": False,
            "muitas_duplicatas": True,
            "estabilidade": False,
            "restricao_memoria": False
        }
        pontuacoes = calcular_pontuacoes(caracteristicas)
        self.assertEqual(pontuacoes["Merge Sort"], self.pontuacoes_base["Merge Sort"] + 10)
        self.assertEqual(pontuacoes["Quick Sort"], self.pontuacoes_base["Quick Sort"] - 10)
        self.assertEqual(pontuacoes["Insertion Sort"], self.pontuacoes_base["Insertion Sort"])

    def test_regra_4_estabilidade(self):
        caracteristicas = {
            "tamanho": 1000,
            "quase_ordenado": False,
            "muitas_duplicatas": False,
            "estabilidade": True,
            "restricao_memoria": False
        }
        pontuacoes = calcular_pontuacoes(caracteristicas)
        for alg in _ALGORITMOS_INSTAVEIS:
            self.assertEqual(pontuacoes[alg], self.pontuacoes_base[alg] - 20, f"Algoritmo {alg} deveria ter -20 pts")
        self.assertEqual(pontuacoes["Merge Sort"], self.pontuacoes_base["Merge Sort"])

    def test_regra_5_restricao_memoria(self):
        caracteristicas = {
            "tamanho": 1000,
            "quase_ordenado": False,
            "muitas_duplicatas": False,
            "estabilidade": False,
            "restricao_memoria": True
        }
        pontuacoes = calcular_pontuacoes(caracteristicas)
        self.assertEqual(pontuacoes["Merge Sort"], self.pontuacoes_base["Merge Sort"] - 25)
        self.assertEqual(pontuacoes["Quick Sort"], self.pontuacoes_base["Quick Sort"])

    def test_combinacao_regras_e_clamp_min(self):
        # Cenário que deve levar a pontuações abaixo de 0, que devem ser clampadas para 0
        caracteristicas = {
            "tamanho": 1000,
            "quase_ordenado": False,
            "muitas_duplicatas": False,
            "estabilidade": True, 
            "restricao_memoria": False
        }

        caracteristicas_com_mais_penalidade = caracteristicas.copy()
        caracteristicas_com_mais_penalidade["muitas_duplicatas"] = True 

        pontuacoes = calcular_pontuacoes(caracteristicas_com_mais_penalidade)
        self.assertEqual(pontuacoes["Quick Sort"], 40)
        self.assertEqual(pontuacoes["Heap Sort"], 45)
        self.assertEqual(pontuacoes["Selection Sort"], 20)

        # Testar um cenário que force a pontuação a ser 0
        caracteristicas_zero = {
            "tamanho": _LIMITE_GRANDE + 1, 
            "quase_ordenado": False,
            "muitas_duplicatas": False,
            "estabilidade": True, 
            "restricao_memoria": False
        }
        pontuacoes_zero = calcular_pontuacoes(caracteristicas_zero)
        self.assertEqual(pontuacoes_zero["Selection Sort"], 0)
        self.assertEqual(pontuacoes_zero["Bubble Sort"], 0)
        self.assertEqual(pontuacoes_zero["Insertion Sort"], 0)

    def test_combinacao_regras_e_clamp_max(self):
        caracteristicas = {
            "tamanho": 1000,
            "quase_ordenado": True,  
            "muitas_duplicatas": False,
            "estabilidade": False,
            "restricao_memoria": False
        }
   
        pontuacoes = calcular_pontuacoes(caracteristicas)
        for alg, pts in pontuacoes.items():
            self.assertLessEqual(pts, 100, f"Pontuação de {alg} excedeu 100")

    def test_caracteristicas_ausentes(self):
        caracteristicas = {}
        pontuacoes = calcular_pontuacoes(caracteristicas)
        self.assertEqual(pontuacoes, self.pontuacoes_base)

        caracteristicas_parciais = {"tamanho": 50000, "estabilidade": True}
        pontuacoes_parciais = calcular_pontuacoes(caracteristicas_parciais)

        expected_pontuacoes = dict(self.pontuacoes_base)
        for alg in _ALGORITMOS_INSTAVEIS:
            expected_pontuacoes[alg] -= 20
        expected_pontuacoes = {alg: max(0, min(100, pts)) for alg, pts in expected_pontuacoes.items()}

        self.assertEqual(pontuacoes_parciais, expected_pontuacoes)

if __name__ == '__main__':
    unittest.main()