import random 
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
       t=len(array)

       if t < 2:
           return 1.0
       
       tamanho_limite = 1000

       if t <= tamanho_limite:
           
            trocas = 0

            for i in range (t):
                for j in range (i+1, t):
                    if array[i] > array[j]:
                            trocas += 1
            maximo_trocas= (t*(t-1))//2
            return 1-(trocas/maximo_trocas)
       
       else: 
           pares_sorteados= 5000

           trocas = 0

           for x in range (pares_sorteados):
               
               i = random.randint(0, t-2)
               j = random.randint (i + 1, t - 1 )

               if array[i] > array[j]:
                   trocas += 1 

           return 1 - (trocas/pares_sorteados)
           
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
    

# '''teste'''
# teste =Caracteristicas()
# array=[i for i in range (1000000)]
# lista_aleatoria = random.sample(array, len(array))

# print(teste.grau_ordenacao(lista_aleatoria))