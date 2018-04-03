#Simon McLain 2018-03-11
#Find the greatest common divisor
#From functions - defininf functions, compartmentalisation
#gcd important for cryptography

def gcd(x, y):
  while x !=y:
    if x > y:
      x = x - y
    else:
      y = y - x
  return x
   
z = gcd(221, 323) # create a temporary variable to represent the define function and shorten the print command


print("The GCD of 221 and 323:", z)



print("The GCD of 625120 and 3579804:", gcd(625120, 3579804))
print("The GCD of 4 and 18:", gcd(4, 18))
print("The GCD of 50 and 100:", gcd(50, 100))







