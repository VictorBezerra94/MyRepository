import matplotlib.pyplot as plt
import numpy             as np
import math
import xlrd
import pandas            as pd
import statistics        as st
import random
from   scipy             import stats
import functools

def vector_add(v,w):
    return [v1 + w1 for v1, w1 in zip(v,w)]

def normal_cdf(x, mu=0,sigma=1):

    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2

def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.00001):
    """encontra o inverso mais próximo usando a busca binária"""
    # se não for padrão, computa o padrão e redimensiona

    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)

    low_z, low_p = -10.0, 0            # normal_cdf(-10) está (muito perto de) 0
    hi_z, hi_p   =  10.0, 1            # normal_cdf(10) está (muito perto de) 1

    while hi_z - low_z > tolerance:

        mid_z = (low_z + hi_z) / 2     # considera o ponto do meio e o valor da
        mid_p = normal_cdf(mid_z)      # função de distribuição cumulativa lá

        if mid_p < p:
            # o ponto do meio ainda está baixo, procura acima

            low_z, low_p = mid_z, mid_p

        elif mid_p > p:
            # """o ponto do meio ainda está alto, procura abaixo"""

            hi_z, hi_p = mid_z, mid_p

        else:
            break

    return mid_z

def moeda():
    data = []
    coin = [0,1]
    for i in range(0,100):
        data.append(random.choice(coin))

    return data

result = [moeda().count(1) for x in range(0,100)]

valor_lim = [inverse_normal_cdf(0.025, 50, 5), inverse_normal_cdf(0.975, 50, 5)]

acum = []

for i in range(0,100):
        if result[i] >= valor_lim[0] and result[i] <= valor_lim[1]: acum.append(1)
        else: 0

print(sum(acum))