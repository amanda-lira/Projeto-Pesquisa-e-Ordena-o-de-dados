import time
import copy

class AvaliadorDesempenho:
    def __init__(self, funcao_algoritmo, num_execucoes=5):
        self.funcao_algoritmo = funcao_algoritmo
        self.num_execucoes = num_execucoes

    def executar(self, arr, elemento_busca=None):
        tempo_total = 0
        comparacoes_totais = 0
        trocas_totais = 0

        for _ in range(self.num_execucoes):
            copia_arr = copy.deepcopy(arr)  # Garante um array novo sem alterações das execuções passadas.
            tempo_inicio = time.perf_counter()
            
            if elemento_busca is not None:
                _, comparacoes, trocas = self.funcao_algoritmo(copia_arr, elemento_busca)
            else:
                _, comparacoes, trocas = self.funcao_algoritmo(copia_arr)
            
            tempo_fim = time.perf_counter()

            tempo_total += (tempo_fim - tempo_inicio)
            comparacoes_totais += comparacoes
            trocas_totais += trocas

        tempo_medio = tempo_total / self.num_execucoes
        comparacoes_medias = comparacoes_totais / self.num_execucoes
        trocas_medias = trocas_totais / self.num_execucoes

        return {
            "tempo_medio": tempo_medio,
            "comparacoes_medias": comparacoes_medias,
            "trocas_medias": trocas_medias
        }