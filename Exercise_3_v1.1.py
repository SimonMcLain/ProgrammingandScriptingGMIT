# Simon McLain, 2018-2-12
# Collatz Conjecture added user request to input integer

n = int(input("Please enter an integer: "))

while n > 1:
    if n % 2 == 0:
        n = n / 2
        print(n) 
    else:
        n = (n * 3) + 1
        print(n)
