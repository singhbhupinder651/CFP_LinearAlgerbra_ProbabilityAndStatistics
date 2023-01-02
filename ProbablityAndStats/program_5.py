"""
    @Author: Bhupinder Singh
    @Date: 01-01-2023
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 01-01-2023
    @Title: In my town, it's rainy one third of the days. Given that it is rainy, there will be heavy 
            traffic with probability 1/2, and given that it is not rainy, there will be heavy traffic 
            with probability 1/4. If it's rainy and there is heavy traffic, I arrive late for work with 
            probability 1/2. On the other hand, the probability of being late is reduced to 1/8 if it is 
            not rainy and there is no heavy traffic. In other situations (rainy and no traffic, not 
            rainy and traffic) the probability of being late is 0.25. You pick a random day.

            Write a program to find following
            a.	What is the probability that it's not raining and there is heavy traffic and I am not 
            late?
            b.	What is the probability that I am late?
            c.	Given that I arrived late at work, what is the probability that it rained that day?

"""

import sys

from data_log import get_logger

lg = get_logger(name="(program_5)", file_name="data_log.log")


class ProbabilityComputation:

    def create_probability(self):
        """
        Description:
            This function is used to create dictionary of probability with respect to rainy, heavy traffic
            and late condition
        Parameter:
            None
        Return:
            Returns None
        """
        try:
            # Rain and no rain probability
            rainy = 1/3
            no_rainy = 2/3

            # Rain with heavy traffic and rain with no traffic probability
            rainy_traffic = rainy * 1/2
            rainy_no_traffic = rainy * 1/2

            # No rain with heavy traffic and no rain with heavy traffic probability
            no_rainy_traffic = no_rainy * 1/4
            no_rainy_no_traffic = no_rainy * 3/4

            # Rain, traffic with late and rain, heavy traffic with no late probability
            rainy_traffic_late = rainy_traffic * 1/2
            rainy_traffic_no_late = rainy_traffic * 1/2

            # Rain, no traffic with late and rain, no traffic with no late
            rainy_no_traffic_late = rainy_no_traffic * 1/4
            rainy_no_traffic_no_late = rainy_no_traffic * 3/4

            # No rain, traffic with late and no rain traffic no late
            no_rainy_traffic_late = no_rainy_traffic * 1/4
            no_rainy_traffic_no_late = no_rainy_traffic * 3/4

            # No rain, no traffic and late and no rain, no traffic and no late
            no_rainy_no_traffic_late = no_rainy_no_traffic * 1/8
            no_rainy_no_traffic_no_late = no_rainy_no_traffic * 7/8

            my_dict = {'rainy_traffic_late': rainy_traffic_late,
                       'rainy_traffic_no_late': rainy_traffic_no_late,
                       'rainy_no_traffic_late': rainy_no_traffic_late,
                       'rainy_no_traffic_no_late': rainy_no_traffic_no_late,
                       'no_rainy_traffic_late': no_rainy_traffic_late,
                       'no_rainy_traffic_no_late': no_rainy_traffic_no_late,
                       'no_rainy_no_traffic_late': no_rainy_no_traffic_late,
                       'no_rainy_no_traffic_no_late': no_rainy_no_traffic_no_late}
            probablity = self.find_probablity(my_dict)
            lg.info(f'The probablity: {probablity}')

        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")

    def find_probablity(self, my_dict: dict):
        """
        Description:
            This function is used to find the probability with certain condition
        Parameter:
            my_dict: The my_dict to be checked 
        Return:
            Returns probablity
        """
        try:
            lg.info("\n1: find is the probability that it's not raining and there is heavy traffic and I am not late? "
                    "\n2: probability that I am late? \n3: I arrived late at work, what is the probability that it "
                    "rained that day?") 
            choice = int(input('Enter the choice: '))
            if choice == 1:
                probablity = my_dict.get('no_rainy_traffic_no_late')
            elif choice == 2:
                probablity = my_dict.get('rainy_traffic_late')+my_dict.get('rainy_no_traffic_late') + \
                    my_dict.get('no_rainy_traffic_late') + \
                    my_dict.get('no_rainy_no_traffic_late')
            elif choice == 3:
                # P(R | L) = P(R∩L)/P(L)
                probablility_of_late = my_dict.get('rainy_traffic_late') + my_dict.get('rainy_no_traffic_late') + \
                             my_dict.get('no_rainy_traffic_late') + \
                             my_dict.get('no_rainy_no_traffic_late')
                probablity = (my_dict.get(
                    'rainy_traffic_late') + my_dict.get('rainy_no_traffic_late')) / probablility_of_late
            else:
                print('Valid number')

            return probablity

        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == "__main__":
    stats_obj = ProbabilityComputation()
    stats_obj.create_probability()
