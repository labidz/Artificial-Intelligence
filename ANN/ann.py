# -*- coding: utf-8 -*-
"""ANN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1D3Tthi0M7kYHpzrhfze7GU7-L2ByOOZV
"""

import pandas as pd
import numpy as np 
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import OneHotEncoder

# load the boston dataset 
dataframe =  pd.read_csv('/content/penguins_size.csv')

# defining feature matrix(X) and response vector(y) 
X = dataframe.iloc[:,:-1] 
y = dataframe.iloc[:,-1:]


#convert categorical to numeric
labelencoder_X=LabelEncoder()
z = X.iloc[:,-1:]
X.iloc[:,-1:] = labelencoder_X.fit_transform(z.values.ravel())

#convert categorical to numeric
labelencoder_X=LabelEncoder()
z = X.iloc[:,0]
X.iloc[:,0] = labelencoder_X.fit_transform(z.values.ravel())


#z score normalization
scaller = StandardScaler()
X = scaller.fit_transform(X)


# encode class values as integers
encoder = LabelEncoder()
encoder.fit(y)
y = encoder.transform(y)


# splitting X and y into training and testing sets  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=1) 

from keras.utils import np_utils
# convert integers to dummy variables (i.e. one hot encoded)
y_train = np_utils.to_categorical(y_train)


#print(X_train.shape)
#print(y_train)
#print(y_test)


# define the keras model
model = Sequential()
model.add(Dense(6, input_dim=6, activation='relu'))
model.add(Dense(4, activation='relu'))
model.add(Dense(3, activation='softmax'))

# compile the keras model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])


# fit the keras model on the dataset
model.fit(X_train, y_train, epochs=100, batch_size=10)

acc = model.evaluate(X_train, y_train)
print("Loss:", acc[0], " Accuracy:", acc[1])

pred = model.predict(X_test)
pred_y = pred.argmax(axis=-1)

#count_class(train_label)

#print(y_test)
#print(pred)

cm = confusion_matrix(y_test, pred_y)
print(cm)

# make class predictions with the model
predictions = (model.predict(X_test) > 0.5).astype(int)
# prdiction for test data
print(predictions)
