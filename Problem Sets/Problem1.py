# Simon McLain 2018-04-02
"""Write a function sumultiply that takes two integer arguments and returns their
product. The function should not use the * or / operators. For example:
> sumultiply(11, 13)
143
> sumultiply(5, 123)
615"""

x = int(input("Enter the first integer to multiply:"))
y = int(input("Enter the second integer to multiply:"))
#user input
def sumultiply(x, y):
  # create a variable that will become the answer
  total = 0
  #loop over y adding x to the total
  for i in range(y):
    total = total + x
  return total

print("The product of", x, "multiplied by", y, "is equal to:", sumultiply(x, y))







