"""
    @Author: Bhupinder Singh
    @Date: 01-01-2023
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 01-01-2023
    @Title: Write a program to find probability of drawing an ace from pack of cards
"""

import sys

from data_log import get_logger

lg = get_logger(name="(program_1)", file_name="data_log.log")


class ProbabilityComputation:

    def find_probablity_cards(self):
        """
        Description:
            This function is used to find probability of drawing an ace from pack of cards
        Parameter:
            None 
        Return:
            Returns None
        """
        try:
            pack_of_cards = 52
            ace = 4
            probablity = ace/pack_of_cards
            lg.info(
                f'The probability of drwaing an ace from pack of cards: {probablity}')

        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == "__main__":
    stats_obj = ProbabilityComputation()
    stats_obj.find_probablity_cards()
