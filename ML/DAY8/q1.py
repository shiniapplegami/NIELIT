
'''
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import load_boston

data=load_boston()

X=data.data
y=data.target

print(data.feature_names)
print(y)
print(X[:,2:5])

rf=RandomForestRegressor()

rf.fit(X,y)

y_pred=rf.predict(X)

from sklearn.metrics import mean_squared_error

print(mean_squared_error(y_pred,y))

import matplotlib.pyplot as plt

plt.scatter(y_pred,y)

plt.show()
'''

#------------------------------------KNN--------------------------------------------------
'''
from sklearn.neighbors import KNeighborsRegressor
from sklearn.datasets import load_boston

data=load_boston()

X=data.data
y=data.target

print(data.feature_names)
print(y)
print(X[:,2:5])

knn=KNeighborsRegressor()

knn.fit(X,y)

y_pred=knn.predict(X)

from sklearn.metrics import mean_squared_error

print(mean_squared_error(y_pred,y))

import matplotlib.pyplot as plt

plt.scatter(y_pred,y)

plt.show()
'''
#------------------------------------SVR------------------------------------------------------
'''
from sklearn.svm import SVR
from sklearn.datasets import load_boston

data=load_boston()

X=data.data
y=data.target

print(data.feature_names)
print(y)
print(X[:,2:5])

svm=SVR()
svm.fit(X,y)

y_pred=svm.predict(X)

from sklearn.metrics import mean_squared_error

print(mean_squared_error(y_pred,y))

import matplotlib.pyplot as plt

plt.scatter(y,y_pred)

plt.show()

'''
#-----------------------------------RIDGE-------------------------------------------------------------
'''
from sklearn.linear_model import Ridge
from sklearn.datasets import load_boston

data=load_boston()

X=data.data
y=data.target

print(data.feature_names)
print(y)
print(X[:,2:5])

r=Ridge(0.5)

r.fit(X,y)

y_pred=r.predict(X)

from sklearn.metrics import mean_squared_error

print(mean_squared_error(y_pred,y))

import matplotlib.pyplot as plt

plt.scatter(y,y_pred)

plt.show()
'''
#----------------------------------LASSO------------------------------------------------------

from sklearn.linear_model import Lasso
from sklearn.datasets import load_boston

data=load_boston()

X=data.data
y=data.target

print(data.feature_names)
print(y)
print(X[:,2:5])

r=Lasso(0.5)

r.fit(X,y)

y_pred=r.predict(X)

from sklearn.metrics import mean_squared_error

print(mean_squared_error(y_pred,y))

import matplotlib.pyplot as plt

plt.scatter(y,y_pred)

plt.show()
