import pandas as pd
from sklearn.model_selection import train_test_split
from perceptron import Perceptron

losses = []

data = pd.read_csv("abalone/abalone.csv")

X = data["Length"].values
Y = data["Diameter"].values

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, shuffle=True, test_size=0.5)

X_train = X_train.reshape(-1,1)
Y_train = Y_train.reshape(-1,1)
X_test = X_test.reshape(-1,1)
Y_test = Y_test.reshape(-1,1)

perceptron = Perceptron(0.01, 0.1)
perceptron.fit(X_train, Y_train)

perceptron.evaluate(X_test, Y_test)
Y_pred = perceptron.predict(X_test)
Y_pred = Y_pred.reshape(X_train.shape[0], -1)