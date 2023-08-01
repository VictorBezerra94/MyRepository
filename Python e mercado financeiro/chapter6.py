import numpy as np
import math
from math import cos, exp
import matplotlib.pyplot as plt

class chapter7():
    def __init__(self):
        pass

    def exemple_1(self):
        n = int(input('Numero de pontos = '))
        x = np.linspace(-2,2,n)
        y = [exp(-i**2) for i in x]
        coef = np.polyfit(x,y,2)
        plt.plot(x,y)
        plt.plot(x, [coef[2]+coef[1]*i+coef[0]*i**2 for i in x],'--')
        plt.show()

    def exemple_2(self):
        x = np.linspace(0,20,200)
        y = [exp(-0.1*i)*cos(i) for i in x]
        y = np.array(y)
        plt.plot(x,y)
        plt.grid()
        plt.title('exp(-0.1x)*cos(x)')
        plt.xlabel('x')
        plt.ylabel('y = f(x)')
        coef = np.polyfit(x,y,1)
        plt.plot(x, [coef[1]+coef[0]*i for i in x], '--')
        plt.show()

    def exemple_3(self):
        vet = np.arange(10)
        mat = vet.reshape(5,2)
        max = mat.max (axis=1)
        min = mat.min (axis=1)
        avg = mat.mean(axis=1)
        std = mat.std (axis=1)
        print(max, min, avg, std)

    def exemple_4(self):
        x = [2,  5, 7, 4, 10 , 80 , 1  ,2 ]
        y = [-3,-5, 2, 1,  4 , -5 , 3,  20]
        x = np.array(x)
        y = np.array(y)
        z = x**2+10*y
        z = z.reshape(2,4)
        print(z)

    def exemple_5(self):
        x = np.array([2,1,3])
        y = np.array([2,1,3])
        y.sort()
        z = x-y
        print(z)

    def exemple_6(self):
        A = np.array( [ [2,5,7], [4,10,1], [1,2,1] ] )
        par = 0
        impar = 0
        for elem in A:
            for x in elem:
                if x%2 ==0: par +=1
                else:          impar+=1

        return par, impar

    def exemple_7(self):
        A = np.array( [ [2,5,7], [4,10,1], [1,2,1] ] )
        l,c = np.where(A==A.max())
        print(l,c)

    def exemple_8(self):
        A = [[2000, 1000 , 500 , 5000 ], [1000, 2500, 2000, 0]]
        B = [30.43, 13.91, 7.42, 47.96]
        print(np.matmul(A,B))

    def exemple_9(self):
        A = [[0.15,0.10,0.06], [1,1,-1], [1,1,1]]
        B = [20000,0   ,200000]
        X = np.linalg.solve(A,B)
        print('Alto  risco = ',  X[0])
        print('Medio risco = ',  X[1])
        print('Baixo risco = ',  X[2])

    def exercise_1(self, X, n):

        x = [i for i in np.arange(0,n+0.2, 0.2)]
        y = [X[0]*i + X[1] for i in x]
        plt.plot(x,y, color = 'black' , linewidth = 0.2)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Reta: y = ax + b')
        plt.show()

    def exercise_2(self, X, n):
        x = [i for i in np.arange(0,n+0.2, 0.2)]
        y = [X[0]*i**2 + X[1]*i + X[2] for i in x]
        plt.plot(x,y, color = 'black' , linewidth = 2)
        plt.xlabel('x')
        plt.ylabel('y ')
        plt.title('Parabola: y = ax^2 + bx + c')
        plt.show()

    def exercise_3(self, X, n):
        x = [i                                     for i in np.arange(0,n+0.2, 0.2)]
        y = [X[0]*i**3 + X[1]*i**2 + X[2]*i + X[3] for i in x]
        plt.plot(x,y, color = 'black' , linewidth = 2)
        plt.xlabel('x')
        plt.ylabel('y ')
        plt.title('Cubica: y = ax^3 + bx^2 + cx + d')
        plt.show()

    def exercise_4(self, X, Y, n):
        x = [i for i in np.arange(0,n+0.2, 0.2)]
        y = [X[0]*i    + X[1]          for i in x]
        z = [Y[0]*i**2 + Y[1]*i + Y[2] for i in x]
        plt.plot(x,y, color = 'black' , linewidth = 2, label = 'reta')
        plt.plot(x,z, color = 'red'   , linewidth = 2, linestyle = '--', marker = '*', markersize = 8, label = 'parabola' )
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title ('Grafico de duas equações')
        plt.legend()
        plt.show()

    def exercise_5(self, n, taxa, amp, freq):
        x = [i for i in np.arange(0,n+0.2, 0.2)]
        exponencial = [math.exp(taxa*i) for i in x]
        trigonometrica = [amp*math.cos(freq*i) for i in x]
        plt.plot(x,exponencial   ,color = 'red'  , linewidth = 2, label = 'exponencial')
        plt.plot(x,trigonometrica,color = 'blue' , linewidth = 2, label = 'trigonometrica', linestyle = '--', marker = '*', markersize = 8 )
        plt.title ('Grafico de duas equações')
        plt.legend()
        plt.show()

    def exercise_6(self, amp, freq ,n, a, b, A, B):
        x = [i for i in np.arange(0,n+0.2, 0.2)]
        p = np.array([amp*cos(freq*i) for i in np.arange(0, n+0.2, 0.2)])
        qo = a+b*p
        qd = A-B*p
        plt.plot(x ,qo , label = 'Oferta' , linewidth = 2, color = 'red' )
        plt.plot(x ,qd , label = 'Demanda', linewidth = 2, color = 'blue', marker = '*', markersize = 8, linestyle = '--',)
        plt.title('Oferta X demanda')
        plt.grid()
        plt.show()

    def exercise_7(self, list):
        return np.array(list)

    def exercise_8(self):
        list = np.zeros(10)
        list[5] = 11
        print(list)

    def exercise_9(self):
        return np.arange(7,22,1)

    def exercise_10(self, A):
        A = np.array(A)
        return (A*9/5+32)

    def exercise_11(self, teste, lista):
        lin, col = np.shape(lista)
        validator = False
        for i in np.arange(0,lin,1):
            for j in np.arange(0,col,1):
                if teste == lista[i][j]: validator = True

        if validator == True:
            print('Achou')
        else:
            print('Nao achou')

    def exercise_12(self, escalar, lista):
        lista = np.array(lista)
        print(lista*escalar)

    def exercise_13(self, vetor_1, vetor_2):
        vetor_1 = np.array(vetor_1)
        vetor_2 = np.array(vetor_2)
        max_indice = np.where(vetor_1 == vetor_1.max())
        return vetor_2[max_indice]

    def exercise_14(self,x ,y):
        x = np.array(x)
        y = np.array(y)
        y.sort()
        z = x-y
        print(z)

    def exercise_15(self, x, y):
        x = np.array(x)
        y = np.array(y)
        z = np.append(x,y)
        print(z)

    def exercise_16(self, lista):
        x = [x for x in np.arange(0, len(lista))]
        lista = np.array(lista)
        a,b = np.polyfit(x,lista,1)
        plt.plot(x,lista)
        plt.plot(x, [a*x + b for x in x])
        plt.show()

    def exercise_17(self):
        A = [1,4,5,12,14,-5,8,9,0,17,-6,7,11,19,21]
        A = np.array(A)
        A = A.reshape(3,5)
        B = A[0:2,0:4]
        C = A[0:1,0:]
        D = A[0:,2]
        E = A[0:,2:]

    def exercise_18(self):
        A = np.zeros(6).reshape(3,2)
        B = np.ones(8).reshape(4,2)
        C = np.identity(10)
        D1 = np.array([-2,5,3,0]).reshape(2,2)
        D2 = np.array([1,-1,6,5]).reshape(2,2)
        D = D1+D2
        E = np.matmul(D1,D2)+D2
        F = np.matmul(np.linalg.inv(D1),D2)

    def exercise_19(self):
        A = np.array([2,-1,3,1,0,-5,4,1,-1,8,7,9,1,2,5,3]).reshape(4,4)
        det = np.linalg.det(A)
        print(det)

    def exercise_20(self):
        C = np.array([0,-4,50,1,14,-5,-8,9,0,17,-6,70,11,19,21]).reshape(5,3)
        lin,col = np.shape(C)
        mat = np.random.rand(5,5)
        print(mat)

    def exercise_21(self, list):
        list = np.array(list)
        i,j = np.shape(list)
        par = 0
        impar = 0

        for a in range(0,i):
            for b in range(0,j):
                if list[a][b]%2 == 0:
                    par   += 1
                else:
                    impar += 1

        return par, impar