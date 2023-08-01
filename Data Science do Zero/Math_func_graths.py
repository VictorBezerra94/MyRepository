import matplotlib.pyplot as plt
import matplotlib_venn
import numpy as np
import math
import xlrd
import pandas as pd
import statistics as st
import random
import pptx
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from scipy import stats


def parabola(a,b,c):
    d,e = get_root(a,b,c)
    if a>b:
        x1,x2 = d,e
    else:
        x1,x2 = e,d

    d,e = int(x1*10), int(x2*10)
    xm = int((d+e)/2)
    x = list([*(x/10 for x in range(xm-50, xm+50))])
    y = [a*x**2 + b*x + c for x in x]
    ax = plt.subplot(111)
    plt.plot(x,[a*x**2 + b*x + c for x in x])
    ax.text( x= x1, y = a*x1**2 + b*x1 + c, s = 'x1')
    ax.text( x= x2, y = a*x2**2 + b*x2 + c, s = 'x2')
    ax.text( x= (x2+x1)/2-0.5, y = a*((x2+x1)/2)**2-1 + b*(x2+x1)/2 + c, s = 'max/min')
    ax.grid(True)
    #plt.show()

def get_root(a,b,c):
    delta = b**2 - 4*a*c

    if delta >= 0:
        x1 = (-b+math.sqrt(delta))/(2*a)
        x2 = (-b-math.sqrt(delta))/(2*a)

    else:
        x1,x2 = 'none', 'none'

    return x1,x2

def bissection_method(func, a , b, A, B, C):
    func_a = func(A,B,C,a)
    func_b = func(A,B,C,b)

    if func(a,A,B,C) > 0:
        max = func(A,B,C,a)
        min = func(A,B,C,b)
        a_max = True
    else:
        max = func(A,B,C,b)
        min = func(A,B,C,a)
        a_max = False

    test = func((a+b)/2, A,B,C,)

    if test<-0.001:
        if a_max == True:
            b = (a+b)/2
        else:
            a = (a+b)/2
        return bissection_method(func, a, b,A,B,C,)

    elif test > 0.001:
        if a_max == True:
            a = (a+b)/2
        else:
             b = (a+b)/2
        return bissection_method(func, a, b,A,B,C,)

    else:
        return (a+b)/2

def second_degree(a,b,c,x):

    return a*x**2+b*x-c


print(bissection_method(second_degree, -4, 1, 1, 2, 1))


