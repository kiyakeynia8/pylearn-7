import numpy as np

class LLS:
    def __init__(self):
        self.w = None

    def fit(self, X_train, Y_train):
        self.w = np.matmul(np.matmul(np.linalg.inv(np.matmul(X_train.T, X_train)), X_train.T), Y_train)
        return self.w

    def predict(self, X_test):
        return np.matmul(X_test, self.w)