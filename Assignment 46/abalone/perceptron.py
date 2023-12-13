import numpy as np
import matplotlib.pyplot as plt

losses = []
fig, (ax1 , ax2)=plt.subplots(1,2)

class Perceptron:
    def __init__(self, learning_rate_w, learning_rate_b):
        self.w = np.random.rand(1, 1)
        self.b = np.random.rand(1, 1)
        self.learning_rate_w = learning_rate_w
        self.learning_rate_b = learning_rate_b

    def fit(self, X_train, Y_train):      

        self.X_train = X_train
        self.Y_train = Y_train
                    
        for j in range(20):
            for i in range(self.X_train.shape[0]):
                # time.sleep(0.5)
                x = self.X_train[i]
                y = self.Y_train[i]
                y_pred = x * self.w + self.b
                error = y - y_pred

                # SGD update
                self.w = self.w + (error * x * self.learning_rate_w)
                self.b = self.b + (error * self.learning_rate_b)
                # print(w)

                # calculate loss MAE
                loss = np.mean(np.abs(error))
                losses.append(loss)

                Y_pred = self.X_train * self.w + self.b
                ax1.clear()
                ax1.scatter(self.X_train, self.Y_train, color="blue")
                ax1.plot(self.X_train, Y_pred, color="red")

                ax2.clear()
                ax2.plot(losses)
                plt.pause(0.01)
               
    def predict(self,X):
         for j in range(20):
            for i in range(X.shape[0]):
                Y_pred = X * self.w + self.b
                return Y_pred

    def evaluate(self,X_test):
        Y_pred = self.predict(X_test)
       
        return Y_pred