# Simon McLain, edited from a script created by Ian McLoughlin on 2018-02-12: 
# https://github.com/ianmcloughlin/python-fib/blob/master/fibname.py


# Week 1 exercise 1:
"""Calculate the nth Fibonacci number where n the sum of the first and last letters of your first name as numbers. and
post on the discussion forum: My name is Simon, so the first and last letter of my name (S + N = 19 + 14) give the number  33,
the 33rd Fibonacci number is 352,4578."""

# Week 2 exercise 2: 
"""This program coverts the first and last Unicode characteres of someones surname into integers, adds them together
and returns the corresponding fibonacci number for their sum. It also prints the definition of the ord() function."""

def fib(n):
  """defines n as
  a fibonacci number, fib() 
  is is a function in the Python standard library)"""
  i = 0
  j = 1
  n = n - 1
  """assigns initial values to the varibles
  i & j, assigns a calculation to the variable n"""
  while n >= 0:
    i, j = j, i + j
    n = n - 1
  return i
  """interates over the loop provided (while!') n is
  greater than or equal to 0, preventing negative counting"""
name = "McLain"
first = name[0]
last = name[-1]
"""creates the container 'name' for my surname
and then assigns the 'first' and 'last' letters"""
firstno = ord(first)
lastno = ord(last)
x = firstno + lastno
ans = fib(x)
"""Converts first and last Unicode characters of my surname to integers, adds them together
and returns the corresponding fibonacci number. Ord() is a function in the Python standard library"""
print("My surname is:", name)
print("The first letter", first, "is number:", firstno)
print("The last letter", last, "is number:", lastno)
print("Fibonacci number", x, "is:", ans)

print("The ord() function is used to return an integer of the given single Unicode character. The returned integer represents the Unicode code point.(reference: https://www.jquery-az.com)")

"""Print statements to return the output of the script to the terminal""" 