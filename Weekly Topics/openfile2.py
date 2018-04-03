# Simon McLain 2018-03-02
# Opening a file and splitting up the stings
# Topic 5 
# Python Tutorial https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
# line.split(,) 
# Look at Python tutorial to remove new line character
# [#] insert the positional number of the value in the string to print that value
# end='' remove the unseen new line character

with open("data/iris.csv") as f:
  for line in f:
    print(line.split(',')[4], end='')






