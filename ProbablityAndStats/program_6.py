"""
    @Author: Bhupinder Singh
    @Date: 01-01-2023
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 01-01-2023
    @Title: Given the following statistics, write a program to find the probability 
            that a woman has cancer if she has a positive mammogram result?
            a.	One percent of women over 50 have breast cancer.
            b.  Ninety percent of women who have breast cancer test positive on mammograms. 
            c.  Eight percent of women will have false positives
"""

import sys

from data_log import get_logger

lg = get_logger(name="(program_6)", file_name="data_log.log")


class Statistics:

    def find_probablity(self):
        """
        Description:
            This function is used to find the probability that a woman has cancer if she has a positive mammogram result
        Parameter:
            None 
        Return:
            Returns None
        """
        try:
            cancer = 0.01
            no_cancer = 0.99
            cancer_mammograms = 0.9
            no_cancer_mammograms = 0.08

            prob_total_cancer = cancer * cancer_mammograms
            prob_total_mammograms = cancer*no_cancer_mammograms+no_cancer * cancer_mammograms
            # Bayes theorm P(A/B) = P(B/A) x P(A) / P(B)
            probability_mammograms = prob_total_cancer/prob_total_mammograms
            lg.info(
                f'the probability that a woman has cancer if she has a positive mammogram result: {probability_mammograms}')

        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == "__main__":
    stats_obj = Statistics()
    stats_obj.find_probablity()
