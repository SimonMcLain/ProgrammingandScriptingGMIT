#Simon McLain 2018-03-11
#Second input, quicker to find the greatest common divisor
#From functions - defininf functions, compartmentalisation
#gcd important for cryptography

def gcd(x, y):
  while x != 0 and y != 0:
    if x > y:
      x = x % y
    else:
      y = y % x
  if x == 0:
    return y
  else:
    return x

z = gcd(6, 15)

print("The GCD of 6 and 15 is:", z)

