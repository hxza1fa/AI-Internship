import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def mse_loss(y_true, y_pred):
    return 0.5 * (y_true - y_pred) ** 2

def training_loop(X, y, w, b, epochs, learning_rate):
    for _ in range(epochs):
        total_loss = 0.0

        for idx, x in enumerate(X):
            z1 = np.dot(x, w[0]) + b[0]
            a1 = sigmoid(z1)

            z2 = np.dot(a1, w[1]) + b[1]
            y_hat = sigmoid(z2)

            loss = mse_loss(y[idx], y_hat)
            total_loss += loss

            # Output layer
            delta2 = (y_hat - y[idx]) * y_hat * (1 - y_hat)

            dW2 = delta2 * a1
            db2 = delta2

            # Hidden layer
            delta1 = (delta2 * w[1]) * a1 * (1 - a1)

            dW1 = np.outer(x, delta1)
            db1 = delta1

            w[1] -= learning_rate * dW2
            b[1] -= learning_rate * db2

            w[0] -= learning_rate * dW1
            b[0] -= learning_rate * db1

        print(f"Epoch {_ + 1}: Loss = {total_loss:.6f}")

    return w, b

def main():
    X = np.array([
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ])

    y = np.array([0, 1, 1, 0])

    weights = [np.random.rand(2, 2), np.random.rand(2)]
    biases = [np.random.rand(2), np.random.rand()]

    nw, nb = training_loop(X, y, weights, biases, epochs=2000, learning_rate=0.5)

    print("\nPredictions:")
    for x, target in zip(X, y):
        z1 = np.dot(x, nw[0]) + nb[0]
        a1 = sigmoid(z1)

        z2 = np.dot(a1, nw[1]) + nb[1]
        y_hat = sigmoid(z2)

        prediction = int(y_hat >= 0.5)

        print(f"Input: {x}, Target: {target}, Output: {y_hat:.4f}, Prediction: {prediction}")

if __name__ == '__main__':
    main()
