import numpy as np
import math
from numpy.linalg import inv


class LLS:
    def __init__(self):
        pass

    def fit(self, X_train, Y_train):
        # Train
        self.w = inv(X_train.T @ X_train) @ X_train.T @ Y_train
        return self.w

    def predict(self, X_test):
        self.Y_pred = X_test @ self.w
        return self.Y_pred

    def evaluate(self, X_test, Y_test, metric):
        # loss - خطا

        # mean square error (MSE)
        if metric == "mse":
            loss = np.sum((Y_test - self.Y_pred) ** 2) / len(Y_test)
    
        # mean abs error (MAE)
        elif metric == "mae":
            loss = np.sum(np.abs(Y_test - self.Y_pred)) / len(Y_test)
        
        elif metric == "rmse" :
            loss = math.sqrt(np.sum((Y_test - self.Y_pred) ** 2) / len(Y_test))

        return loss