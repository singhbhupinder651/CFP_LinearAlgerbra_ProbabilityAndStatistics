"""
    @Author: Bhupinder Singh
    @Date: 29-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 29-12-2022
    @Title: Write a program to perform multiplication of given matrix and vector
            X = [[ 5, 1 ,3],
                [ 1, 1 ,1],
                [ 1, 2 ,1]],
            Y = [1, 2, 3]
"""

import sys

from data_log import get_logger

lg = get_logger(name="(program_3)", file_name="data_log.log")


class MatrixComputations:

    def vector_multipliction(self, matrix, vector):
        """
        Description:
             This function is used to perform multiplication of given matrix and vector
        Parameter:
            matrix: The matrix is 3X3 matrix to be checked
            vector: The vector is 1X3 row matrix to be checked
        Return:
            Returns result
        """
        try:
            result = [0, 0, 0]
            for i in range(len(matrix)):
                for j in range(len(vector)):
                    result[i] += matrix[j][i] * vector[j]
            return result

        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == "__main__":
    matrix = [[5, 1, 3],
              [1, 1, 1],
              [1, 2, 1]]
    vector = [1, 2, 3]
    mat_obj = MatrixComputations()
    lg.info(
        f"After vector multiplication of matrix: {mat_obj.vector_multipliction(matrix, vector)}")
