# Simon McLain 2018-03-02
# Format command in Python
# See Python Tutorial 7.0 https://docs.python.org/3/tutorial/inputoutput.html
# Curly brackets enable formating, in this case instructing the number of places within the number
# also note the use of ** to square, cube etc

for i in range(1, 10):
  print('{:2d} {:3d} {:4d} {:5d}'.format(i, i**2, i**3, i**4))



