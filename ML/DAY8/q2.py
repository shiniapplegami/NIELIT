import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data= pd.read_csv("k.txt",delimiter="\s+")
X=data.iloc[:,[0,1]].values
y=data.iloc[:,2].values

from sklearn.ensemble import RandomForestRegressor
#from sklearn.datasets import load_boston

rf=RandomForestRegressor()

rf.fit(X,y)

y_pred=rf.predict(X)

from sklearn.metrics import mean_squared_error

print(mean_squared_error(y_pred,y))

import matplotlib.pyplot as plt

plt.scatter(y_pred,y)

plt.show()


#------------------------------------KNN--------------------------------------------------

from sklearn.neighbors import KNeighborsRegressor

knn=KNeighborsRegressor()

knn.fit(X,y)

y_pred=knn.predict(X)

from sklearn.metrics import mean_squared_error

print(mean_squared_error(y_pred,y))

import matplotlib.pyplot as plt

plt.scatter(y_pred,y)

plt.show()

#------------------------------------SVR------------------------------------------------------

from sklearn.svm import SVR
#from sklearn.datasets import load_boston

svm=SVR()
svm.fit(X,y)

y_pred=svm.predict(X)

from sklearn.metrics import mean_squared_error

print(mean_squared_error(y_pred,y))

import matplotlib.pyplot as plt

plt.scatter(y,y_pred)

plt.show()


#-----------------------------------RIDGE-------------------------------------------------------------

from sklearn.linear_model import Ridge
#from sklearn.datasets import load_boston

r=Ridge(0.5)

r.fit(X,y)

y_pred=r.predict(X)

from sklearn.metrics import mean_squared_error

print(mean_squared_error(y_pred,y))

import matplotlib.pyplot as plt

plt.scatter(y,y_pred)

plt.show()

#----------------------------------LASSO------------------------------------------------------

from sklearn.linear_model import Lasso
#from sklearn.datasets import load_boston

r=Lasso(0.5)

r.fit(X,y)

y_pred=r.predict(X)

from sklearn.metrics import mean_squared_error

print(mean_squared_error(y_pred,y))

import matplotlib.pyplot as plt

plt.scatter(y,y_pred)

plt.show()

#---------------------------------------------------------------------------------------------------

