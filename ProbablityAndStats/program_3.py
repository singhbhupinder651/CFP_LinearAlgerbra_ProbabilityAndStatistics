"""
    @Author: Bhupinder Singh
    @Date: 01-01-2023
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 01-01-2023
    @Title: Write a program to find the probability of drawing an ace after drawing an ace on the first draw
"""

import sys

from data_log import get_logger

lg = get_logger(name="(program_3)", file_name="data_log.log")


class ProbabilityComputation:

    def find_probablity_cards(self):
        """
        Description:
            This function is used to find the probability of drawing an ace after drawing an ace on the first draw
        Parameter:
            None 
        Return:
            Returns None
        """
        try:
            # Dependent event
            ace = 4
            ace_card_after_drawing = 3
            deck_of_cards = 52
            deck_of_card_after_drawing_ace = deck_of_cards - 1
            # multiplication rule
            probablity = (ace/deck_of_cards) * \
                (ace_card_after_drawing / deck_of_card_after_drawing_ace)
            lg.info(
                f'The probability of drawing an ace after drawing a ace on the first draw: {probablity}')

        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == "__main__":
    stats_obj = ProbabilityComputation()
    stats_obj.find_probablity_cards()
