import pandas as pd
import numpy as np
import math
import random as rd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sys import argv

def relu(x):
    return np.maximum(0, x)

def main(argv):
    if len(argv) != 2:
        print("Please provide the number of layers")
        exit(1)
    try:
        num_layers = int(argv[1])
    except (ValueError, TypeError):
        print("The value for the number of layers provided must be numerical.")
        exit(1)


    bc = load_breast_cancer()
    X = bc.data
    y = bc.target

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Find the number of nodes per layer
    nodes = np.random.randint(1, 10, size=(num_layers))
    print(f"NODES: {nodes}\n")

    # Make the weights for each layer
    num_features = X.shape[1]

    print(f"NUM FEATURES: {num_features}\n")

    weights = [np.random.rand(num_features if _ == 0 else nodes[_ - 1], nodes[_]) for _ in range(num_layers)]
    bias = [np.random.rand(nodes[_]) for _ in range(num_layers)]
    print(f"~WEIGHTS~\n{weights}\n")

    o = X_train
    for idx, w in enumerate(weights):
        o = np.dot(o, w) + bias[idx]
        o = relu(o)

    # Add the final weights and bias to get the final outputs
    # Final weights are based on the shape of the final number of nodes

    fw = np.random.rand(nodes[-1], 1)
    b = np.random.rand(1, )

    o = np.dot(o, fw) + b 
    o = relu(o)

    print(f"~FINAL OUTPUTS - FIRST 5 SAMPLES~\n{o[:5,]}\n")

if __name__ == '__main__':
    main(argv=argv)