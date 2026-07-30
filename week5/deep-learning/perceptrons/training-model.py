import numpy as np
import pandas as pd
import random as rd
import math
from sys import argv
from sklearn.metrics import root_mean_squared_error as rmse
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

def step_function(x):
    return 1 if x >= 0 else 0

def train_perceptron_step(X: np.ndarray, y: np.ndarray, weights: np.ndarray, lr, epochs):
    # We do stochastic updates for perceptron learning
    # (i.e. we update by the loss of each feature)

    # NOTE: Stopping condition: If one epoch makes no errors

    w = weights.copy()
    for _ in range(epochs):
        errors = 0
        for xi, yi in zip(X, y):
            z = np.dot(xi, w)
            y_pred = step_function(z)
            
            error = yi - y_pred
            errors = errors + 1 if error != 0 else errors
            w = w + lr * error * xi
        if errors == 0:
            break
    return w

def main(args):
    if len(args) != 3:
        print("Please provide the learning rate and epoch number")
        exit(1)
    try:
        learning_rate = float(args[1])
    except ValueError:
        print("Learning rate must be a numerical value")
        exit(1)
    try:
        epochs = int(args[2])
    except ValueError:
        print("Epochs must be an int value")
        exit(1)

    iris = load_iris()
    X = iris.data
    y = iris.target

    # This wasn't binary, so make it so, chap.
    mask = y < 2

    X = X[mask]
    y = y[mask]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    weights = np.zeros(X.shape[1] + 1)
    X_train_mod = np.hstack((X_train, np.ones((X_train.shape[0], 1))))

    res = train_perceptron_step(X_train_mod, y_train, weights, learning_rate, epochs)

    w = res[:-1]
    b = res[-1]

    print(f"Weights: {w}")
    print(f"Bias: {b}")

    y_pred = np.dot(X_test, w) + b
    y_pred = np.array([step_function(x) for x in y_pred])
    
    print(f"RMSE for perceptron: {rmse(y_test, y_pred)}")

if __name__ == '__main__':
    main(args=argv)