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
        grad_b = np.sum(error) / n

        if np.linalg.norm(grad_w) < epsilon and np.linalg.norm(grad_b) < epsilon:
            break

        w -= lr * grad_w
        b -= lr * grad_b

        loss = np.sum(error**2) / n

        total_loss.append(loss)
    return w, b, total_loss

def ridge_regression(X, y, weights, bias, n, lr, epochs, epsilon, _lambda):
    total_loss = []
    w = weights.copy()
    b = bias
    for _ in range(epochs):
        y_pred = np.dot(X, w) + b
        error = y_pred - y

        grad_w = np.dot(X.T, error) / n
        grad_b = np.mean(error)

        w = w - lr * (grad_w + 2 * w * _lambda)
        b = b - lr * grad_b

        if np.linalg.norm(grad_w) < epsilon and np.linalg.norm(grad_b) < epsilon:
            break

        loss = np.mean(error**2)
        penalty = np.sum(w**2) * _lambda

        total_loss.append(loss + penalty)
    return w, b, total_loss

def main():
    epochs = 5000
    learning_rate = 0.001
    epsilon = 1e-6

    train_size = 60 / n_samples
    validation_size = 30 / n_samples
    test_size = 30 / n_samples

    # Step 1: Extract dataset
    X = df.iloc[:, :df.shape[1] - 1].to_numpy()
    y = df.iloc[:, df.shape[1] -1].to_numpy()

    # Step 2: Split into test, train, and validation

    train_bounds = int(train_size * X.shape[0])
    validation_bounds = int((train_size + validation_size) * X.shape[0])

    X_train = X[:train_bounds]
    X_validation = X[train_bounds:validation_bounds]
    X_test = X[validation_bounds:]

    y_train = y[:train_bounds]
    y_validation = y[train_bounds:validation_bounds]
    y_test = y[validation_bounds:]

    # Step 3: Min-max normalize X

    X_min = np.min(X_train, axis=0)
    X_max = np.max(X_train, axis=0)

    X_train = (X_train - X_min) / (X_max - X_min)
    X_validation = (X_validation - X_min) / (X_max - X_min)
    X_test = (X_test - X_min) / (X_max - X_min)

    # Step 4: Apply gradient descent and analyze test data

    weights = np.zeros(X_train.shape[1])
    bias = 0

    new_weights, new_bias, loss_over_epochs = linear_regression(X_train, y_train, weights, bias, 
        len(y_train), learning_rate, epochs, epsilon)
    
    # Step 5: Analysis

    # --- Loss over epochs ---

    plt.title("Loss over epochs")
    plt.plot(loss_over_epochs, color="red")
    plt.xlabel("Epochs")
    plt.ylabel("Loss")
    plt.show()

    # --- Predicted vs Actual Test --- 

    y_pred_test = np.dot(X_test, new_weights) + new_bias

    plt.title("Predicted vs Actual")
    plt.plot(y_test, color="skyblue")
    plt.plot(y_pred_test, color="orange")
    plt.show()

    # --- Test Overfitting --- 

    labels = ["Train", "Test"]
    
    train_mse = np.mean((np.dot(X_train, new_weights) + new_bias - y_train)**2)
    test_mse = np.mean((np.dot(X_test, new_weights) + new_bias - y_test)**2)

    print(f"Train MSE: {train_mse}\nTest MSE: {test_mse}\n")

    plt.title("Train vs Test Loss")
    plt.bar(labels, [train_mse, test_mse], color=["skyblue", "orange"])
    plt.xlabel("Train vs Test")
    plt.ylabel("Loss")
    plt.show()

    # Step 6: Find the optimal value of lambda

    lambdas = [0, 0.01, 0.1, 1, 10, 100]
    
    # Step 7: Run ridge regression for all lambdas

    models = [
        ridge_regression(
            X_train, y_train,
            weights, bias,
            len(y_train),
            learning_rate,
            epochs,
            epsilon,
            l
        )
        for l in lambdas
    ]

    best_fit_weights = [model[0] for model in models]
    best_fit_bias = [model[1] for model in models]
    
    validation_mses = []
    for w, b in zip(best_fit_weights, best_fit_bias):
        validation_mse = np.mean(
            (np.dot(X_validation, w) + b - y_validation)**2
        )
        validation_mses.append(validation_mse)

    best_idx = np.argmin(validation_mses)
    best_weights = best_fit_weights[best_idx]
    best_bias = best_fit_bias[best_idx]
    best_lambda = lambdas[best_idx]

    print(f"The best value of lambda is: {best_lambda}\n")
    print(f"The optimal weights are: {best_weights}\n")
    print(f"The optimal bias is: {best_bias}\n")

    # Step 8: Conclusion: Was the model overfit?

    print(f"Was the model overfit? {'No' if best_lambda == 0 else 'Yes'}")

if __name__ == "__main__":
    main()