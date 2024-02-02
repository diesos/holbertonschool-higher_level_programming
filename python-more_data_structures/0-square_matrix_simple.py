# Content of 0-square_matrix_simple.py

def square_matrix_simple(matrix=None):
    if matrix is None:
        matrix = []
    squared_matrix = []
    for row in range(len(matrix)):
        squared_row = []
        for element in range(len(matrix[row])):
            square = pow(matrix[row][element], 2)
            squared_row.append(square)
        squared_matrix.append(squared_row)
    return squared_matrix
