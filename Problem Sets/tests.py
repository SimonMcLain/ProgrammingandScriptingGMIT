"""for n in range(2, 12):
     for x in range(2, n):
         if n % x == 0:
             print(n, 'equals', x, '*', n//x)
             break
     else:
         # loop fell through without finding a factor
         print(n, 'is a prime number')"""

"""def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)"""

"""def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))"""

"""def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))"""

"""def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")"""

"""def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

parrot('a thousand', state='pushing up the daisies')"""

"""squares = [x**2 for x in range(10)]
print(squares)"""

"""lists = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(lists)"""

"""vec = [[1,2,3], [4,5,6], [7,8,9]]
[num for elem in vec for num in elem]"""

"""matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12],
]
matrix = [[row[i] for row in matrix] for i in range(4)]

print(matrix)"""

"""matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12],
]
matrix = list(zip(*matrix))

print(matrix)"""

"""tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)

dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(dict)

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
  print(k, v)"""

"""import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)"""

"""print(filtered_data)
string1, string2, string3 = '', '', 'Hammer Dance'
non_null = string1 or string2 or string3
print(non_null)"""

"""import fibo
fib = fibo.fib
fib(10)
print(fib)"""

"""x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)

hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # Note use of 'end' on previous line
    print(repr(x*x*x).rjust(4))

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))"""


"""print('3.1'.zfill(5))

print('This {food} is {adjective}.'.format(
      food='spam', adjective='absolutely horrible'))"""

"""import math
print('The value of PI is approximately {0:.5f}.'.format(math.pi))"""

"""table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print('{0:10} ==> {1:10d}'.format(name, phone))"""

"""import math
print('The value of PI is approximately %.20f.' % math.pi)"""

"""while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")"""

"""try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))    # the exception instance
    print(inst.args)     # arguments stored in .args
    print(inst)          # __str__ allows args to be printed directly,
                         # but may be overridden in exception subclasses
    x, y = inst.args     # unpack args
    print('x =', x)
    print('y =', y)"""

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

divide(2, 1)

divide(2, 0)

divide("2", "1")









      






 
  









