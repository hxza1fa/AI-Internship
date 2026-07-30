import numpy as np
import pandas as pd
import random as rd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import sys

def relu(x):
    return np.maximum(0, x)

def forward_prop(model, data):
    res = data
    outputs = []
    for m in model:
        res = np.dot(res, m[0]) + m[1]
        res = relu(res)
        outputs.append(res)
    return  res, outputs

def train_model(model, data, target, epochs, learning_rate):
    new_model = []
    for _ in range(epochs):
        # TO DO: Stochastically loop thru the dataset 
        for sample in range(data.shape[0]):
            # TO DO: Predict the value of the sample
            pred, outputs = forward_prop(model, data[sample])
            
            for idx, layer in enumerate(reversed(model)):
                w, b = layer

                model_size = len(model)
                curr_idx = model_size - idx - 1

                grad_w = outputs[curr_idx] * (target[sample] - pred)
                w = w - learning_rate * grad_w

                grad_b = 1 * (target[sample] - pred)
                b = b - learning_rate * grad_b
                
    return new_model

    
def main(argv):
    if len(argv) != 3:
        print("Please provide the learning rate and number of epochs")
        sys.exit(1)
    try:
        learning_rate = float(argv[1])
    except ValueError:
        print("The learning rate must be a numerical value (i.e. int/float)")
        sys.exit(1)
    try:
        epochs = int(argv[2])
    except ValueError:
        print("The number of epochs must be an integer value")
        sys.exit(1)

    # TO DO: Load dataset

    df = pd.read_pickle("datasets/adult-income.pkl")

    # TO DO: Extract features and target 

    X = df.iloc[:, :-1].values
    y = df.iloc[:, -1].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # TO DO: Standard scale the dataset

    ss = StandardScaler()
    X_train_scaled = ss.fit_transform(X_train)
    X_test_scaled = ss.transform(X_test)

    # TO DO: Build the inital ANN 
    """ 2 Layers: 
        Layer 1: 3 Nodes
        Layer 2: 2 Nodes
    """

    num_inputs = X_train_scaled.shape[1]

    weights = [
        np.random.rand(num_inputs, 3),
        np.random.rand(3, 2),
        np.random.rand(2, 1)
    ]

    biases = [
        np.random.rand(3),
        np.random.rand(2),
        np.random.rand(1)
    ]

    mlp = []

    for w, b, in zip(weights, biases):
        mlp.append((w, b))

    train_model(model=mlp, data=X_train, target=y_train, epochs=epochs, learning_rate=learning_rate)
if __name__ == '__main__':
    main(argv=sys.argv)