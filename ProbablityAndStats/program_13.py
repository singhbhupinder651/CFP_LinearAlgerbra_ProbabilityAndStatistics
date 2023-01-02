"""
    @Author: Bhupinder Singh
    @Date: 01-01-2023
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 01-01-2023
    @Title: The table below shows the height, x, in inches and the pulse rate, y, per minute,
            for 9 people. Write a program to find the correlation coefficient and interpret your result.
            x ⇒ 68 72 65 70 62 75 78 64 68
            y ⇒ 90 85 88 100 105 98 70 65 72

"""

import sys

from data_log import get_logger

lg = get_logger(name="(program_13)", file_name="data_log.log")


class Statistics:

    def find_correlation_coefficient(self, x, y):
        """
        Description:
            This function is used to find the correlation coefficient
        Parameter:
            x: The x is height of people to be checked
            y: The y is pulse rate per minute to be checked
        Return:
            Returns co_efficient
        """
        try:
            # ρ (X,Y) = cov (X,Y) / σx, σy
            # summation ((x-x^)x(y-y^)/n-1) / summation ((x-x^)2 x (y-y^)2 / n-1)
            x_sum = sum(x)
            y_sum = sum(y)
            n = len(x)

            xy_sum = sum([x[i]*y[i] for i in range(len(x))])
            sum_of_sqaure_of_x = sum([x[i] * x[i] for i in range(len(x))])
            sum_of_sqaure_of_y = sum([y[i] * y[i] for i in range(len(y))])

            # pearson co-relation co-efficient
            co_efficient = (n * xy_sum - x_sum*y_sum) / \
                ((n * sum_of_sqaure_of_x - x_sum ** 2)
                 * (n * sum_of_sqaure_of_y - y_sum ** 2)) ** 0.5
            return co_efficient
        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == "__main__":
    x = [68, 72, 65, 70, 62, 75, 78, 64, 68]
    y = [90, 85, 88, 100, 105, 98, 70, 65, 72]
    stats_obj = Statistics()
    pearson_corelation_coefficient = stats_obj.find_correlation_coefficient(
        x, y)
    lg.info(
        f'the co-relation co_efficient of x and y: {pearson_corelation_coefficient}')
