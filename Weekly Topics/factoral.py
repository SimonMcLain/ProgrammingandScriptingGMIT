# Simon McLain 2018-03-11
# Topic 6, Exercise 6
# Please complete the following exercise this week. Write a Python script containing 
# a function called factorial() that takes a single input/argument which is a 
# positive integer and returns its factorial. The factorial of a number is that number 
# multiplied by all of the positive numbers less than it. For example, the factorial of
# 5 is 5x4x3x2x1 which equals 120. You should, in your script, test the function by 
# calling it with the values 5, 7, and 10.

# Instructions: run the program and enter a positive integer when asked


n = int(input("Enter a positive integer and I will return its factorial: "))
def factorial(n):
  factorialn = 1
  for i in range(1, n + 1):
    factorialn = factorialn * i
  return factorialn
   
print("The factorial for of the number you entered is:", factorial(n))

