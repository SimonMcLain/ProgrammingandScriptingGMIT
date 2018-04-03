# Simon McLain, 2018-03-01
# Project Euler problem 1
# https://projecteuler.net/problem=1

sum = 0
i = 1

while i < 1000:
  if i % 3 == 0:
    sum = sum + i
  elif i % 5 == 0:
    sum = sum + i
  i = i + 1

print("The sum of all the numbers between 1 and 1000 that are divisble by 3 and 5 is:", sum)


