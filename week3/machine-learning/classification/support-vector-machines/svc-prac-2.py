import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score

np.random.seed(42)
n = 5000

epochs = 20
learning_rate = 0.001
regularization_strength = 0.01
margin = 1.0
batch_size = 1
shuffle_data = True

study_hours = np.random.uniform(0, 12, n)
attendance = np.random.uniform(40, 100, n)
sleep_hours = np.random.uniform(3, 10, n)
stress_level = np.random.uniform(1, 10, n)

previous_gpa = np.random.uniform(2.0, 4.0, n)
assignments_done = np.random.randint(0, 20, n)
class_participation = np.random.uniform(0, 1, n)

screen_time = np.random.uniform(1, 12, n)
caffeine_intake = np.random.uniform(0, 5, n)

mental_load = (
    stress_level * 0.6 +
    screen_time * 0.3 +
    caffeine_intake * 0.2
)

score = (
    2.2 * study_hours +
    0.12 * attendance +
    1.5 * sleep_hours +
    1.8 * previous_gpa +
    0.3 * assignments_done +
    2.0 * class_participation * 10 -
    2.5 * mental_load +
    np.random.normal(0, 3, n)
)

threshold = np.percentile(score, 55)

y = (score > threshold).astype(int)

df = pd.DataFrame({
    "study_hours": study_hours,
    "attendance": attendance,
    "sleep_hours": sleep_hours,
    "stress_level": stress_level,
    "previous_gpa": previous_gpa,
    "assignments_done": assignments_done,
    "class_participation": class_participation,
    "screen_time": screen_time,
    "caffeine_intake": caffeine_intake,
    "mental_load": mental_load,
    "pass": y
})

def lsvc(weights, bias, X, y, lr, epochs):
    dim = X.shape[0]
    w = weights.copy()
    b = bias
    for i in range(epochs):
        for j in range(dim):
            m = y[j] * (np.dot(w.T, X[j]) + b)
            
            if m < 1:
                w = w + lr * y[j] * X[j]
                b = b + lr * y[j]
    return w, b

def main():
    X = df.iloc[:, :-1].values
    y = df.iloc[:, -1].values

    train_size = 0.8
    test_size = 0.2

    train_bounds = int(train_size * X.shape[0])

    X_train = X[:train_bounds]
    y_train = y[:train_bounds]

    X_test = X[train_bounds:]
    y_test = y[train_bounds:]

    weights = np.zeros(X.shape[1])
    bias = 0

    weight_decay = 0.0001
    tolerance = 1e-4
    random_state = 42
    feature_dim = X.shape[1]

    print_every = 1
    eval_every = 1

    w, b = lsvc(weights, bias, X_train, y_train, learning_rate, epochs)
    
    y_pred = np.dot(X_test, w) + b
    y_pred = [1 if n > 0 else 0 for n in y_pred]

    print(y_pred)

    print(y_pred)

if __name__ == '__main__':
    main()