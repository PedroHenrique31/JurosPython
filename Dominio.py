"""
        Script pra gerar uma função de dominio
"""
class Dominio:
        def geraDominio(maximo):
                iterador=1/100
                n=0.0
                a=[]
                while(n<maximo):
                        a.append(n)
                        n+=iterador
                return a
        def calculaSubDominio(valor,conjuntoDominio):
                tam=len(conjuntoDominio)
                subDom=[]
                i=0
                while(conjuntoDominio[i]<=valor):
                        subDom.append(conjuntoDominio[i])
                        i+=1
                return subDom

