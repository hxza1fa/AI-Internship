import pandas as pd
import numpy as np

def highest_revenue_product(df: pd.DataFrame) -> str:
    df["Revenue"] = df["Quantity"] * df["Price"]
    return df["Product"].iloc[np.argmax(df["Revenue"])]

def solution(df: pd.DataFrame) -> str:
    df["Revenue"] = df["Quantity"] * df["Price"]
    return df["Product"].iloc[df["Revenue"].idxmax()]


def main():
    df = pd.DataFrame({
        "Product": ["Xbox", "Playstation", "Laptop", "Dining Table"],
        "Quantity": [2, 4, 5, 2],
        "Price": [400, 450, 200, 175]
        })
    
    print(df)
    print(f"\nHighest revenue product: {solution(df)}")

if __name__ == "__main__":
    main()
