import numpy as np
from sklearn.model_selection import train_test_split
from perceptron import Perceptron
from sklearn.datasets import make_regression

x, y, coef = make_regression(n_samples=300,
                            n_features=1,
                           n_informative=1,
                          noise=10,
                         coef=True,
                        random_state=40) 

X = np.interp(x, (x.min(), x.max()), (0, 20))
Y = np.interp(y, (y.min(), y.max()), (20000, 150000))


X_train , X_test , Y_train , Y_test = train_test_split(X , Y ,shuffle=True ,  test_size=0.2)
Y_train = Y_train.reshape(-1 , 1)
Y_test = Y_test.reshape( -1, 1)

learning_rate_w = 0.00001  
learning_rate_b = 0.001 
Epoch = 10
Y_test = []
X_test = []

perceptron = Perceptron(learning_rate_w, learning_rate_b, Epoch) 
perceptron.fit(X_train, Y_train)

y_predicted = perceptron.predict(X_test)
y_predicted_train = perceptron.predict(X_train)