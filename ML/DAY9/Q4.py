import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('banking.csv')

X = data.iloc[:,[0,1,3,5,6,10,11,12,13,15,16,17,18,19]].values
y = data.iloc[:,-1].values

#print(X)


#Using Encoder
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

le = LabelEncoder()
X[:,1] = le.fit_transform(X[:,1])
X[:,2] = le.fit_transform(X[:,2])
X[:,3] = le.fit_transform(X[:,3])
X[:,4] = le.fit_transform(X[:,4])

onehot = OneHotEncoder(categorical_features=[1,2,3,4])
X = onehot.fit_transform(X).toarray()

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
