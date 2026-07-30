import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score
from sys import argv

def main(args):
    if len(args) != 3:
        print("ERORR: Please provide the learning rate and number of epochs")
        exit(1)
    try:
        learning_rate = float(args[1])
    except ValueError:
        print("The learning rate must be a numerical value")
        exit(1)
    try:
        epochs = int(args[2])
    except ValueError:
        print("The number of epochs provided must be an integer value")
        exit(1)
    
    iris = load_iris()
    X = iris.data
    y = iris.target

    mask = y < 2

    X = X[mask]
    y = y[mask]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    p = Perceptron(eta0=learning_rate, max_iter=epochs, random_state=42)
    
    p.fit(X_train, y_train)

    y_pred = p.predict(X_test)
    print(f"Perceptron Accuracy Score: {accuracy_score(y_test, y_pred)}")

if __name__ == '__main__':
    main(args=argv)