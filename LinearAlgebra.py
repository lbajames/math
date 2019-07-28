from decimal import Decimal
from fractions import Fraction
import numpy as np

class LinearAlgebra(object):

    def swapArray(self, A, i, j):
        temp = np.array(A[i], copy=True)
        A[i] = A[j]
        A[j] = temp

    def elinimation(self, A, i):
        for j in range(i+1, A.shape[0]):
            ratio = float(A[j][i]) / float(A[i][i])
            A[j] = A[j] - A[i] * ratio
        return

    #   高斯消元得到上三角矩阵
    #   参数
    #       A       方阵
    #   返回
    #       A       一个上三角矩阵
    #       None    A为奇艺矩阵
    def gauseElinimation(self, A):
        row = A.shape[0]
        col = A.shape[1]
        for i in range(0, row): 
            #对角点的值
            diagonal_value = A[i][i]  
            #如果为0，则看下面的行有没有不为0的，有就交换
            if (diagonal_value == 0):
                for j in range(i+1, row):
                    back_value = A[j][i]
                    if (back_value != 0):
                        self.swapArray(A, i, j)
            diagonal_value = A[i][i]
            #如果为0，且没有可交换的，则该矩阵为一个奇异矩阵
            if (diagonal_value == 0):
                return None
            #对下面的行进行消元
            self.elinimation(A, i)
        return

if __name__ == '__main__':
    linearAlgebra = LinearAlgebra()
    A = np.random.randint(0, 10, (3, 4))
    A = np.array(A, dtype=np.float)
    print(A)
    linearAlgebra.gauseElinimation(A)
    print(A)

