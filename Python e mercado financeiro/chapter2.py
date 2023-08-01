import matplotlib.pyplot as fig
import numpy as np
import math
import statistics as st

class chapter2:
    def __init__(self):
        pass

    def exercise_1(self):
        x = int(input("digite um numero"))
        if x >= 0: print("valor maior ou igual a zero")
        else: print ("valor menor do que zero")

    def exercise_2(self):
        a = int(input("valor do lado a"))
        b = int(input("valor do lado b"))
        c = int(input("valor do lado c"))
        if a == b and a == c: print("Triangulo equilatero")
        elif a == b or a == c or b == c: print("Triangulo isoceles")
        else: print("Triangulo escaleno")

    def exercise_3(self):
        compra = float(input("valor de compra"))
        venda = float(input("valor de venda"))
        if (venda/compra)<1.1: print("lucro menor do que 10%")
        elif (venda/compra)>=1.1 and (venda/compra)<=1.2: print("lucro entre 10% e 20%")
        else: print("lucro maior do que 20%")

    def exercise_4(self):
        baixa = float(input("baixa historica"))
        alta = float(input("alta historica"))
        suporte = baixa + 0.15*(alta-baixa)
        resistencia = baixa + 0.3*(alta-baixa)
        valor_atual = float(input("valor atual"))
        if valor_atual >= suporte and valor_atual <= resistencia: print("Valor atual da acao esta dentro da faixa suporte-resitencia")
        else: print("Valor atual da acao esta fora da faixa suporte-resistencia")

    def exercise_5(self):
        A = float(input("A"))
        B = float(input("B"))
        C = float(input("C"))
        D = float(B**2 - 4*A*C)
        print(D)

        if D < 0: print("Nao ha raizes reais para esta equacao")
        else:
            x1 = float(-B+math.sqrt(D))/(2*A)
            x2 = float(-B-math.sqrt(D))/(2*A)
            print("As raizes sao x1 = %f e x2 = %f" % (x1, x2))

    def exercise_6(self):
        #conditions
        valor_compra = float(input("valor da compra em R$"))
        if valor_compra>0 and valor_compra <= 20: print("valor a ser pago eh R$%.2f"     %( valor_compra*0.95))
        if valor_compra>20 and valor_compra <= 50: print("valor a ser pago eh R$%.2f"    %( valor_compra*0.90))
        if valor_compra>50 and valor_compra <= 100: print("valor a ser pago eh R$%.2f"   %( valor_compra*0.85))
        if valor_compra>100 and valor_compra <= 1000: print("valor a ser pago eh R$%.2f" %( valor_compra*0.80))
        if valor_compra>1000: print("valor a ser pago eh R$%.2f" % (valor_compra*0.70))

    def exercise_7(self):
        n = int(input("Numero total de pedidos"))
        par=[]
        impar=[]
        i = 0
        for i in range(n):
            a = int(input("pedido %d" % (i+1)))
            if a%2==0: par.append(a)
            else: impar.append(a)
        par = np.array(par)
        impar = np.array(impar)
        total_par   =  sum(par)
        total_impar =   sum(impar)
        print("total par = %.2f, e total impar = %.2f" %(total_par, total_impar))

    def exercise_8(self):
        numerador = np.arange(70,0,-1)
        denominador = 7*np.arange(1,71)
        cociente = numerador/denominador
        S = sum(cociente)
        print(S)

    def exercise_9(self):
        par = []
        impar = []
        n = int(input("n"))
        for i in range (n):
            a = int(input("a"))
            if a%2==0: par.append(a)
            else: impar.append(a)
        par = np.array(par)
        impar = np.array(impar)
        soma_par=sum(par)
        soma_impar=sum(impar)
        pares = len(par)
        impares = len(impar)
        print("%d pares, %d soma pares, %d impares, %d soma impares" % (pares, soma_par, impares, soma_impar))

    def exercise_10(self):
        n = int(input("numero de termos"))
        x = float(input("limite de integracao"))
        den1 = [1]
        den1Aux = np.arange(1,n)
        den1.extend(den1Aux)
        for i in range(n):
            den1[i] = math.factorial(den1[i])
        den2 = np.arange(1, 2*n+1, 2)
        pot = np.arange(1, 2*n+1, 2)
        aux =[]
        for i in range (n):
            if i%2==0: aux.append(1)
            else: aux.append(-1)
        aux = np.array(aux)
        coc = []
        for i in range(n):
            a = math.pow(x,pot[i])/(den1[i]*den2[i])*aux[i]
            coc.append(a)
        np.array(coc)
        print(sum(coc))
        print(den1 ,den2, aux)

    def exercise_11(self):
        b = 1
        acum = 0
        teste = 1
        n = 0
        while teste > 0.0009:
            c = 4
            d = b+2
            b=b+2
            acum_old = acum
            acum = acum + ((c/d)*math.pow(-1,n))
            teste = acum - acum_old
            teste = math.fabs(teste)
            n = n+1
        print(4-acum)

    def exercise_12(self):
        n = int(input("digite o numero de termos da soma n"))
        range =np.arange(2,n+1)
        impar=np.arange(3,2*n+1,2)
        total = 1 + sum(impar/range)
        print(total)

    def exercise_14(self):
        lista = ["a1", "a2", "a3", "b1", "b2", "b3"]
        acao = input("nome da acao ")
        for i in range (len(lista)):
            if lista[i] == acao:
                print("acao foi encontra pela primeira vez no indice %d" %i)

    def exercise_15(self):
        list = ['bbdc4', 'itub4','petr4','petr4','bbas3','petr4','sanb4','petr4','bpac3','petr4']
        tam = len(list)
        for i in range(0, tam):
            for j in range(0, tam):
                if j!=i:
                    if list[i] == list[j]:
                        return j


    def exercise_16(self):
        lista = [['a','b','c'], ['1','2'], ['a1', 'a2']]
        for x in lista:
            print(x)


    def exercise_17(self):
        lista = [['a','b','c'], ['1','2'], ['a1', 'a2']]
        for x in lista:
            for i in x:
                print(i)

    def exercise_18(self):
        lista = [[1,2,1], [3,-1,4,5], [0,0,1,2,-1], [-1,-1,2,2,-1,2,-1], [3,2,0], [1,1,-1,0,2]]
        nova_lista = []
        [nova_lista.extend(x) for x in lista]

        print('soma          = ' , sum(nova_lista))
        print('max           = '  ,max(nova_lista))
        print('min           = '  ,min(nova_lista))
        print('avg           = '  ,st.mean(nova_lista))
        print('moda          = ' ,st.mode(nova_lista))
        print('desvio padrao = ' ,st.pstdev(nova_lista))

    def exercise_19(self):
        lista = [['ontem', 'hoje', 'amanha'], ['sp', 'rj', 'mg', 'ce'], ['sao paulo', 'rio', 'santos', 'cuiaba']]
        nova_lista = []
        for y in lista:
            for i in y:
                nova_lista.append(i)

        nova_lista.extend(['ferias', 'negocios'])
        nova_lista.sort()

    def exercise_20(self):
        let = ['a', 'b', 'c', 'a', 'd', 'f', 'a', 'b', 'b', 'd', 'c']
        new_list = []
        for x in let:
            if x not in new_list:
                new_list.append(x)
        print(new_list)

chapter2().exercise_20()



