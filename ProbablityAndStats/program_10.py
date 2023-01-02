"""
    @Author: Bhupinder Singh
    @Date: 01-01-2023
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 01-01-2023
    @Title: X is a normally distributed variable with mean μ = 30 and standard deviation σ = 4.
            Write a program to find
            a. P(x < 40)
            b. P(x > 21)
            c. P(30 < x < 35)
"""

import sys

from data_log import get_logger

lg = get_logger(name="(program_10)", file_name="data_log.log")


class Statistics:
    def __init__(self, my_dict: dict):
        self.mean_value = my_dict.get('mean_value')
        self.sd = my_dict.get('sd')

    def find_z_score(self, x):
        """
        Description:
            This function is used to find the z score value
        Parameter:
            x: The x is normally distributed variable to be checked
        Return:
            Returns z_score
        """
        try:
            # applying Z score formulae:  x-mean / sd
            z_score = (x - self.mean_value) / self.sd
            return z_score

        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == "__main__":
    mean_value = 30
    sd = 4
    x1 = 40
    x2 = 21
    x3 = 35
    my_dict = {'mean_value': mean_value, 'sd': sd}
    stats_obj = Statistics(my_dict)
    z_score1 = stats_obj.find_z_score(x1)
    lg.info(f'Z score of P(x < 40): {z_score1}')
    lg.info(f'P(x < 40) using standard normal distribution: 0.9938')
    z_score2 = stats_obj.find_z_score(x2)
    lg.info(f'Z score of P(x > 21): {z_score2}')
    lg.info(f'P(x < 40) using standard normal distribution: 0.122')
    z_score3 = stats_obj.find_z_score(x3)
    lg.info(f'Z score of P(30 < x < 35): {z_score3}')
    lg.info(f'P(30< x < 35) using standard normal distribution: 0.8944')
