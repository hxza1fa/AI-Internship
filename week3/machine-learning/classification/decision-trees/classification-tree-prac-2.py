import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier 
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import ConfusionMatrixDisplay

np.random.seed(42)

n = 100

study_hours = np.random.choice(
    ["Low", "Medium", "High"],
    size=n,
    p=[0.3, 0.4, 0.3]
)

attendance = np.random.choice(
    ["Low", "Medium", "High"],
    size=n,
    p=[0.3, 0.3, 0.4]
)

sleep = np.random.choice(
    ["Poor", "Good"],
    size=n,
    p=[0.4, 0.6]
)

internet_usage = np.random.choice(
    ["Low", "Medium", "High"],
    size=n,
    p=[0.3, 0.4, 0.3]
)

assignments_submitted = np.random.choice(
    ["No", "Yes"],
    size=n,
    p=[0.3, 0.7]
)

scores = []

for sh, att, sl, iu, assn in zip(
        study_hours,
        attendance,
        sleep,
        internet_usage,
        assignments_submitted):

    score = 0

    if sh == "High":
        score += 3
    elif sh == "Medium":
        score += 2
    else:
        score += 1

    if att == "High":
        score += 3
    elif att == "Medium":
        score += 2
    else:
        score += 1

    if sl == "Good":
        score += 2

    if iu == "Low":
        score += 2
    elif iu == "Medium":
        score += 1

    if assn == "Yes":
        score += 3

    score += np.random.randint(-2, 3)

    scores.append(1 if score >= 8 else 0)

df = pd.DataFrame({
    "study_hours": study_hours,
    "attendance": attendance,
    "sleep": sleep,
    "internet_usage": internet_usage,
    "assignments_submitted": assignments_submitted,
    "pass": scores
})

def main():
    y = df.iloc[:, -1].values
    X = df.iloc[:, :-1].copy()

    # Encode the labels into numerical values 
    for col in X.columns:
        le = LabelEncoder()
        X[col] = le.fit_transform(X[col])
    
    X = X.values

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, train_size=0.8, random_state=42
    )

    dtc = DecisionTreeClassifier()
    dtc.fit(X_train, y_train)
    y_pred = dtc.predict(X_test)

    print(y_pred)
    print(y_test)
    
    ascore = accuracy_score(y_test, y_pred)

    print(f"Model accuracy score: {ascore}\n")

    ConfusionMatrixDisplay.from_estimator(
        dtc,
        X_test,
        y_test
    )
    plt.show()

if __name__ == '__main__':
    main()