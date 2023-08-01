import matplotlib.pyplot as plt
import numpy as np
import math
import xlrd
import pandas as pd
import statistics as st

def percToFloat(a: str):
    a = float(a.strip('%'))
    return a

class chapter8():
    def __init__(self):
        pass

    def exercise1(self):
        serie1 = pd.Series([2, 1, 3, 6,7])
        serie2 = pd.Series([1,-3, 5,-5,8])
        soma   = serie1 + serie2
        sub    = serie1 - serie2
        prod   = serie1 * serie2
        div    = serie1 / serie2
        print(soma)
        print(sub )
        print(prod)
        print(div )


    def exercise2(self):
        a = np.array([2, 5, -4, 8, 7, 1])
        b = pd.Series(a)
        print(b)
        print(type(b))

    def exercise3(self):
        a = pd.Series(["a", "b", "c", "d" , "e"])
        b = []
        for i in range(len(a)):
            b.append(a[i])
        print(a)
        print(b)

    def exercise4(self):
        serie = pd.Series([-1, 40, 0, -100])
        serie = serie.sort_values()
        print(serie)

    def exercise5(self):
        serie1 = pd.Series([-1, 40, 0, -100])
        serie2 = pd.Series(["Comprar", "Vender", "Manter"])
        serie3 = pd.concat([serie2, serie1])
        print(serie3)

    def exercise6(self):
        ativos = pd.DataFrame(
        {
        "Ativos":["USIM5", "PETR4", "VALE3", "BBAS3", "BBDC4", "ITUB4"],
        "Precos":[ 8.2   ,30.9    ,48.3    ,47.8    ,33.9    ,36.5    ]
        })
        print(ativos.head(2))
        print(ativos.tail(2))
        a = ativos["Precos"].max()
        print(ativos[ativos["Precos"]==a])

    def exercise7(self):
        moedas = pd.DataFrame({
            "Moedas"    : ["Dolar", "Peso", "Euro", "Yuan", "Rupia", "Iene"],
            "Cotacao"   : [4.17   , 0.07  , 4.6   , 0.59  , 0.058  , 0.038 ]
                                })
        print("a)")
        print( moedas[moedas["Cotacao"] < 1])
        print("\nb)")
        print( moedas[moedas["Cotacao"] > 4])
        print("\nc)")
        print(moedas [ (moedas["Cotacao"]>0.05) & (moedas["Cotacao"]<0.6) ] )

    def exercise8(self):
         serie = np.random.random(8)

    def exercise9(self):
        serie = pd.DataFrame({
            "Empresa": ["Dow" , "S&P500", "Nasdaq", "HSI", "Ibov"  , "Ftse"],
            "Valor"  : [27.747, 3.099   ,8.501    ,27.065, 107.266 ,7.379  ]
                              })
        #print(serie)
        #print(serie[(serie["Empresa"]=="Nasdaq")  | (serie["Empresa"]=="HSI") | (serie["Empresa"]=="Ibov")])
        print(serie)

    def exercise10(self):
        bov = pd.DataFrame(
        {
            'Nome'         :['COSAN ON NM',  'CEMIG PN N1',   'ENGIE BRASILO'],
            'Valor'        :[57.53        ,  13.01        ,   44.48          ],
            'Oscilacao'    :[-3.06        ,  -0.13        ,   -0.59          ],
            '% Mudanca'    :['-5.05%'     ,  '-0.99%'     ,   '-1.31%'       ],
            'Abrt'         :[60.50        ,  13.09        ,   45.19          ],
            'Max'          :[60.50        ,  13.09        ,   45.27          ],
            'Min'          :[57.15        ,  12.95        ,   44.29          ]
        },
            index          =['EMPO1'      , 'EMPO2'       ,   'EMPO3'        ]
        )
        bov = bov.drop("Abrt", axis = 1)
        print(bov)

    def exercise14(self, a):
        Brasil = pd.DataFrame(
        { 'Ano'         : [1999   , 2000   , 2001   , 2002     , 2003   , 2004   , 2005   , 2006   , 2007   , 2008   ],
          'Cred/Dep'    : [0.74   , 0.71   , 0.64   , 0.69     , 0.60   , 0.59   , 0.59   , 0.62   , 0.72   , 0.82   ],
          'Inflacao'    : ['8.94%', '5.97%', '7.67%',  '12.53%', '9.30%', '7.60%', '5.69%', '3.14%', '4.46%', '5.90%'],
          'Pais'        : ['BRA'  , 'BRA'  , 'BRA'  , 'BRA'    , 'BRA'  , 'BRA'  , 'BRA'  , 'BRA'  , 'BRA'  , 'BRA'  ]
        })

        USA = pd.DataFrame(
            { 'Ano'         : [1999   , 2000   , 2001   , 2002     , 2003   , 2004   , 2005   , 2006   , 2007   , 2008   ],
              'Cred/Dep'    : [0.76   , 0.77   , 0.76   , 0.75     , 0.77   , 0.81   , 0.83   , 0.83   , 0.80   , 0.77   ],
              'Inflacao'    : ['2.20%', '3.36%', '2.84%',  '1.58%' , '2.27%', '2.66%', '3.38%', '3.22%', '2.84%', '3.83%'],
              'Pais'        : ['USA'  , 'USA'  , 'USA'  , 'USA'    , 'USA'  , 'USA'  , 'USA'  , 'USA'  , 'USA'  , 'USA'  ]
            })

        BReUSA = pd.concat([Brasil, USA])
        BReUSA['Inflacao'] = BReUSA['Inflacao'].apply(percToFloat)

        if (a == 'a'):
            BR                 = BReUSA[ (BReUSA['Pais'] == 'BRA') &  (BReUSA['Cred/Dep'] < 0.6)]
            USA                = BReUSA[ (BReUSA['Pais'] == 'USA') &  (BReUSA['Inflacao'] > 3  )]
            #print(BR)
            #print(USA)
            return USA[USA['Ano'].eq(BR['Ano'])]

        elif (a == 'b'):
            USA                = BReUSA[ (BReUSA['Pais'] == 'USA') &  (BReUSA['Cred/Dep'] > 0.75)  &  (BReUSA['Inflacao'] < 2.5)]
            BR                 = BReUSA[  BReUSA['Pais'] =='BRA' ]
            return BR[BR['Ano'].eq(USA['Ano'])]

    def exercise15(self, a):

        table1 = pd.DataFrame(
            {
                'Ano'   :[1962,   1963,   1964    ,1965,  1966,   1967,  1968,   1969,  1970],
                'Barril':[4.01,   4.01,   3.96    ,3.85,  4.01,   3.69,  3.56,   3.56,  4.01],
                'Prod'  :[7.54,   7.61,   7.80    ,8.30,  8.81,   8.66,  8.78,   9.18,  9.03]
            }
        )

        table2 = pd.DataFrame(
            {
                'Ano'       :[1962,   1963,   1964,   1965,  1966,   1967,  1968,   1969,  1970],
                'Dow Jones' :[ 652,    763,    874,    969,   785,    905,   943,    800,   838],
                'Abertura'  :[  56,     23,     48,    150,    17,     70,   170,    120,   150]
            }
        )
        table3 = table1.merge(table2, left_on= 'Ano', right_on='Ano')

        if (a == 'a'):

            print(table3)
            #fig1 = table3.plot.line(x='Ano', color='k')
            #fig1.set_ylim(0,1000)
            #fig2 = fig1.twinx()
            #fig2.set_ylim(0,10)
            #fig2 = table3.plot.line(x='Ano', y='Abertura')
            fig,ax = plt.subplots(figsize=(16,9))
            x = table3['Ano']
            y = table3['Dow Jones']
            z = table3['Abertura']
            ax.plot(x,y, marker = 'o', label = 'plt1', color = 'grey')
            ax.plot(x,z, marker = 'o', label = 'plt1', color = 'black')
            plt.legend()
            ax2 = ax.twinx()
            w = table3['Barril']
            u = table3['Prod']
            ax2.plot(x,u, marker = '.', label = 'plt2', color = 'green')
            ax2.plot(x,w, marker = '.', label = 'plt2', color = 'red')
            plt.legend()
            plt.show()

        if(a == 'b'):
            resp = table3[
                (table3['Dow Jones'] > 750) &
                (table3['Prod']      > 8.9) &
                (table3['Barril']    > 4  )
                         ]
            print(resp['Abertura'].sum(), resp['Ano'].unique())

    def exercise16(self, a):

        table1 = pd.DataFrame(
            {
                'Mes'       :['Agosto','Dezembro','Julho' ,'Novembro', 'Outubro','Setembro'],
                'VolBov'    :['-2.56%','-3.25%'  ,'-0.94%','0.52%'   ,'2.65%'   ,'-5.34%'  ],
                'VolDow'    :['0.12%' ,'-0.20%'  ,'-0.10%','-0.08%'  ,'-0.02%'  ,'-3.48%'  ]
            })

        table2 = pd.DataFrame(
            {
                'Mes'       :['Agosto','Dezembro','Julho' ,'Novembro', 'Outubro','Setembro'],
                'Inflacao'  :['2.90%' ,'1.00%'   ,'1.00%' ,'2.10%'   , '2.30%'  ,'1.00%'   ]
            }
        )

        table3 = table1.merge(table2, left_on='Mes', right_on='Mes')
        table3['VolBov']   = table3['VolBov'].apply(percToFloat)
        table3['VolDow']   = table3['VolDow'].apply(percToFloat)
        table3['Inflacao'] = table3['Inflacao'].apply(percToFloat)

        if(a=='a'):
            fig,ax = plt.subplots(figsize=(9,9))
            x   = table3['Mes']
            y   = table3['VolBov']
            z   = table3['VolDow']
            inf = table3['Inflacao']
            plt.plot(x,y)
            plt.plot(x,z)
            plt.plot(x,inf)
            plt.show()

        elif(a=='b'):
            #Inflacao > 3%
            #VolIbo   > 2%
            resp = table3[ (table3['Inflacao']>3) | (table3['VolBov']>2) ]
            print(resp)

exerc1 = chapter8().exercise1()
#exerc8 = chapter8().exercise16('b')

