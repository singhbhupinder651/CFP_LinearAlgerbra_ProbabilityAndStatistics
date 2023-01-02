"""
    @Author: Bhupinder Singh
    @Date: 01-01-2023
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 01-01-2023
    @Title: You toss a fair coin three times write a program to find following:
            a.	What is the probability of three heads, HHH?
            b.	What is the probability that you observe exactly one heads?
            c.	Given that you have observed at least one heads, what is the probability that you observe at least two heads?
"""

import sys

from data_log import get_logger

lg = get_logger(name="(program_4)", file_name="data_log.log")


class ProbabilityComputation:

    def find_probablity_fair_coin(self):
        """
        Description:
            This function is used to find the probability after tossing the fair coin three times
        Parameter:
            None 
        Return:
            Returns None
        """
        try:
            possible_outcomes = ['HHH', 'THH', 'HTH',
                                 'HHT', 'TTH', 'THT', 'HTT', 'TTT']
            outcomes = len(possible_outcomes)
            probablity = self.count_heads(possible_outcomes, outcomes)
            head_outcome = len(probablity)
            probalblity_of_head = head_outcome/outcomes

            lg.info(
                f'The probability of getting heads are : {probalblity_of_head}')

        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")

    def count_heads(self, possible_outcomes, outcomes):
        """
        Description:
            This function is used to find the probability after tossing the fair coin three times
        Parameter:
            possible_outcomes: The possible_outcomes to be checked
            outcomes: The outcomes to be checked
        Return:
            Returns None
        """
        try:
            lg.info('\n1.What is the probability of three heads, HHH? \n2.What is the probability that you observe '
                    'exactly one heads? \n3.Given that you have observed at least one heads, what is the probability '
                    'that you observe at least two heads? ')
            choice = int(input("Enter the choice: "))
            if choice == 1:
                head_probablity = [possible_outcomes[i] for i in range(
                    outcomes) if possible_outcomes[i].count('H') == 3]
            elif choice == 2:
                head_probablity = [possible_outcomes[i] for i in range(
                    outcomes) if possible_outcomes[i].count('H') == 1]
            elif choice == 3:
                head_probablity = [possible_outcomes[i] for i in range(
                    outcomes) if possible_outcomes[i].count('H') >= 2]
            else:
                lg.info('Enter the valid input: ')

            return head_probablity

        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == "__main__":
    stats_obj = ProbabilityComputation()
    stats_obj.find_probablity_fair_coin()
