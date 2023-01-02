"""
    @Author: Bhupinder Singh
    @Date: 29-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 29-12-2022
    @Title: Write a python program to add below matrices
            X = [[12,7,3],
                [4 ,5,6],
                [7 ,8,9]]
            Y = [[5,8,1],
                [6,7,3],
                [4,5,9]]
"""

import sys

from data_log import get_logger

lg = get_logger(name="(program_1)", file_name="data_log.log")


class MatrixComputations:

    def add_matrices(self, X, Y):
        """
        Description:
            This function is used to add two matrices
        Parameter:
            X: The X is 3X3 size of matrix to be checked
            Y: The Y is 3X3 size of matrix to be checked
        Return:
            Returns result
        """
        try:
            result = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]

            for i in range(len(X)):
                for j in range(len(X[0])):
                    result[i][j] = X[i][j] + Y[i][j]
            return result

        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == "__main__":
    X = [[12, 7, 3],
         [4, 5, 6],
         [7, 8, 9]]

    Y = [[5, 8, 1],
         [6, 7, 3],
         [4, 5, 9]]

    mat_obj = MatrixComputations()
    lg.info(f"After addition of matrix: {mat_obj.add_matrices(X, Y)}")
