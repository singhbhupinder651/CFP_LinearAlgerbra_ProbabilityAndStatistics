"""
    @Author: Bhupinder Singh
    @Date: 01-01-2023
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 01-01-2023
    @Title: A radar unit is used to measure speeds of cars on a motorway. The speeds are normally 
            distributed with a mean of 90 km/hr and a standard deviation of 10 km/hr. 
            Write a program to find the probability that a car picked at random is travelling 
            at more than 100 km/hr?
"""

import sys

from data_log import get_logger

lg = get_logger(name="(program_11)", file_name="data_log.log")


class Statistics:
    def __init__(self, my_dict: dict):
        self.mean_value = my_dict.get('mean_value')
        self.sd = my_dict.get('sd')
        self.x = my_dict.get('x')

    def find_z_score(self):
        """
        Description:
            This function is used to find the z score value
        Parameter:
            None
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
    mean_value = 90
    sd = 10
    x = 100
    my_dict = {'mean_value': mean_value, 'sd': sd, 'x': x}
    stats_obj = Statistics(my_dict)
    z_score = stats_obj.find_z_score()
    lg.info(f'Z score of P(x > 100): {z_score}')
    lg.info(f'the probability that a car picked at random is travelling at more than 100 km/hr: (1-0.8413) = 0.1587 ')
