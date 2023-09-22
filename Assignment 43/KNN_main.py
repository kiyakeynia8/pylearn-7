import numpy as np
from tqdm import tqdm
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

class KNN:
    def __init__(self, k):
        self.k = k

    def fit(self, X, Y):
        self.X_train = X 
        self.Y_train = Y

    def euclidean(self, x1, x2):
        return np.sqrt(np.sum((x1 - x2)**2))
    
    def predict(self, X):
        Y = []
        for x in tqdm(X):
            distances = []
            for i in self.X_train:
                d = self.euclidean(x, i)
                distances.append(d)
            
            nearrest_neighbors = np.argsort(distances)[0:self.k]

            result = np.bincount(self.Y_train[nearrest_neighbors])

            y = np.argmax(result)
            Y.append(y)

        return Y
    
    def evaluate(self, X, Y):
        Y_pred = self.predict(X)
        accuracy = np.sum(Y_pred == Y) / len(Y)

        return accuracy

if __name__ == "__main__":
    iris = load_iris()
    X = iris.data
    Y = iris.target

    print(X)
    
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

    print(X_train, X_test, Y_train, Y_test)

    knn = KNN(3)
    knn.fit(X_train, Y_train)
    accuracy = knn.evaluate(X_test, Y_test)
    print(f"accuracy = {accuracy}")

    knn_sk = KNeighborsClassifier(3)
    knn_sk.fit(X_train, Y_train)
    accuracy2 = knn_sk.score(X_test, Y_test)
    print(f"accuracy = {accuracy2}")