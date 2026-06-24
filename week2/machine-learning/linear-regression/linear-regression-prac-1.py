import numpy as np
import pandas as pd
import math

def gradient_descent(X, y, weights, bias, n, epochs, learning_rate):
    w = weights.copy()
    b = bias
    for _ in range(epochs):
        y_pred = np.dot(X, w) + b
        err = y_pred - y

        grad_w = np.dot(X.T, err)
        grad_w /= n
        grad_w *= learning_rate

        w -= grad_w

        grad_b = np.sum(err)
        grad_b /= n
        grad_b *= learning_rate

        b -= grad_b
    return w, b

def main():
    df = pd.DataFrame({
    "size": [1, 2, 3, 4, 5, 6, 7, 8],
    "bedrooms": [1, 1, 2, 2, 3, 3, 4, 4],
    "age": [10, 5, 20, 15, 8, 12, 25, 30],
    "distance": [5, 3, 8, 6, 2, 4, 10, 12],
    "price": [50, 70, 90, 110, 150, 170, 200, 220]
})

    x_features = ["size", "bedrooms"]

    X = df[x_features].to_numpy()
    y = df["price"].to_numpy()

    weights = np.zeros(X.shape[1])
    bias = 0.0

    epochs = 100
    learning_rate = 0.01

    n = len(y)

    print(f"Weights before descent: {weights}\nBias before descent: {bias}\n")

    w, b = gradient_descent(X, y, weights, bias, n, epochs, learning_rate)

    print(f"Weights after descent: {w}\nBias after descent: {b}")
    print(f"RMSE: {math.sqrt(np.sum(((np.dot(X, w) + b) - y)**2) / n)}")

    # Once gradient descent is done, we have the best fit equation
if __name__ == "__main__":
    main()