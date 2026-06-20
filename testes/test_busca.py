import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from algoritimos.busca.busca_binaria import busca_binaria
from algoritimos.busca.busca_sequencial import busca_sequencial

class TestBusca(unittest.TestCase):
    def setUp(self):
        self.algoritmos = [busca_binaria, busca_sequencial]

    def test_busca_sucesso(self):
        for algoritmo in self.algoritmos:
            with self.subTest(algoritmo=algoritmo.__name__):
                lista = [1, 3, 4, 7, 9, 11]
                indice, _, _ = algoritmo(lista, 7)
                self.assertEqual(indice, 3)

    def test_busca_falha(self):
        for algoritmo in self.algoritmos:
            with self.subTest(algoritmo=algoritmo.__name__):
                lista = [1, 3, 4, 7, 9, 11]
                indice, _, _ = algoritmo(lista, 100)
                self.assertEqual(indice, -1)

if __name__ == '__main__':
    unittest.main()