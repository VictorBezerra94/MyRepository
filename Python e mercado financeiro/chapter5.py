import math

class chapter5():
    def __init__(self):
        pass

    def exercise_1(self, a, b):
        result = a+b
        print(result)
        return result

    def exercise_2(self, a, b, c):
        result = a**3-a*b+b**2-b*c
        print(result)
        return result

    def exercise_3(self, a, b):
        result = math.sqrt(a**2+b**2)-math.sin(a)+math.cos(a+b)
        print(result)
        return result

    def exercise_4(self, x, y):
        z = x+y if x>=y else x-y
        print(z)
        return z

    def exercise_5(self, list):
        tam = len(list)
        result = list[tam-1] if tam>4 else list[0]
        return result

    def exercise_6(self, bolsas):
        simbolo = input('Deseja descobrir o index de qual simbolo? ')
        index = bolsas.index(simbolo)
        return index

    def exercise_7(self, bolsas):
        simbolo = input('Deseja remover qual simbolo? ')
        bolsas.remove(simbolo)
        return bolsas

    def exercise_8(self, lista):
        elem = int(input('Qual numero deseja contar? '))
        cont = 0
        for i in range(0, len(lista)):
            if lista[i] == elem:
                cont +=1
        return cont

    def exercise_9(self, alternative):
        PETR4   = [9.72 ,10.69 ,11.82 ,12.93 ,12.92, 12.82, 13.64, 13.79, 13.78, 13.08, 12.67, 12.83]
        PETRF42 = [ 0.2 , 0.46 , 0.82 , 1.38 , 1.46 , 1.24 , 1.69 , 1.75 , 1.6 ,  1.02 , 0.64 , 0.58]
        retorno = []
        if alternative == 'a':
            return mean(PETR4), mean(PETRF42)

        elif alternative == 'b':
            return pstdev(PETR4), pstdev(PETRF42)

        elif alternative == 'c':

            for i in range(0, len(PETR4)-2):
                retorno.append([(PETR4  [i+1] - PETR4  [i])/PETR4  [i],(PETRF42[i+1] - PETRF42[i])/PETRF42[i]])
            return retorno

        elif alternative == 'd':
            retorno_0 = []
            retorno_1 = []
            retornos = chapter6().exercise_9('c')
            [retorno_0.append(retornos[i][0]) for i in range(0, len(retornos))]
            [retorno_1.append(retornos[i][1]) for i in range(0, len(retornos))]

            return max(retorno_0), max(retorno_1)

print(chapter5().exercise_9('d'))
