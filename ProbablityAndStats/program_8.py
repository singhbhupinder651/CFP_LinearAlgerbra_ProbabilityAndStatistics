"""
    @Author: Bhupinder Singh
    @Date: 01-01-2023
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 01-01-2023
    @Title: In a communication system each data packet consists of 1000 bits. Due to the noise,
    each bit may be received in error with probability 0.1. It is assumed bit errors occur independently.
    Find the probability that there are more than 120 errors in a certain data packet.
"""

import sys

from data_log import get_logger

lg = get_logger(name="(program_8)", file_name="data_log.log")


class Statistics:
    def __init__(self, my_dict: dict):
        self.mean_value = my_dict.get('mean_value')
        self.sd = my_dict.get('sd')
        self.no_of_samples = my_dict.get('no_of_samples')
        self.y1 = my_dict.get('y1')

    def find_probablity(self):
        """
        Description:
            This function is used to find the probability that there are more than 120 errors in a certain data packet
        Parameter:
            None
        Return:
            Returns z_score
        """
        try:
            # applying Z score formulae
            z_score = (self.y1 - self.mean_value * self.no_of_samples) / \
                ((self.no_of_samples ** 0.5) * self.sd)
            return z_score

        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == "__main__":
    # mean_value, p = 0.1       variance = sd^2 =p(1-p)
    mean_value = p = 0.1
    sd = (p * (1-p))**0.5
    no_of_samples = 1000
    y1 = 120
    my_dict = {'mean_value': mean_value, 'sd': sd,
               'no_of_samples': no_of_samples, 'y1': y1}
    stats_obj = Statistics(my_dict)
    z_score = stats_obj.find_probablity()
    lg.info(f'Z score 1: {z_score}')
    normal_distribution_z = 0.9821
    prob = 1 - normal_distribution_z
    lg.info(
        f'the probability that there are more than 120 errors in a certain data packet: {prob}')
