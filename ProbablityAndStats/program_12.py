"""
    @Author: Bhupinder Singh
    @Date: 01-01-2023
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 01-01-2023
    @Title: Write a program to find the probability of getting a random number from the interval [2, 7]
"""

import sys

from data_log import get_logger

lg = get_logger(name="(program_12)", file_name="data_log.log")


class Statistics:

    def find_probability(self):
        """
        Description:
            This function is used to find the probability of getting a random number from the given interval
        Parameter:
            None
        Return:
            Returns None
        """
        try:
            lower = 2
            upper = 7
            random_num = 1 / (upper - lower)
            lg.info(
                f'the probability of getting a random number from the given interval: {random_num}')

        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == "__main__":
    stats_obj = Statistics()
    stats_obj.find_probability()
