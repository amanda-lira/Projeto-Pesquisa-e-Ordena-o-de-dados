import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from algoritimos.ordenacao.bubble_sort import bubble_sort
from algoritimos.ordenacao.merge_sort import merge_sort
from algoritimos.ordenacao.quick_sort import quick_sort
from algoritimos.ordenacao.insertion_sort import insertion_sort
from algoritimos.ordenacao.selection_sort import selection_sort
from algoritimos.ordenacao.heap_sort import heap_sort

class TestOrdenacao(unittest.TestCase):
    def setUp(self):
        self.algoritmos = [
            bubble_sort, merge_sort, quick_sort, 
            insertion_sort, selection_sort, heap_sort
        ]

    def test_corretude(self):
        for algoritmo in self.algoritmos:
            with self.subTest(algoritmo=algoritmo.__name__):
                lista = [11, 4, 7, 1, 3, 9]
                esperado = sorted(lista)
                resultado, _, _ = algoritmo(lista[:])
                self.assertEqual(resultado, esperado)

    def test_lista_vazia(self):
        for algoritmo in self.algoritmos:
            with self.subTest(algoritmo=algoritmo.__name__):
                resultado, _, _ = algoritmo([])
                self.assertEqual(resultado, [])

    def test_lista_ja_ordenada(self):
        for algoritmo in self.algoritmos:
            with self.subTest(algoritmo=algoritmo.__name__):
                lista = [1, 2, 3, 4, 5]
                resultado, _, _ = algoritmo(lista[:])
                self.assertEqual(resultado, [1, 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()