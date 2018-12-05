import pandas as pd
import numpy as np
from pandas import Series as s
from pandas import DataFrame as f
'''
a1=np.random.randint(10,20,40).reshape(10,4)

f1=f(a1)

f1.columns=list("c1 c2 c3 c4".split())

#------------------------------------------------------------------------------------------------------------------------------------

sort=f1.sort_values(['c1','c2'], ascending=(True,False))

print(sort)

#------------------------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------------------

import numpy as np
import pandas as pd
from pandas import DataFrame as f
global d

d={'Items':['a','b','c','d','e'],\
           'Places':['HR','TN','MH','DEL','JK'],\
            'Total_Sale':[100,200,300,400,500]}
df=f(d)
print(df)

def Item_Wise():

    print(df)
    p=input('Enter an item name:')

    for i,j in zip(df.index,df['Items']):
        if j==p:
            print('Place wise rank of',p, 'is', df.rank()['Places'][i])

def Place_Wise():

    print(df)
    q=input('Enter a place name:')

    for i,j in zip(df.index,df['Places']):
        if j==q:
            print('Item wise rank of',q, 'is', df.rank()['Items'][i])



while True:
    print("========================================")
    print('Choose option:')
    print('1. Add data')
    print('2. Show Item_Wise Rank')
    print('3. Show Place_Wise Rank')
    print('4. Exit')

    ch=input('Choose a number: ')

    if ch==1:
        itm=input("Enter an Item name: ")
        plc=input("Enter an Place name: ")
        sl=int(input("Enter total sale value: "))


        l1=[itm,plc,sl]
        arr1=np.array(l1).reshape(1,3)
        df1=f(arr1,columns=['Items', 'Places', 'Total_Sale'], index=[len(df)])
        df=df.append(df1)
        print(df)

    if ch==2:
        Item_Wise()
    if ch==3:
        Place_Wise()
    if ch==4:
        break
'''
#------------------------------------------------------------------------------------------------------------------------------------

import pandas as pd
data = pd.read_csv('lsf3',skiprows=1,header=None)
data.head()

#-------------------------------------------------------------------------------------------------------------------------------------



data.sort_values(4)

#------------------------------------------------------------------------------------------------------------------------------------

data.to_csv('lsf5')
