"""
        Script para calcular os valores de juros
"""
class Juros:
        def __init__(self,taxaJuros=0.0,Capital=1.0):
                self.taxaJuros=taxaJuros
                self.capital=Capital
        def calculaJuros(self,tempo):
                return 1.0
        def avaliaJuros(self,dominio):
                tamanho=len(dominio)
                self.Imagem=[0]*tamanho
                for i in range(0,tamanho):
                        self.Imagem[i]=self.calculaJuros(dominio[i])
        def primeiros(self,n):
                subImagem=[0]*n
                for i in range(0,n):
                        subImagem[i]=self.Imagem[i]
                return subImagem
class JurosSimples(Juros):
        def __init__(self,taxaJuros=0.14,Capital=1.0):
                super().__init__(taxaJuros,Capital)
        #Sobrescreve
        def calculaJuros(self,tempo):
                e=self.taxaJuros*tempo+1
                return self.capital*e
                
class JurosComposto(Juros):
        def __init__(self,taxaJuros=0.14,Capital=1.0):
                super().__init__(taxaJuros,Capital)
        #Sobrescreve
        def calculaJuros(self,tempo):
                e=(1+self.taxaJuros)**tempo
                return self.capital*e
class JurosConfianca(Juros):
        def __init__(self, taxaJuros=0.14,Capital=1,grauConfianca=0.8):
                super().__init__(taxaJuros,Capital)
                self.grauConfianca=2-grauConfianca
        #Sobrescreve
        def calculaJuros(self,tempo):
                e=(tempo*self.taxaJuros)+1
                e=e**self.grauConfianca
                return self.capital*e               
