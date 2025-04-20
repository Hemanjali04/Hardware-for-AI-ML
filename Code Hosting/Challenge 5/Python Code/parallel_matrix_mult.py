# parallel_matrix_mult.py
from multiprocessing import Pool

def multiply_row(args):
    row, B = args
    result_row = []
    for j in range(len(B[0])):
        total = 0
        for k in range(len(B)):
            total += row[k] * B[k][j]
        result_row.append(total)
    return result_row

def matrix_multiply_parallel(A, B):
    with Pool() as pool:
        result = pool.map(multiply_row, [(row, B) for row in A])
    return result

if __name__ == "__main__":
    A = [[1, 2, 3], [4, 5, 6]]
    B = [[7, 8], [9, 10], [11, 12]]
    result = matrix_multiply_parallel(A, B)
    for row in result:
        print(row)
