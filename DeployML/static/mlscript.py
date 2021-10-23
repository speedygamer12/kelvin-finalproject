import numpy as np
import pandas as pd
import sklearn
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split

dataset = pd.read_excel('.\Training Data set.xlsx')

target = dataset.iloc[:,1]
dataset.drop(["DATE", "Time to next failure readings", "S/N"], axis = 1, inplace = True)

scalar = StandardScaler()
dataset = scalar.fit_transform(dataset)

model = SVR(C = 24, epsilon=0.03, gamma=0.042, kernel = "rbf")
model.fit(dataset, target)

import pickle
modelname = "model.sav"
pickle.dump(model, open(modelname, 'wb'))

scalarname = "scalar.sav"
pickle.dump(scalar, open(scalarname, 'wb'))


