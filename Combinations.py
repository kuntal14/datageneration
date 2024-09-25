from itertools import combinations
import numpy as np

def generate_combinations(arr, n):
    return list(combinations(arr, n))


if __name__ == "__main__":
    array = np.arange(0,8)
    combinations_list = generate_combinations(array,2)
    # print(combinations_list)
    print(int(combinations_list[0][0]))
