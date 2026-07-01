import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

np.random.seed(42)
n = 1000

study_hours = np.random.uniform(0, 10, n)
attendance = np.random.uniform(50, 100, n)
sleep_hours = np.random.uniform(4, 10, n)
stress_level = np.random.uniform(1, 10, n)

score = (
    2.5 * study_hours +
    0.15 * attendance +
    1.0 * sleep_hours -
    1.8 * stress_level +
    np.random.normal(0, 2, n)  # noise
)

y = (score > 15).astype(int)

df = pd.DataFrame({
    "study_hours": study_hours,
    "attendance": attendance,
    "sleep_hours": sleep_hours,
    "stress_level": stress_level,
    "pass": y
})

def main():

    X = df.iloc[:, :-1].to_numpy()
    y = df.iloc[:, -1].to_numpy()

    train_size = 0.8
    validation_size = 0.0
    test_size = 0.2

    train_bounds = int(train_size * X.shape[0])
    validation_bounds = train_bounds + int(validation_size * X.shape[0])

    X_train = X[:train_bounds]
    y_train = y[:train_bounds]

    X_val = X[train_bounds:validation_bounds]
    y_val = y[train_bounds:validation_bounds]

    X_test = X[validation_bounds:]
    y_test = y[validation_bounds:]

    svc_model = SVC(kernel='linear')
    
    svc_model.fit(X_train, y_train)
    y_pred = svc_model.predict(X_test)

    print(f"Accuracy Score: {accuracy_score(y_test, y_pred)}\n")

    plt.title("Predictions vs Actual")
    plt.plot(y_test, color="skyblue")
    plt.plot(y_pred, color="orange")
    plt.show()

if __name__ == "__main__":
    main()