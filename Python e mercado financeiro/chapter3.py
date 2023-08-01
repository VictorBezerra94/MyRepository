import matplotlib.pyplot as plt
import numpy as np
import math
import xlrd
import pandas as pd
import statistics as st
from scipy import stats

class chapter3():
    def __init__(self):
        pass

    def exemple1(self):
        set1 = np.arange(1,21)
        set1 = np.array(set1)
        set2 = np.array([10,9,8,9,9,8,10,11,15,7,8,7,8,10,10,10,11,9,10,8])
        plt.figure()
        f, (ax1,ax2) = plt.subplots(2,1)
        ax1.hist(set2, bins = 5)
        ax2.boxplot(set2)
        plt.show()

    def exemple2(self):
        set1 = np.random.randint(1,60,100)
        set1 = np.array(set1)
        plt.figure()
        plt.plot(set1)
        plt.xlabel('Indice')
        plt.ylabel('Valor')
        plt.show()

    def exemple2_2(self):
        set1 = np.random.rand(100)
        set1 = np.array(set1)
        plt.figure()
        plt.plot(set1)
        plt.xlabel('Indice')
        plt.ylabel('Valor')
        plt.show()

    def exemple2_3(self):
        set1 = np.random.uniform(-1,1,100)
        set1 = np.array(set1)
        plt.figure()
        plt.plot(set1)
        plt.xlabel('Indice')
        plt.ylabel('Valor')
        plt.show()

    def exercise_1(self):
        x = [5,5,5,4,3,2,4,1,1,1,3,3,3,3,3,3,2,3,1,2,1,2,5,4,3,1,3]
        plt.subplots(212)
        plot.hist(x, bins=5, color = black)
        plt.show()

    def exercise_2(self):
        p = np.array([6,7,8,7,5,5,6,4,7,10,10,11,10,11,10,12,9,8,7,8,6,7])
        for i in range(len(p)-1):
            ret = (p[i+1]-p[i])/p[i]

        plt.subplot(211)
        plt.plot(p)
        plt.subplot(212)
        plt.hist(p, bins=5)
        #ax2.plot(ret)
        #print(ax1)
        plt.show()

    def exercise_3(self):
        dados = [-2,-3,-1,-1,-1,1,2,1,-1,-2,1,1,2,2,1,1,2,2,3,2,1,1,-1,-1,2,3,2,1,2,-1,-3,2]
        dados = np.array(dados)
        retorno = [(dados[i+1]-dados[i])/dados[i] for i in range(0, len(dados)-1)]
        x = [i for i in range(0, len(dados))]
        x_ret = [i for i in range(0, len(dados)-1)]

        fig, ax = plt.subplots(2)
        ax[0].plot(x_ret, dados[0:-1])
        ax[1].plot(x_ret, retorno)
        plt.show()

        print(type(x), type(dados))

chapter3().exercise_3()

#print(f'set1: {set1}, \nset2: {set2}')