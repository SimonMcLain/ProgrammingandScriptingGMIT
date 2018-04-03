# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# 
# Solution to Project Euler problem 5
# Copyright (c) Project Nayuki. All rights reserved.
# 
# https://www.nayuki.io/page/project-euler-solutions
# https://github.com/nayuki/Project-Euler-solutions
# 

import fractions 

def compute():
	ans = 1
	for i in range(1, 21):
		ans *= i // fractions.gcd(i, ans)
	return str(ans)
if __name__ == "__main__":
	print(compute())
