"""
    @Author: Bhupinder Singh
    @Date: 01-01-2023
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 01-01-2023
    @Title: A bank teller serves customers standing in the queue one by one. Suppose that the 
            service time XiXi for customer ii has mean EXi=2 (minutes) and Var(Xi)=1. We assume 
            that service times for different bank customers are independent. Let YY be the total 
            time the bank teller spends serving 50 customers. Write a program to find P(90<Y<110)
"""

import sys

from data_log import get_logger

lg = get_logger(name="(program_7)", file_name="data_log.log")


class Statistics:
    def __init__(self, my_dict: dict):
        self.mean_value = my_dict.get('mean_value')
        self.sd = my_dict.get('sd')
        self.no_of_samples = my_dict.get('no_of_samples')
        self.y1 = my_dict.get('y1')
        self.y2 = my_dict.get('y2')

    def find_probablity(self):
        """
        Description:
            This function is used to find the probability of different events
        Parameter:
            None 
        Return:
            Returns z score: z1 and z2
        """
        try:
            # applying Z score formulae
            z1 = (self.y1 - self.mean_value * self.no_of_samples) / \
                ((self.no_of_samples ** 0.5) * self.sd)
            z2 = (self.y2 - self.mean_value * self.no_of_samples) / \
                ((self.no_of_samples ** 0.5) * self.sd)
            return z1, z2

        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == "__main__":
    mean_value = 2
    sd = 1 ** 0.5
    no_of_samples = 50
    y1 = 90
    y2 = 110
    my_dict = {'mean_value': mean_value, 'sd': sd,
               'no_of_samples': no_of_samples, 'y1': y1, 'y2': y2}
    stats_obj = Statistics(my_dict)
    z1, z2 = stats_obj.find_probablity()
    lg.info(f'Z score 1: {z1}')
    lg.info(f'Z score 2: {z2}')
    normal_distribution_z1 = 0.9207
    normal_distribution_z2 = 0.0793
    result = normal_distribution_z1 - normal_distribution_z2
    lg.info(f'90<Y<110: {result}')
