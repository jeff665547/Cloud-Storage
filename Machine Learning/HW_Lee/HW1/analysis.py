import os
import pandas as pd
import numpy as np
from sklearn import linear_model

os.chdir("C:/Users/jeff/Desktop/Learning/Machine Learning/HW_Lee/HW1")

train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

data = train

data = data.rename(columns = {'日期': 'date', 
                              '測站': 'station',
                              '測項': 'terms'})

data = data.drop(['station'], axis = 1)

All = data.iloc[0:18,2:]
for i in range(int(data.shape[0]/18)):
    if(i == 0):
        continue
    All = pd.concat([All, data.iloc[(18*(i)):(18*(i+1)),3:].reset_index(drop = True)], 
                    axis = 1, ignore_index = True)

All = All.replace('NR', '0')
All.rename(index = dict(zip([i for i in range(0, 18)], All.iloc[:,0])), inplace = True)
All = All.drop([0], axis = 1).T









reg = linear_model.Ridge(alpha = 0.5)
reg.fit([[0, 0], [0, 0], [1, 1]], [0, .1, 1])

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

# Load the diabetes dataset
diabetes = datasets.load_diabetes()

diabetes_X = diabetes.data[:, np.newaxis, 2]

diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]

diabetes_y_train = diabetes.target[:-20]
diabetes_y_test = diabetes.target[-20:]

regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(diabetes_X_train, diabetes_y_train)

# Make predictions using the testing set
diabetes_y_pred = regr.predict(diabetes_X_test)

