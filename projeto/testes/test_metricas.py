import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from algoritimos.ordenacao.bubble_sort import bubble_sort
from algoritimos.ordenacao.merge_sort import merge_sort

class TestMetricas(unittest.TestCase):
    def test_merge_sort_metricas_especificas(self):
        """Valida se o Merge Sort conta 2 trocas para [11, 4, 7]."""
        lista = [11, 4, 7]
        _, _, trocas = merge_sort(lista)
        self.assertEqual(trocas, 2)

    def test_bubble_sort_metricas_especificas(self):
        """Valida trocas do Bubble Sort para [3, 2, 1] (deve ser 3 trocas)."""
        lista = [3, 2, 1]
        _, _, trocas = bubble_sort(lista)
        self.assertEqual(trocas, 3)

    def test_tipo_metricas(self):
        """Garante que as métricas retornadas são sempre inteiros."""
        from algoritimos.ordenacao.quick_sort import quick_sort
        _, comps, trocas = quick_sort([5, 4, 3, 2, 1])
        self.assertIsInstance(comps, int)
        self.assertIsInstance(trocas, int)

if __name__ == '__main__':
    unittest.main()