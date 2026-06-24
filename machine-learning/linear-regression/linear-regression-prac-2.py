import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
n = 1000

study_hours     = np.random.uniform(1, 10, n)
sleep_hours     = np.random.uniform(4, 9, n)
attendance_pct  = np.random.uniform(50, 100, n)
prev_gpa        = np.random.uniform(1.5, 4.0, n)
assignments_done = np.random.randint(0, 20, n)
stress_level    = np.random.uniform(1, 10, n)
internet_hours  = np.random.uniform(0, 8, n)
part_time_hours = np.random.uniform(0, 20, n)

noise = np.random.normal(0, 5, n)

final_score = (
    6.5  * study_hours
  + 2.1  * sleep_hours
  + 0.4  * attendance_pct
  + 8.0  * prev_gpa
  - 1.2  * stress_level
  - 0.5  * internet_hours
  - 0.3  * part_time_hours
  + 1.1  * assignments_done
  + noise
)

final_score = np.clip(final_score, 0, 100)

df = pd.DataFrame({
    'study_hours':      study_hours,
    'sleep_hours':      sleep_hours,
    'attendance_pct':   attendance_pct,
    'prev_gpa':         prev_gpa,
    'assignments_done': assignments_done,
    'stress_level':     stress_level,
    'internet_hours':   internet_hours,
    'part_time_hours':  part_time_hours,
    'final_score':      final_score
})

def gradient_descent(X, y, w, epochs, n, learning_rate):
    total_loss = []

    for _ in range(epochs):
        err = np.dot(X, w) - y
        mse = np.sum(err**2) / n

        total_loss.append(mse)

        gradient = np.dot(X.T, err) / n
        w -= learning_rate * gradient
    return w, total_loss

def main():
    epochs = 1000
    learning_rate = 0.01

    X_features = [feature for feature in df.columns if feature != 'final_score']
    X = df[X_features]
    y = df['final_score']

    X = (X - np.min(X, axis=0)) / (np.max(X, axis=0) - np.min(X, axis=0))
    y = (y - np.min(y)) / (np.max(y) - np.min(y))

    X = np.column_stack((np.ones(X.shape[0]), X))
    w = np.zeros(X.shape[1])

    n = len(y)

    new_w, total_loss = gradient_descent(X, y, w, epochs, n, learning_rate)

    print(f"New weights: {new_w}\n")

    plt.title("Total Loss Over Iterations")
    plt.xlabel("Iteration")
    plt.ylabel("Total Loss")
    plt.plot(total_loss, color="red")
    plt.show()

if __name__ == "__main__":
    main()