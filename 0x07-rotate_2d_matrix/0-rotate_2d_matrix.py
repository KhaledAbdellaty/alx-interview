#!/usr/bin/python3
"""
A module that transposing the matrix and then reversing
each row to achieve a 90-degree clockwise rotation.
"""


def rotate_2d_matrix(matrix):
    """
    A function that rotate 2D matrix.
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i] = matrix[i][::-1]
