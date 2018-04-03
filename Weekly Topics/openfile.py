#open files 208-02-28
#f= the file I was to open
#printinf the file only is usually not intersting
# don't forget to close the file


#f = open("data/iris.csv")

#print(f)

#print(f.read())

#f.close()

#better to close with 'with'

with open("data/iris.csv") as f:
  contents = f.read()
  print(contents)

print("Out of width")

  #print(f.read())



