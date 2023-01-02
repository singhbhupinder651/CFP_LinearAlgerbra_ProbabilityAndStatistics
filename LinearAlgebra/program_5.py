"""
    @Author: Bhupinder Singh
    @Date: 29-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 29-12-2022
    @Title: Write a program to find inverse matrix of matrix X
            X = [[12,7,3],
                [4 ,5,6],
                [7 ,8,9]]
"""

import sys

from data_log import get_logger

lg = get_logger(name="(program_5)", file_name="data_log.log")


class MatrixComputations:

    def determinant_func(self, X):
        """
        Description:
             This function is used to find determinant of X matrix
        Parameter:
            X: The X is 3X3 matrix to be checked
        Return:
            Returns determinant of X matrix
        """
        try:
            n = len(X)

            if n == 1:
                return X[0][0]

            result = 0
            for i in range(n):
                x = [[X[a][b] for a in range(1, n)]
                     for b in range(n) if b != i]
                cofactor = (-1) ** i * self.determinant_func(x)
                result += cofactor * X[0][i]
            return result
        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")

    def adjoint_func(self, X):
        """
        Description:
             This function is used to find adjoint function of X matrix
        Parameter:
            X: The X is 3X3 matrix to be checked
        Return:
            Returns adjoint of X matrix
        """
        try:
            n = len(X)

            if n == 1:
                return X

            adjoint_x = [[0 for i in range(n)] for j in range(n)]

            for i in range(n):
                for j in range(n):
                    x = [[X[a][b]
                          for a in range(n)
                          if a != i]
                         for b in range(n) if b != j]
                    cofactor = (-1) ** (i + j) * self.determinant_func(x)
                    adjoint_x[j][i] = cofactor
            return adjoint_x
        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")

    def inverse_func(self, X):
        """
        Description:
             This function is used to find inverse function of X matrix
        Parameter:
            X: The X is 3X3 matrix to be checked
        Return:
            Returns None
        """
        try:
            if self.determinant_func(X) == 0:
                return
            else:
                return self.adjoint_func(X), f'/({self.determinant_func(X)})'
        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == '__main__':
    matrix = [[12, 7, 3],
              [4, 5, 6],
              [7, 8, 9]]
    mat_obj = MatrixComputations()
    lg.info(mat_obj.inverse_func(matrix))
