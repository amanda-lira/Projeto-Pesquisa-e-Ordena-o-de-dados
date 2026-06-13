class Caracteristicas:
    
    def analisa (self,array):
        return {

            "tamanho": self.tamanho(array),
            "grau_ordenacao": self.grau_ordenacao(array),
            "duplicatas": self.duplicatas(array),
            "amplitude": self.amplitude(array),
            "tipo": self.tipo(array)
        }
       
    def tamanho(self, array):
        return len(array)
    
    def grau_ordenacao (self, array):
       
       trocas = 0
       t=len(array)
       for i in range (t):
           for j in range (i+1, t):
               if array[i] > array[j]:
                    trocas+=1
       maximo_trocas= (t*(t-1))//2
       return 1-(trocas/maximo_trocas)
    
    def duplicatas (self, array):

        tamanho = len(array)
        unicos= len(set(array))
        duplicados= tamanho-unicos
        return duplicados / tamanho
    
    
    def amplitude (self, array):

        maior=max(array)
        menor = min(array)
        return maior-menor
    

    def tipo(self, array):
        return type(array[0]).__name__
    

