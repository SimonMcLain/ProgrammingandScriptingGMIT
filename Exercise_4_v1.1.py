# Simon Mclain 2018-03-27
# Second attempt as v.1.0 ran very slowly on my computer. Solution base on code found at: 
# https://stackoverflow.com/questions/8024911/project-euler-5-in-python-how-can-i-optimize-my-solution
# I modified the code slightly so it would run, changing xrange to range and adding parentheses to the print statements.
# This code runs much faster than my original v1.0

check_list = [11, 13, 14, 16, 17, 18, 19, 20]

def find_solution(step):
    for num in range(step, 999999999, step):
        if all(num % n == 0 for n in check_list):
            return num
    return None

if __name__ == '__main__':
    solution = find_solution(20)
    if solution is None:
        print ("No answer found")
    else:
        print ("found an answer:", solution)
