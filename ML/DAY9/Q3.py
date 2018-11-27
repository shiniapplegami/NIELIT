from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data=pd.read_csv("Immunotherapy.csv")

X=data.iloc[:,:-1].values
y=data.iloc[:,-1].values

#Splitting the data

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)

#Scaling the data

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
train=sc.fit_transform(X_train)
test=sc.transform(X_test)

#Using KNN

from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=3)
knn.fit(train,y_train)
y_pred=knn.predict(test)
print(y_pred)

#Accuracy_matrix

from sklearn.metrics import accuracy_score,confusion_matrix
print(accuracy_score(y_pred,y_test))
