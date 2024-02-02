#!/usr/bin/python3


def square_matrix_simple(matrix=None):
    if matrix is None:
        matrix = []

    # Create a new matrix to store squared values
    squared_matrix = []

    # Iterate through rows in the original matrix
    for row in range(len(matrix)):
        squared_row = []

        # Iterate through elements in the current row
        for element in range(len(matrix[row])):
            square = matrix[row][element] ** 2
            squared_row.append(square)

        # Append the squared row to the new matrix
        squared_matrix.append(squared_row)

    return squared_matrix
