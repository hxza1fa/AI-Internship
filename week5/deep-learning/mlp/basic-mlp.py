import pandas as pd
import numpy as np
import math
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sys import argv

def relu(x):
    return np.maximum(0, x)
    
def main(argv):
    if len(argv) != 3:
        print("ERROR: Please provide the number of hidden layers and the number of nodes in each layer")
        exit(1)
    try:
        n_layers = int(argv[1])
    except (ValueError, TypeError):
        print("The number of hidden layers provided must be of data type 'int'")
        exit(1)
    try:
        n_nodes = int(argv[2])
    except (ValueError, TypeError):
        print("The number of nodes per layer provided must be of data type 'int'")
        exit(1)
    
    bc = load_breast_cancer()

    X = bc.data
    y = bc.target

    num_features = X.shape[1]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    layers = []
    bias = [np.random.rand(n_nodes) for _ in range(n_layers)]

    nf = num_features
    for h in range(n_layers):
        layer = np.random.rand(nf, n_nodes)
        nf = n_nodes
        layers.append(layer)

    print(f"~LAYERS~\n{layers}")

    O = X_train
    for idx, layer in enumerate(layers):
        O = O @ layer + bias[idx]
        O = relu(O)

    # Apply to one more layer to get output
    
    weights = np.random.rand(n_nodes, 1)
    bias = np.random.rand(1)

    O = O @ weights + bias
    O = relu(O)

    print(f"Final Value: {O}")

if __name__ == '__main__':
    main(argv=argv)