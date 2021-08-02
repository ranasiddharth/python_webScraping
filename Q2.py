rows, columns = map(int, input().split())
matrix1 = []
matrix2 = []

for i in range(rows):
    entries = list(map(int, input().split()))
    matrix1.append(entries)
    if len(entries)!=columns:
        print("invalid matrix")
        break

print("\n")

rows2, columns2 = map(int, input().split())

for i in range(rows2):
    entries = list(map(int, input().split()))
    matrix2.append(entries)
    if len(entries)!=columns2:
        print("invalid matrix")
        break

print("\n")

class Matrix:

    def __init__(self, List):
        self.List = List

    def display(self):
        for i in self.List:
            print(i)

    def __add__(self, other):
        Temp = Matrix([])
        Temp.List = [[0 for i in range(len(self.List[0]))] for j in range(len(self.List))]
        for i in range(len(self.List)):
            for j in range(len(self.List[0])):
                Temp.List[i][j] = self.List[i][j] + other.List[i][j]
        return Temp

    def __sub__(self, other):
        Temp = Matrix([])
        Temp.List = [[0 for i in range(len(self.List[0]))] for j in range(len(self.List))]
        for i in range(len(self.List)):
            for j in range(len(self.List[0])):
                Temp.List[i][j] = self.List[i][j] - other.List[i][j]
        return Temp

    def __mul__(self, other):
        result = Matrix([])
        result.List = [[0 for i in range(len(other.List[0]))] for j in range(len(self.List))]
        for i in range(len(self.List)):
            for j in range(len(other.List[0])):
                for k in range(len(other.List)):
                    result.List[i][j] += self.List[i][k] * other.List[k][j]
        return result

    def __pow__(self, power, modulo=None):
        Temp = Matrix([])
        Temp.List = self.List
        for i in range(power-1):
            Temp = Temp * self
        return Temp

    def getMatrixDeterminant(self, m):
        if len(m) == 2:
            return m[0][0] * m[1][1] - m[0][1] * m[1][0]
        determinant = 0
        for c in range(len(m)):
            metric = [row[:c] + row[c + 1:] for row in (m[:0] + m[1:])]
            obj = Matrix(metric)
            determinant += ((-1) ** c) * m[0][c] * obj.getMatrixDeterminant(metric)
        return determinant


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
