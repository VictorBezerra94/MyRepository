import matplotlib.pyplot as plt
import numpy             as np
import math
import xlrd
import pandas            as pd
import statistics        as st
import random
from   scipy             import stats

"""probability distribuition function"""
def uniform_pdf(x):
    if x >= 0 and x < 1: return 1
    else: return 0

"""cumulated distribution function"""
def uniform_cdf(x):
    if x<0: return 0
    if x<1: return x
    else: return   1

def normal_pdf(x, mu = 0, sigma=1):
    firs_ele = 1 / ( 2* math.pi * sigma)
    sec_ele  = math.exp(-1*(x-mu)**2/(2*sigma))
    return firs_ele*sec_ele

def random_kid():
    my_list= ['boy', 'girl']
    return random.choice(my_list)

def normal_curve():
    xs = list(*[(x/10.0 for x in range(-50,50))])

    plt.plot(xs, [normal_pdf(x, sigma=1         ) for x in xs], '-' , label = 'mu =  0, sigma = 1'  )
    plt.plot(xs, [normal_pdf(x, sigma=2         ) for x in xs], '--', label = 'mu =  0, sigma = 2'  )
    plt.plot(xs, [normal_pdf(x, sigma=0.5       ) for x in xs], ':' , label = 'mu =  0, sigma = 0.5')
    plt.plot(xs, [normal_pdf(x, sigma=1, mu = -1) for x in xs], '-.', label = 'mu = -1, sigma = 1'  )
    plt.legend()
    plt.show()

def mega_sena(jogos):
    result = []
    results = []
    cartela = list([*(x for x in range(1,61))])
    sorteado = np.random.choice(cartela, 6, replace = False)

    for x in range (1, jogos+1):
        jogo = np.random.choice(cartela, 6, replace = False)
        count = 0
        for x in jogo:
            if x in sorteado: count+=1
        result.append(count)

    results.append(result.count(0))
    results.append(result.count(1))
    results.append(result.count(2))
    results.append(result.count(3))
    results.append(result.count(4))
    results.append(result.count(5))
    results.append(result.count(6))

    return results

def monty_hall():
    doors   = [0,0,1]
    choice  = [0,0,1]
    correct = [0,0,1]
    random.shuffle(choice)
    random.shuffle(correct)

#case1: mantem a porta"""
    if choice == correct: win_1 = 1
    else: win_1 = 0

#case2: Troca a porta
    for i in range(0,3):
        if choice[i] == correct[i] and choice[i] == 0:
            rem = i
    del correct[rem]
    del choice [rem]
    correct.reverse()
    if choice == correct: win_2 = 1
    else: win_2 = 0
    #print(win_1, win_2)
    return win_1, win_2

result = []

    ##
    #for i in range (0,100000):
    #    result.append(monty_hall())
    #
    #acum = 0
    #acum_1 = [acum+result[i][0] for i in range (0, len(result))]
    #acum_2 = [acum+result[i][1] for i in range (0, len(result))]

def normal_cdf(x, mu=0,sigma=1):

    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2

def below_nomal_cdf                 (x, mu, sigma):
    return normal_cdf               (x, mu, sigma)

def above_normal_cdf                (x, mu, sigma):
    return 1-normal_cdf             (x, mu, sigma)

def between_normal_cdf              (lo, hi, mu, sigma):
    return                          (normal_cdf(hi,mu, sigma) - normal_cdf(lo))

def out_normal_cdf                  (lo, hi, mu, sigma):
    return 1-between_normal_cdf     (lo, hi, mu, sigma)

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

def normal_upper_bound(probability, mu, sigma):
    """retorna z para que p(Z <= z) = probability"""
    return inverse_normal_cdf(probability, mu , sigma)

def normal_lower_bound(probability, mu, sigma):
    """retorna z para que p(Z=>z) = probability"""
    return inverse_normal_cdf(1-probability, mu , sigma)

def normal_two_sided_bounds(probability, mu=0, sigma=1):
    """retorna os limites simétricos (sobre a média)
    que contêm a probabilidade específica"""

    tail_probability = (1 - probability) / 2

    """limite superior deveria ter tail_probability acima"""
    upper_bound = normal_lower_bound(tail_probability, mu, sigma)

    """limite inferior deveria ter tail_probability abaixo"""
    lower_bound = normal_upper_bound(tail_probability, mu, sigma)

    return lower_bound, upper_bound

mu = 500
sigma = 15.8

print(normal_two_sided_bounds(0.95, mu, sigma))

#xs = [x / 10.0 for x in range(-50, 50)]
#plt.plot(xs, [normal_cdf(x) for x in xs])
#plt.show()

print(above_normal_cdf(529.50, 500, 15.8))
