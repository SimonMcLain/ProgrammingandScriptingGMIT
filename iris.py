# Simon McLain 2018-03-04
# Topic 5, exercise 5
# Please complete the following exercise this week. 
# Write a Python script that reads the Iris data set in and 
# prints the four numerical values on each row in a nice format. 
# That is, on the screen should be printed the petal length, petal width, 
# sepal length and sepal width, and these values should have the decimal places aligned, 
# with a space between the columns.

import csv

with open("data/iris.csv") as f:
  for line in f:
    a = line.split(',')
    print (a[0], a[1], a[2], a[3])
    

    

    







    
    




    
  


    


 
 
  #for line in f:
    # print(line.split(',')[0].format(*line)
  
