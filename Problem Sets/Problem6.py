# Simon McLain 3018-04-02
"""Write a function pitondecs that takes an integer n and returns  correct to n decimal
places. For example:"""

import math
from math import pi 

n = int(input("State number of decimals places for PI:", ))
pitondecimal = [str(round(pi, n))]

print("pi to", n, "decimal places is:", pitondecimal)
