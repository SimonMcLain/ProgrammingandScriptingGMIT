# Simon Mclain 2018-03-04

""""Find the solution to Problem 5 in Project Euler 2520 is the smallest number that
can be divided by each of the numbers from 1 to 10 without any remainder. What is the smallest 
positive number that is evenly divisible by all of the numbers from 1 to 20? https://projecteuler.net/problem=5
Researched from various sources in Stackoverflow 
https://stackoverflow.com/questions/8024911/project-euler-5-in-python-how-can-i-optimize-my-solution
and YouTube https://www.youtube.com/results?search_query=Project+Euler+5+Python"""

def answer(number):
  for i in range(1, 21):
    if number % i != 0:
      return False
  return True
  """def defines the function answer() as a number. for loop interates over the
  integers in the range 1 to 20 and returns True when number is evenly divisible by the specified range)"""
number = 1
while True:
  if answer(number):
    break
  number += 1

print("The Solution to Problem 5 in Project Euler is:", number)
  
"""The break statement stops the code interating back over the same number when the answer is True, 
then sums the values using the += 1 to produce the largest evenly divisble number"""
  