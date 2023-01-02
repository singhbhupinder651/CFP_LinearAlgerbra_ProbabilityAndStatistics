"""
    @Author: Bhupinder Singh
    @Date: 29-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 29-12-2022
    @Title: Write a program to perform scalar multiplication of matrix and a number
            X = [[12,7,3],
                [4 ,5,6],
                [7 ,8,9]]
                Y = 9
"""

import sys

from data_log import get_logger

lg = get_logger(name="(program_2)", file_name="data_log.log")


class MatrixComputations:

    def scalar_multiplication(self, matrix, s_num):
        """
        Description:
            This function is used to perform scalar multiplication of matrix and a number
        Parameter:
            matrix: The matrix is 3X3 matrix to be checked
            s_num: The s_num is scaler number to be checked
        Return:
            Returns matrix
        """
        try:
            for i in range(len(matrix)):
                for j in range(len(matrix)):
                    matrix[i][j] = matrix[i][j]*s_num
            return matrix

        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == "__main__":
    matrix = [[12, 7, 3],
              [4, 5, 6],
              [7, 8, 9]]
    s_num = 9
    mat_obj = MatrixComputations()
    lg.info(
        f"After scalar multiplication of matrix: {mat_obj.scalar_multiplication(matrix, s_num)}")
