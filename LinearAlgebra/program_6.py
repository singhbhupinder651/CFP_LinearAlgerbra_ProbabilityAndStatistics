"""
    @Author: Bhupinder Singh
    @Date: 29-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 29-12-2022
    @Title: Write a program to find transpose matrix of matrix Y 
            X = [[12,7,3],
                [4 ,5,6],
                [7 ,8,9]]
            Y = [[5,8,1],
                [6,7,3],
                [4,5,9]]
"""

import sys

from data_log import get_logger

lg = get_logger(name="(program_6)", file_name="data_log.log")


class MatrixComputations:

    def transpose_matrix(self, Y):
        """
        Description:
             This function is used to find transpose of matrix
        Parameter:
            Y: The Y is 3X3 size of matrix to be checked
        Return:
            Returns result
        """
        try:
            result = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]

            for i in range(len(Y)):
                for j in range(len(Y[0])):
                    result[i][j] = Y[j][i]
            return result

        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == "__main__":
    Y = [[5, 8, 1],
         [6, 7, 3],
         [4, 5, 9]]
    mat_obj = MatrixComputations()
    lg.info(f"After transposing of matrix: {mat_obj.transpose_matrix(Y)}")
