# Simon McLain 2018-04-02
"""Write a function newtonsroot that takes a number x and returns its square root
correct to six decimal places as calculated by Newton’s method. Newton’s method is
to make an initial (random) guess r0 at the square root, and to repeatedly improve
it as follows:
ri+1 = ri −
r2
i − x
2ri
For example:
> newtonsroot(100)
10.0
> newtonsroot(144)
12.0"""

def newtonsroot(x):
  z = x / 2.0
  n = z - ((z**2 - x)/(2 * z))
  while abs(z -n) >= 0.0000001:
    z = n - ((z**2 - x)/(2 * z))

print(newtonsroot(10))

  

  

