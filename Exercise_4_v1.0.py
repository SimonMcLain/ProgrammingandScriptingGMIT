# Simon Mclain 2018-03-04
# GMIT Programming and Scripting Topic 4 Exercise 4
# Find the solution to Problem 5 in Project Euler
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# https://projecteuler.net/problem=5
# Researched from various sources in Stackoverflow https://stackoverflow.com/questions/8024911/project-euler-5-in-python-how-can-i-optimize-my-solution
# and YouTube https://www.youtube.com/results?search_query=Project+Euler+5+Python 

def answer(number):
  for i in range(1, 21):
    if number % i != 0:
      return False
  return True

number = 1
while True:
  if answer(number):
    break
  number += 1

print("The Solution to Problem 5 in Project Euler is:", number)


  







