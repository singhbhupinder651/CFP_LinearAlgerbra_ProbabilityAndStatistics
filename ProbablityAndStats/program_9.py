"""
    @Author: Bhupinder Singh
    @Date: 01-01-2023
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 01-01-2023
    @Title: In a particular pain clinic, 10% of patients are prescribed narcotic pain killers. 
            Overall, five percent of the clinic’s patients are addicted to narcotics 
            (including pain killers and illegal substances). Out of all the people prescribed pain pills,
            8% are addicts. If a patient is an addict, write a program to find the probability that they 
            will be prescribed pain pills?
"""

import sys

from data_log import get_logger

lg = get_logger(name="(program_9)", file_name="data_log.log")


class Statistics:
    def __init__(self, my_dict: dict):
        self.prescribed_pain_killers = my_dict.get('prescribed_pain_killers')
        self.prob_addict = my_dict.get('prob_addict')
        self.addict_based_on_prescribed_pain_killers = my_dict.get(
            'addict_based_on_prescribed_pain_killers')

    def find_probablity(self):
        """
        Description:
            This function is used to find the probability that they will be prescribed pain pills
        Parameter:
            None
        Return:
            Returns prescribed_pain_killers_based_on_addicted_patient
        """
        try:
            # applying bayes theorm
            prescribed_pain_killers_based_on_addicted_patient = (
                prescribed_pain_killers * addict_based_on_prescribed_pain_killers) / prob_addict
            return prescribed_pain_killers_based_on_addicted_patient

        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == "__main__":
    prescribed_pain_killers = 0.1
    prob_addict = 0.05
    addict_based_on_prescribed_pain_killers = 0.08

    my_dict = {'prescribed_pain_killers': prescribed_pain_killers, 'prob_addict': prob_addict,
               'addict_based_on_prescribed_pain_killers': addict_based_on_prescribed_pain_killers}
    stats_obj = Statistics(my_dict)
    result = stats_obj.find_probablity()
    lg.info(
        f'the probability that they will be prescribed pain pills: {result}')
