# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 08:23:28 2020

@author: mouseless
"""

from sklearn.metrics import confusion_matrix 
from sklearn.model_selection import train_test_split

import librosa
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import os
from PIL import Image
import pathlib
import csv

# Preprocessing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler


data = pd.read_csv('song_features.csv')
#preview the first 5 lines of data
data.head()
# Dropping unneccesary columns
data = data.drop(['filename'],axis=1)


#Encoding the Labels
genre_list = data.iloc[:, -1]
encoder = LabelEncoder()
y = encoder.fit_transform(genre_list)
mapping = dict(zip(encoder.classes_, range(len(encoder.classes_))))

#Scaling the feature columns
scaler = StandardScaler()
X = scaler.fit_transform(np.array(data.iloc[:, :-1], dtype = float))

#make train and test dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

#SVM 
from sklearn.svm import SVC 
svm_model_linear = SVC(kernel = 'linear', C = 1).fit(X_train, y_train) 
svm_predictions = svm_model_linear.predict(X_test)   
# model accuracy for X_test
accuracy = svm_model_linear.score(X_test, y_test) 
# creating a confusion matrix 
cm = confusion_matrix(y_test, svm_predictions)

import pickle
pickle.dump([svm_model_linear,scaler,mapping],open('model_trained.pkl','wb'))
# training a DescisionTreeClassifier 
#from sklearn.tree import DecisionTreeClassifier 
#dtree_model = DecisionTreeClassifier(max_depth = 2).fit(X_train, y_train) 
#dtree_predictions = dtree_model.predict(X_test) 
#accuracy=dtree_model.score(X_test,y_test) 
#print(accuracy)
# creating a confusion matrix 
#cm = confusion_matrix(y_test, dtree_predictions) 

# training a KNN classifier 
from sklearn.neighbors import KNeighborsClassifier 
knn = KNeighborsClassifier(n_neighbors = 7).fit(X_train, y_train)   
# accuracy on X_test 
accuracy = knn.score(X_test, y_test) 
print(accuracy)   
# creating a confusion matrix 
knn_predictions = knn.predict(X_test)  
cm = confusion_matrix(y_test, knn_predictions) 
pickle.dump([knn,scaler,mapping],open('knn_model.pkl','wb'))


#training a random forest classifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import  confusion_matrix
rfc = RandomForestClassifier()
rfc.fit(X_train,y_train)
# predictions
rfc_predict = rfc.predict(X_test)
cm=confusion_matrix(y_test, rfc_predict)
pickle.dump([rfc,scaler,mapping],open('random_forest.pkl','wb'))
