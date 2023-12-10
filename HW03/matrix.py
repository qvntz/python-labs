from pprint import pformat

import numpy as np


class Matrix:
    def __init__(self, data):
        if not all(len(row) == len(data[0]) for row in data):
            raise ValueError("Не все строки матрицы имеют одинаковую длину")
        self.data = data

    def __add__(self, other):
        if self.is_valid_for_addition(other):
            return Matrix(
                [
                    [
                        self.data[i][j] + other.data[i][j]
                        for j in range(len(self.data[0]))
                    ]
                    for i in range(len(self.data))
                ]
            )
        raise ValueError("Матрицы разных размеров, нельзя выполнить сложение")

    def __mul__(self, other):
        return Matrix(
            [
                [self.data[i][j] * other.data[i][j] for j in range(len(self.data[0]))]
                for i in range(len(self.data))
            ]
        )

    def __matmul__(self, other):
        if self.is_valid_for_matmul(other):
            return Matrix(
                [
                    [
                        sum(
                            self.data[i][k] * other.data[k][j]
                            for k in range(len(self.data[0]))
                        )
                        for j in range(len(other.data[0]))
                    ]
                    for i in range(len(self.data))
                ]
            )
        raise ValueError(
            "Матрицы некорректных размеров, нельзя выполнить матричное умножение"
        )

    def is_valid_for_addition(self, other):
        return len(self.data) == len(other.data) and len(self.data[0]) == len(
            other.data[0]
        )

    def is_valid_for_matmul(self, other):
        return len(self.data[0]) == len(other.data)

    def __str__(self):
        return "\n".join([" ".join(map(str, row)) for row in self.data])


np.random.seed(0)
matrix_data = np.random.randint(0, 10, (10, 10))
matrix_data2 = np.random.randint(0, 10, (10, 10))
matrix1 = Matrix(matrix_data.tolist())
matrix2 = Matrix(matrix_data2.tolist())

with open("matrix+.txt", "w") as f:
    f.write("Custom:\n")
    f.write(str(matrix1 + matrix2))
    f.write("\nNumpy:\n")
    f.write(str(pformat(((matrix_data + matrix_data2).tolist()))))
    f.write("\n")

with open("matrix*.txt", "w") as f:
    f.write("Custom:\n")
    f.write(str(matrix1 * matrix2))
    f.write("\nNumpy:\n")
    f.write(str(pformat((matrix_data * matrix_data2).tolist())))
    f.write("\n")

with open("matrix@.txt", "w") as f:
    f.write("Custom:\n")
    f.write(str(matrix1 @ matrix2))
    f.write("\nNumpy:\n")
    f.write(str(pformat((matrix_data @ matrix_data2).tolist())))
