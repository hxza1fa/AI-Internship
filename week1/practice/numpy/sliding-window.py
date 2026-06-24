import numpy as np

def window_max(arr: np.array, start_pos, k: int) -> int:
    start_x, start_y = start_pos
    window = arr[start_x:start_x+k, start_y:start_y+k]
    
    return np.max(window)

def sliding_window(arr: np.array, k: int) -> int:
    row_number = arr.shape[0]
    col_number = arr.shape[1]
    
    max_val = 0
    
    for i in range(row_number - k + 1):
        for j in range(col_number - k + 1):
            w = window_max(arr, (i, j), k)
            if w > max_val:
                max_val = w

    return max_val

def main():
    arr = np.array ([
        [1, 2, 3, 4], 
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ])

    k = 2

    print(arr,'\n',end='\n')
    print(f"Max from all windows: {sliding_window(arr, k)}")

if __name__ == "__main__":
    main()
