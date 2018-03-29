# Simon McLain, 2018-2-12
"""Write a single Python script that starts with an integer and repeatedly applies the Collatz function 
(divide by 2 if even, multiply by three and 1 if odd) using a while loop and if statement. 
At each iteration, the current value of the integer should be printed to the screen."""


n = int(input("Please enter an integer: "))
"""asks the user to provide the integer and 
assigns it to the variable n"""
while n > 1:
    if n % 2 == 0:
        n = n / 2
        print(n) 
    else:
        n = (n * 3) + 1
        print(n)
