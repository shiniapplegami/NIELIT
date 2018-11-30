import pandas as pd
import numpy as np

#----------------------------------------------------------------------------------------------
a2 = np.array(range(1,17)).reshape(4,4)
a2

#----------------------------------------------------------------------------------------------
mask_a3 = np.ma.masked_array(a2,mask=a2%3 == 0)
mask_a3

mask_a3.mask

#----------------------------------------------------------------------------------------------

from pandas import DataFrame as df

dfm3 =df(mask_a3) 
dfm3

#----------------------------------------------------------------------------------------------

from pandas import Series as se

se1 = se(range(5),index=list('abcde'))
se1

#----------------------------------------------------------------------------------------------
se1.reindex(list('edcab'))

x =se1.reindex(list('abcdef'))
x

#----------------------------------------------------------------------------------------------

fx =se1.reindex(list('abcdef'),method='ffill')
fx

bx =se1.reindex(list('abcdfe'),method='bfill')
bx

bx =se1.reindex(list('abcdfe'),method='nearest')
bx
