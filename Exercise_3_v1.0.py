# Simon McLain, 2018-2-11

"""Write a single Python script that starts with an integer and repeatedly applies the Collatz function
 (divide by 2 if even, multiply by three and 1 if odd) using a while loop and if statement. 
 At each iteration, the current value of the integer should be printed to the screen. 
 Specify in your code the starting value of 17."""

n = 17
"""assigns the variable n to the range 0 to 17"""
while n > 1:
  """starts the loop interating at the integer 2"""
  if n % 2 == 0:
    n = n / 2
    print(n) 
    """The if statement finds even integers 
    by checking the reminder equals 0 when divided by 2"""
  else:
    n = (n * 3) +1 
    print(n)
    """The else statement deals with odd integers that are 'skipped' by the if statement
    multiplies them by 3 and prints the result"""
