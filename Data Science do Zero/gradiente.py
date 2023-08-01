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

def sum_of_squares(v):
    return sum(v_i**2 for v_i in v)

def particial_derivate(f, v, i, h):
    w = [v_j + (h if j==i else 0)
         for j, v_j in enumerate(v)]
    return (f(w) - f(v))/h

def gradient(f,v,h = 0.0001):
    return [particial_derivate(f,v,i,h)
            for i, _ in enumerate(v)]

def step(v, direction, step_size):
    return [v_i - direction_i*step_size for direction_i, v_i in zip(direction, v)]

def min(f, start):

    value = f(start)
    direction = gradient(f, start)
    start = step(start, direction, 0.01)
    new_value = f(start)
    print(value, new_value)
    count = 0
    while(new_value-value < -0.00000001 ):
        value = new_value
        direction = gradient(f, start)
        start = step(start, direction, 0.01)
        new_value = f(start)
        count +=1

    return start, value

print(min(sum_of_squares, [1,1] ))