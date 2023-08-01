import matplotlib.pyplot as fig
import numpy as np
import math
import statistics as st

class chapter_1():

    def __init__(self):
        pass
    def exercise_1(self, x , y):
        A = math.pow(x,2)+ math.pow(y,3)
        B = math.sin(x)+ math.cos(y)
        C = math.cos(math.sin(x)+ math.tan(y))
        D = x%y
        E = math.radians(46.2)
        F = math.degrees(3.1)

    def exercise_2(self, x = 3, y = 6):
        A = math.exp(x)-math.log(y)
        B = x*y**2 + y*math.cos(x)
        C = math.sqrt((x/y)+math.log(x+y)+math.tan(x))

    def exercise_3(self):
        list = [3,3,4,1,2,1,1,2,3,4,4,1,1,5,2]
        A = list[2:4]
        B = list[4:9]
        C = list[1:]
        D = list[:]
        E = list[::3]
        F = list[-1:]
        G = list[-3:]
        H = list[0:4]
        I = len(list)
        J = list.count(1)

    def exercise_4(self):
        list = ['dow', 'ibov','ftse','dax','nasdaq','cac']
        A = list[0:3]
        '''B'''
        list.extend(['hong kong', 'merval'])
        C = list.index('nasdaq')
        '''D'''
        list.remove('cac')
        E = list.insert(2,'sp&500')

    #Exercise_5,6, and 8 was skipped because there are better methodis to open and load a file

    def exercise_7(self):
        list = [2,2,3,3,3,-1,-1,-2,0,0,0,2,4,5,1,2,2,0,0,0,2,1,5,5,7,6,5,0,0]
        A = sum(list)
        B = max(list)
        C = min(list)
        D = st.mean(list)
        E = st.median(list)
        F = st.mode(list)
        G = st.stdev(list)
        H = st.pstdev(list)
        I = list.count(0)
        J = list.count(5)
        '''K'''
        list.sort()
        '''L'''
        list.reverse()


chapter_1().exercise_7()