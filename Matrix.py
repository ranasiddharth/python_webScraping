import unittest
# rows, columns = map(int, input().split())
# matrix1 = []
# matrix2 = []
#
# for i in range(rows):
#     entries = list(map(int, input().split()))
#     matrix1.append(entries)
#     if len(entries)!=columns:
#         print("invalid matrix")
#         break
#
# print("\n")
#
# rows2, columns2 = map(int, input().split())
#
# for i in range(rows2):
#     entries = list(map(int, input().split()))
#     matrix2.append(entries)
#     if len(entries)!=columns2:
#         print("invalid matrix")
#         break
#
# print("\n")
class Error(Exception):
    """ Base class for other exceptions """
    pass

class NotList(Error):
    """ Raised when the input passed is not a list """
    pass

class Matrix:

    def __init__(self, List):
        try:
            if type(List) == list:
                self.List = List
            else:
                raise NotList
        except NotList:
            print("List not passed, please pass a nested list")


    def display(self):
        for i in self.List:
            print(i)

    def __add__(self, other):
        if len(self.List) == len(other.List) and len(self.List[0]) == len(other.List[0]):
            temp = Matrix([])
            temp.List = [[0 for i in range(len(self.List[0]))] for j in range(len(self.List))]
            for i in range(len(self.List)):
                for j in range(len(self.List[0])):
                    temp.List[i][j] = self.List[i][j] + other.List[i][j]
            return temp
        else:
            raise Exception("Matrices' order is different, cannot add")

    def __sub__(self, other):
        if len(self.List) == len(other.List) and len(self.List[0]) == len(other.List[0]):
            temp = Matrix([])
            temp.List = [[0 for i in range(len(self.List[0]))] for j in range(len(self.List))]
            for i in range(len(self.List)):
                for j in range(len(self.List[0])):
                    temp.List[i][j] = self.List[i][j] - other.List[i][j]
            return temp
        else:
            raise Exception("Matrices' order is different, cannot subtract")

    def __mul__(self, other):
        if len(self.List[0]) == len(other.List):
            result = Matrix([])
            result.List = [[0 for i in range(len(other.List[0]))] for j in range(len(self.List))]
            for i in range(len(self.List)):
                for j in range(len(other.List[0])):
                    for k in range(len(other.List)):
                        result.List[i][j] += self.List[i][k] * other.List[k][j]
            return result
        else:
            raise Exception("columns in self not same as rows in other, cannot multiply")

    def __pow__(self, power, modulo=None):
        if len(self.List) == len(self.List[0]):
            temp = Matrix([])
            temp.List = self.List
            for i in range(power-1):
                temp = temp * self
            return temp
        else:
            raise Exception("Not a square matrix, cannot exponentiate")

    def getMatrixDeterminant(self, m):
        if len(self.List) == len(self.List[0]):
            if len(m) == 2:
                return m[0][0] * m[1][1] - m[0][1] * m[1][0]
            determinant = 0
            for c in range(len(m)):
                metric = [row[:c] + row[c + 1:] for row in (m[:0] + m[1:])]
                obj = Matrix(metric)
                determinant += ((-1) ** c) * m[0][c] * obj.getMatrixDeterminant(metric)
            return determinant
        else:
            raise Exception("Not a square matrix, cannot find determinant")


# Matrix1 = Matrix(matrix1)
# Matrix2 = Matrix(matrix2)

# MatrixSum = Matrix1 + Matrix2
# MatrixSum.display()
#
# MatrixDiff = Matrix1 - Matrix2
# MatrixDiff.display()

# MatrixProduct = Matrix1 * Matrix2
# MatrixProduct.display()

# exponent = int(input())
# MatrixPow = Matrix1 ** exponent
# MatrixPow.display()

# print(Matrix1.getMatrixDeterminant(matrix1))

class Test(unittest.TestCase):

    def setUp(self):
        self.Matrix1 = Matrix([[1, 3, 5], [2, 16, 7], [3, 8, 10]])
        self.Matrix2 = Matrix([[7, 4, 3], [5, 7, 1], [1, 1, 1]])
        self.expo = 2

    def tearDown(self):
        print("\n")

    def test_add(self):
        MatrixSum = self.Matrix1 + self.Matrix2
        output = Matrix([[8, 7, 8], [7, 23, 8], [4, 9, 11]])
        self.assertEqual(MatrixSum.display(), output.display())

    def test_sub(self):
        MatrixDiff = self.Matrix1 - self.Matrix2
        output = Matrix([[-6, -1, 2], [-3, 9, 6], [2, 7, 9]])
        self.assertEqual(MatrixDiff.display(), output.display())

    def test_multiply(self):
        MatrixMul = self.Matrix1 * self.Matrix2
        output = Matrix([[27, 30, 11], [101, 127, 29], [71, 78, 27]])
        self.assertEqual(MatrixMul.display(), output.display())

    def test_exponent(self):
        MatrixExpo = self.Matrix1 ** self.expo
        output = Matrix([[22, 91, 76], [55, 318, 192], [49, 217, 171]])
        self.assertEqual(MatrixExpo.display(), output.display())

    def test_det(self):
        MatrixDet = Matrix([[1, 3, 5], [2, 16, 7], [3, 8, 10]])
        det = MatrixDet.getMatrixDeterminant([[1, 3, 5], [2, 16, 7], [3, 8, 10]])
        output = -53
        self.assertEqual(det, output)

if __name__ == "__main__":
    unittest.main()