# Simon Mclain 2018-03-27
"""Second attempt as v.1.0 ran very slowly on my computer. Solution base on code found at: 
https://stackoverflow.com/questions/8024911/project-euler-5-in-python-how-can-i-optimize-my-solution 
I modified the code slightly so it would run, changing xrange to range and adding parentheses to the print statements.
This code runs much faster than my original v1.0"""

check_list = [11, 13, 14, 16, 17, 18, 19, 20]
"""This is much faster as it reduces the number of iterations. We know the solution for the integers 1 to 10, 
we can use this list and also omitt 12 and 15 as they are mulitples of 6 and 5"""
def find_solution(step):
    for num in range(step, 999999999, step):
        if all(num % n == 0 for n in check_list):
            return num
    return None
"""steps through numbers up 999999999, dividing them by check list
and returning numbers that are even"""
if __name__ == '__main__':
    solution = find_solution(20)
    if solution is None:
        print ("No answer found")
    else:
        print ("found an answer:", solution)
"""Ends the script with 2 possible conditions, either no number is evenly
divisible or there is a solution"""