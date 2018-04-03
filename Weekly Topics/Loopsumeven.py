# Simon McLain, 2018-02-22
# Sum all even numbers from 1 to 100

sum = 0
i = 0

while i <= 100: 
    if i % 2 == 0:
        sum = sum + i
    i = i + 1

print("The sum of the numbers 1 = 100 is:", sum)