import pandas as pd

In [3]:

d2 = {'Name':['Jonathan',' Ankeet','Taukir','Mayank'],'R_no':[11,12,13,14],'Marks':[76,87,98,78]}

from pandas import DataFrame as df

f1 = df(d2)

---------------------------------------------------------------------------

from pandas import DataFrame as df
 
f1 = df(d2)

f1



f1['new']=0

f1



from pandas import Series as se

s1 = se(list('abcd'))
s1


fs = df(s1)
fs

import numpy as np


s = np.array(range(20)).reshape((4,5))
print (s,s.shape)


f2m = df(s,index=list('abcd'),columns=list('12345'))
f2m

dict = {'ename':{1:'Ankeet',2:'Jonathan',3:'Taukir'},'eno':{1:11,2:22,3:33},'esal':{1:11000,2:22000,3:33000}}
print dict
edf = df(dict)
print edf

sed = se(['scientist','officer','assisstant'],index=range(1,4),name="designation")
sed.name



edf[sed.name]=sed
edf

s1 = se(range(1,7))
s1.index = list('abcdef')
print s1
s2 = se([11,22,33,44,55,66])
s2.index = list('defxyz')
print s2

