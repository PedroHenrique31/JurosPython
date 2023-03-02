"""
        Script para gerar grafico de funções
"""
import math
import numpy as np
from Dominio import Dominio as dom
import matplotlib.pyplot as ploter
from juros import *




dominio=[]
dominio=dom.geraDominio(90.0)

# Inicia cada um dos tipos de juros
emprestimoJurosSimples=JurosSimples()
emprestimoJurosComposto=JurosComposto()
emprestimoJurosConfianca=JurosConfianca()

# Avalia o juros em cada valor de dominio
emprestimoJurosSimples.avaliaJuros(dominio)
emprestimoJurosComposto.avaliaJuros(dominio)
emprestimoJurosConfianca.avaliaJuros(dominio)



#Seleciona os valores até o 36
subDominio=dom.calculaSubDominio(12.0,dominio)
tamanhoSubDom=len(subDominio)
subImagemJurosSimples=emprestimoJurosSimples.primeiros(tamanhoSubDom)
subImagemJurosComposto=emprestimoJurosComposto.primeiros(tamanhoSubDom)
subImagemJurosConfianca=emprestimoJurosConfianca.primeiros(tamanhoSubDom)

# gera vetores dos subdominios
dominioGrafico=np.array(subDominio)
imagemJurosSimples=np.array(subImagemJurosSimples)
imagemJurosComposto=np.array(subImagemJurosComposto)
imagemJurosConfianca=np.array(subImagemJurosConfianca)

# Plota o gráfico
ploter.title("Gráfico dos juros por tempo")
ploter.plot(dominioGrafico,imagemJurosSimples,'b',label="Juros Simples")
ploter.plot(dominioGrafico,imagemJurosComposto,'r',label="Juros Composto")
ploter.plot(dominioGrafico,imagemJurosConfianca,'g',label="Juros Quadratico")
ploter.grid()
ploter.ylabel("Valor a ser pago (R$)")
ploter.xlabel("tempo em meses")
ploter.legend()
ploter.show()

