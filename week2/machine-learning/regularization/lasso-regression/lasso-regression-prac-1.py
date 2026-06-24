# Ridge Regression for Continuous Data

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math
import random

np.random.seed(42)

n_samples = 120

study_hours = np.random.uniform(0, 10, n_samples)
attendance = np.random.uniform(50, 100, n_samples)
sleep_hours = np.random.uniform(4, 10, n_samples)

noise_1  = np.random.normal(0, 1, n_samples)
noise_2  = np.random.normal(0, 1, n_samples)
noise_3  = np.random.normal(0, 1, n_samples)
noise_4  = np.random.normal(0, 1, n_samples)
noise_5  = np.random.normal(0, 1, n_samples)
noise_6  = np.random.normal(0, 1, n_samples)
noise_7  = np.random.normal(0, 1, n_samples)
noise_8  = np.random.normal(0, 1, n_samples)
noise_9  = np.random.normal(0, 1, n_samples)
noise_10 = np.random.normal(0, 1, n_samples)
noise_11 = np.random.normal(0, 1, n_samples)
noise_12 = np.random.normal(0, 1, n_samples)

exam_score = (
    5 * study_hours +
    0.6 * attendance +
    3 * sleep_hours +
    np.random.normal(0, 8, n_samples)
)

df = pd.DataFrame({
    "StudyHours": study_hours,
    "Attendance": attendance,
    "SleepHours": sleep_hours,
    "Noise1": noise_1,
    "Noise2": noise_2,
    "Noise3": noise_3,
    "Noise4": noise_4,
    "Noise5": noise_5,
    "Noise6": noise_6,
    "Noise7": noise_7,
    "Noise8": noise_8,
    "Noise9": noise_9,
    "Noise10": noise_10,
    "Noise11": noise_11,
    "Noise12": noise_12,
    "ExamScore": exam_score
})

def linear_regression(X, y, weights, bias, n, lr, epochs, epsilon):
    total_loss = []
    w = weights.copy()
    b = bias
    for _ in range(epochs):
        y_pred = np.dot(X, w) + b
        error = y_pred - y

        grad_w = np.dot(X.T, error) / n
        grad_b = np.mean(error)

        if np.linalg.norm(grad_w) < epsilon and np.linalg.norm(grad_b) < epsilon:
            break

        w -= lr * grad_w
        b -= lr * grad_b

        mse = np.mean(error**2)

        total_loss.append(mse)
    return w, b, total_loss

def lasso_regression(X, y, weights, bias, n, lr, epochs, epsilon, _lambda):
    w = weights.copy()
    b = bias
    for _ in range(epochs):
        y_pred = np.dot(X, w) + b
        error = y_pred - y

        grad_w = np.dot(X.T, error) / n
        grad_b = np.mean(error)

        if np.linalg.norm(grad_w) < epsilon and np.linalg.norm(grad_b) < epsilon:
            break

        w -= lr * (grad_w + np.sign(w) * _lambda)
        b -= lr * grad_b
    return w, b

def main():
    epochs = 5000
    learning_rate = 0.001
    epsilon = 1e-6

    train_size = 50 / n_samples
    validation_size = 35 / n_samples
    test_size = 35 / n_samples

    X = df.iloc[:, :-1].to_numpy()
    y = df.iloc[:, -1].to_numpy()

    train_bounds = int(train_size * X.shape[0])
    validation_bounds = train_bounds + int(validation_size * X.shape[0])

    # Train-test split
    
    X_train = X[:train_bounds]
    X_validation = X[train_bounds:validation_bounds]
    X_test = X[validation_bounds:]

    y_train = y[:train_bounds]
    y_validation = y[train_bounds:validation_bounds]
    y_test = y[validation_bounds:]

    # Initialize weights

    weights = np.zeros(X.shape[1])
    bias = 0

    # Normalize

    X_max = np.max(X_train, axis=0)
    X_min = np.min(X_train, axis=0)

    X_train = (X_train - X_min) / (X_max - X_min)
    X_test = (X_test - X_min) / (X_max - X_min)
    X_validation = (X_validation - X_min) / (X_max - X_min)

    # Apply gradient descent

    new_weights, new_bias, total_loss = linear_regression(X_train, y_train, weights, bias, len(y_train), 
        learning_rate, epochs, epsilon)
    
    print(f"Pre lasso weights: {new_weights}\n")
    print(f"Pre lasso bias: {new_bias}\n")

    plt.title("Total Loss over Epochs")
    plt.xlabel("Epochs")
    plt.ylabel("MSE")
    plt.plot(total_loss, color="red")
    plt.show()

    y_pred_test = np.dot(X_test, new_weights) + new_bias

    plt.title("Actual vs Predicted")
    plt.plot(y_test, color="blue")
    plt.plot(y_pred_test, color="orange")
    plt.show()

    train_mse = np.mean((np.dot(X_train, new_weights) + new_bias - y_train)**2)
    test_mse = np.mean((np.dot(X_test, new_weights)  + new_bias - y_test)**2)
    print(f"Train MSE: {train_mse}\nTest MSE: {test_mse}")

    plt.title("Train vs Test Loss")
    plt.xlabel("Train vs Test")
    plt.ylabel("Loss")
    plt.bar(["Train", "Test"], [train_mse, test_mse], color=["skyblue", "orange"])
    plt.show()

    lambdas = [0, 0.01, 0.1, 1, 10, 100]

    models = [lasso_regression(
        X_train,
        y_train,
        weights,
        bias,
        len(y_train),
        learning_rate,
        epochs,
        epsilon,
        l
    ) for l in lambdas]

    post_lasso_weights = [model[0] for model in models]
    post_lasso_bias = [model[1] for model in models]

    validation_errors = []
    for w, b in zip(post_lasso_weights, post_lasso_bias):
        ve = np.mean((np.dot(X_validation, w) + b - y_validation)**2)
        validation_errors.append(ve)

    min_idx = np.argmin(validation_errors)

    optimal_weights = post_lasso_weights[min_idx]
    optimal_bias = post_lasso_bias[min_idx]
    optimal_lambda = lambdas[min_idx]

    print(f"\nThe optimal weights are: {optimal_weights}\n")
    print(f"The optimal bias is: {optimal_bias}\n") 
    print(f"The optimal lambda value was: {optimal_lambda}\n")   

if __name__ == "__main__":
    main()