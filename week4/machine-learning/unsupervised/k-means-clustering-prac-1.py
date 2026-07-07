import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv("datasets/mall-customers.csv")
    X: pd.DataFrame = df.iloc[:, :-1]

    X.rename(columns={"Annual Income (k$)": "Annual Income"}, inplace=True)
    print(X.head())

if __name__ == '__main__':
    main()