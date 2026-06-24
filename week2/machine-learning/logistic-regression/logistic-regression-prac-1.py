import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math

np.random.seed(42)
n = 1000

study_hours     = np.random.uniform(0, 10, n)
sleep_hours     = np.random.uniform(4, 10, n)
attendance      = np.random.uniform(50, 100, n)
previous_gpa   = np.random.uniform(1.5, 4.0, n)
assignments    = np.random.randint(0, 20, n)
stress_level   = np.random.uniform(1, 10, n)
social_media   = np.random.uniform(0, 8, n)

logit = (
    0.9 * study_hours +
    0.6 * sleep_hours +
    0.04 * attendance +
    1.5 * previous_gpa +
    0.2 * assignments -
    0.7 * stress_level -
    0.5 * social_media
)

prob = 1 / (1 + np.exp(-logit))

y = (prob > 0.5).astype(int)

df = pd.DataFrame({
    "study_hours": study_hours,
    "sleep_hours": sleep_hours,
    "attendance": attendance,
    "previous_gpa": previous_gpa,
    "assignments": assignments,
    "stress_level": stress_level,
    "social_media": social_media,
    "pass": y
})

def sigmoid(z):
    return 1 / (1 + math.e**-z)

def logistic_regression(X, y, weights, n, epochs, learning_rate, epsilon):
    loss_total = []
    for _ in range(epochs):
        z = np.dot(X, weights)
        y_pred = sigmoid(z)

        error = y_pred - y
        grad = np.dot(X.T, error) / n

        # Logistic regression loss function
        loss = -np.mean(y * np.log(y_pred + 1e-15) + (1 - y) * np.log(1 - y_pred + 1e-15))

        loss_total.append(loss) 

        weights -= learning_rate * grad
        
        if np.linalg.norm(grad) < epsilon:
            break
    return weights, loss_total
    
def main():
    epochs = 2000
    learning_rate = 0.01
    epsilon_loss = 1e-6
    epsilon_grad = 1e-6

    # Step 1: Extract features and output

    X = df.iloc[:, :df.shape[1]-1]
    y = df["pass"]

    # Step 2: Split into test and train

    train_size = 0.8

    train_edge = int(train_size * X.shape[0])

    X_train = X.iloc[:train_edge].to_numpy()
    X_test = X.iloc[train_edge:].to_numpy()

    y_train = y.iloc[:train_edge].to_numpy()
    y_test = y.iloc[train_edge:].to_numpy()

    # Step 3. Normalize X_train and X_test for each column

    X_train = (X_train - np.min(X_train, axis=0)) / (np.max(X_train, axis=0) - np.min(X_train, axis=0))
    X_test = (X_test - np.min(X_test, axis=0)) / (np.max(X_test, axis=0) - np.min(X_test, axis=0))

    # Step 4. Declare weights and bias

    X_train = np.column_stack((np.ones(X_train.shape[0]), X_train)) # Prepend the bias into X
    weights = np.zeros(X_train.shape[1]) 

    # Step 5. Apply model

    new_weights, total_loss = logistic_regression(X_train, y_train, weights, len(y_train), 
        epochs, learning_rate, epsilon_grad)
    
    # Step 6. Results

    X_test = np.column_stack((np.ones(X_test.shape[0]), X_test))
    y_test_pred = sigmoid(np.dot(X_test, new_weights))
    
    plt.title("Total Loss Over Epochs")
    plt.plot(total_loss)
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.show()

    plt.title("Predicted vs Actual")
    plt.plot(y_test)
    plt.plot(y_test_pred, color="orange")
    plt.show()

    # You will see all predicted classes are 1 (i.e. 'pass') since the predicted y's are above the threshold
    # of 0.5

if __name__ == "__main__":
    main()