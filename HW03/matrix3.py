import numpy as np


class ArithmeticMixin:
    def __add__(self, other):
        return self.__class__(np.add(self.data, other.data).tolist())

    def __sub__(self, other):
        return self.__class__(np.subtract(self.data, other.data).tolist())

    def __mul__(self, other):
        return self.__class__(np.multiply(self.data, other.data).tolist())

    def __matmul__(self, other):
        return self.__class__(np.matmul(self.data, other.data).tolist())


class FileAccessMixin:
    def write_to_file(self, filename):
        with open(filename, "w") as f:
            f.write(self.__str__())


class StringRepresentationMixin:
    def __str__(self):
        return "\n".join(" ".join(map(str, row)) for row in self.data)


class GettersAndSettersMixin:
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value


class HashMixin:
    # Берем сумму элементов первой строки.
    def hash(self):
        return int(sum(self.data[0]))


class Matrix(
    ArithmeticMixin,
    FileAccessMixin,
    StringRepresentationMixin,
    GettersAndSettersMixin,
    HashMixin,
):
    def __init__(self, data):
        self.data = data


np.random.seed(0)
first_matrix_list = [
    [0, 6, 4, 2, 4, 6, 3, 3, 7, 8],
    [5, 0, 8, 5, 4, 7, 4, 1, 3, 3],
    [9, 2, 5, 2, 3, 5, 7, 2, 7, 1],
    [6, 5, 0, 0, 3, 1, 9, 9, 6, 6],
    [7, 8, 8, 7, 0, 8, 6, 8, 9, 8],
    [3, 6, 1, 7, 4, 9, 2, 0, 8, 2],
    [7, 8, 4, 4, 1, 7, 6, 9, 4, 1],
    [5, 9, 7, 1, 3, 5, 7, 3, 6, 6],
    [7, 9, 1, 9, 6, 0, 3, 8, 4, 1],
    [4, 5, 0, 3, 1, 4, 4, 4, 0, 0],
]
second_matrix_list = [
    [0, 6, 4, 2, 4, 6, 3, 3, 7, 8],
    [5, 0, 8, 5, 4, 7, 4, 1, 3, 3],
    [6, 5, 0, 0, 3, 1, 9, 9, 6, 6],
    [6, 5, 0, 0, 3, 1, 9, 9, 6, 6],
    [7, 8, 8, 7, 0, 8, 6, 8, 9, 8],
    [3, 6, 1, 7, 4, 9, 2, 0, 8, 2],
    [7, 8, 4, 4, 1, 7, 6, 9, 4, 1],
    [5, 9, 7, 1, 3, 5, 7, 3, 6, 6],
    [6, 5, 0, 0, 3, 1, 9, 9, 6, 6],
    [4, 5, 0, 3, 1, 4, 4, 4, 0, 0],
]

A = Matrix(first_matrix_list)
B = Matrix(np.random.randint(0, 10, (10, 10)).tolist())
C = Matrix(second_matrix_list)
D = B
AB = A @ B
CD = C @ D

A.write_to_file("A.txt")
B.write_to_file("B.txt")
C.write_to_file("C.txt")
D.write_to_file("D.txt")
AB.write_to_file("AB.txt")
CD.write_to_file("CD.txt")

with open("hash.txt", "w") as f:
    f.write(f"Hash of AB: {AB.hash()}\n")
    f.write(f"Hash of CD: {CD.hash()}")
