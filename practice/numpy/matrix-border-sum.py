import numpy as np

def main():
    arr = np.array ([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9,10,11,12],
        [13,14,15,16]
    ])

    rows = arr.shape[0]
    cols = arr.shape[1]

    print(f"Rows: {rows}\nCols:{cols}\n")

    edge_sum: int = 0

    edge_sum += np.sum(arr[0])
    edge_sum += np.sum(arr[rows-1])
    edge_sum += np.sum(arr.T[0])
    edge_sum += np.sum(arr.T[rows-1])

    edge_sum -= (arr[0, 0] + arr[0, cols-1] + arr[rows-1, 0] + arr[rows-1, cols-1])
    print(edge_sum)

if __name__ == "__main__":
    main() 
