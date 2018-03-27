# Simon McLain, edited from a script created by Ian McLoughlin on 2018-02-12. Week 2 Exercise for Programming and Scripting
# This program coverts the first and last letter of someones name into a fibonaci number.

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1
  while n >= 0:
    i, j = j, i + j
    n = n - 1
  return i
name = "Simon"
first = name[0]
last = name[-1]
firstno = ord(first)
lastno = ord(last)
x = firstno + lastno
ans = fib(x)
print("My first name is", name)
print("The first letter", first, "is number", firstno)
print("The last letter", last, "is number", lastno)
print("Fibonacci number", x, "is", ans)