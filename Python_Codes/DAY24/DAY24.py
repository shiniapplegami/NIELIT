import pandas as pd
import numpy as np
from pandas import Series as s
from pandas import DataFrame as f

a1=np.random.randint(10,20,40).reshape(10,4)

f1=f(a1)

f1.columns=list("c1 c2 c3 c4".split())

#------------------------------------------------------------------------------------------------------------------------------------

sort=f1.sort_values(['c1','c2'], ascending=(True,False))

print(sort)

#------------------------------------------------------------------------------------------------------------------------------------

def data():
    d={'Items':['a','b','c','d','e'],\
           'Places':['HR','TN','MH','DEL','JK'],\
            'Total_Sale':[100,200,300,400,500]}
    df=f(d)
    print(df)

data()

#-----------------------------------------------------------------------------------------------------------------------------------

