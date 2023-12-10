from pprint import pformat

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


class Matrix(
    ArithmeticMixin, FileAccessMixin, StringRepresentationMixin, GettersAndSettersMixin
):
    def __init__(self, data):
        self.data = data


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
