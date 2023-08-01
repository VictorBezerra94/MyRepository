import matplotlib.pyplot as plt
import numpy as np
import math
import xlrd
import pandas as pd
import statistics as st
from scipy import stats

#Vetores:
#Introduction: Lists are Python objects in which we can't do arithemical operatins into. Because this, we need to understand how we can manipute them to solve this.

#****Vetor******
#Somar dois duas listas (Como se fossem vetores espaciais)
def vector_add(vet_1, vet_2):
    return( v_i + w_i for v_i, w_i in zip(vet_1,vet_2))


#Somar todos elementos de um vetor espacial.
def vector_acum(vectors):
    result = 0
    for vector in vectors[0:]:
        result = result + vector
    return result

#Vetor vezes constante
def vector_prod(vet, c):
    return (c*a for a in vet)

#Media do vetor
def vector_mean(vet):
    sum = exemple_2(vet)
    return sum/len(vet)

#Produto escalar
def vector_escalar_prod(v,w):
    return( v_i*w_i for v_i,w_i in zip(v,w))

#Produto vetorial
def vector_escalar_mean(v,w):
    a = ((v_i-w_i)**2 for v_i, w_i in zip(v, w))
    b = list(a)
    result = 0
    for c in b:
        result = result + c

    #for b in a[0:]:
    #    result = result + b
    return (math.sqrt(result))

#******Matriz*****

# define o formato de uma matriz
def shape(A):
    num_rows = len(A)
    num_cols = len(A[0])
    return num_rows, num_cols


def get_row(A,i):
    return A[i]

def get_col(A,j):
    return ( A_i[j] for A_i in A )

def make_matrix(num_rows, num_cols, fn_entry):
    return [fn_entry
            for i in range(num_rows)
            for j in range(num_cols)
            ]

def is_diagonal(i,j):
    return 1 if i==j else 0

#*****Estatistica*******

def Counter(vector):
    return len(vector)

num_friends = [100, 49, 41, 40, 25]

friend_counts = num_friends
xs = range(0,5)
ys = [num_friends[x] for x in xs]

plt.bar(xs,ys)
plt.axis([-1,5,0,110])
plt.title('Histograma da Contagem de Amigos')
plt.xlabel("# de Amigos")
plt.ylabel('# de pessoas')
plt.show()


list1 = [0,0,0]
list2 = [3,4,0]

A = [[1,2,3],
     [4,5,6]]

B = list(make_matrix(2,2,is_diagonal))

print(B)

#a = exemple_6(list1, list2)

#print(a)

#Probabilidade

def random_kid():
    return random.choice('boy', 'girl')

    both_girls  = 0
    older_girl  = 0
    either_girl = 0
    random.seed(0)

for _ in range(10000):
    younger = random_kid()
    older   = random_kid()

    if older & younger == 'girl':
        both_girls +=1

    elif older == 'girl':
        older_girl +=1

    elif younger == 'girl':
        either_girl +=1

print( 'both percentage = %d' , both_girl )