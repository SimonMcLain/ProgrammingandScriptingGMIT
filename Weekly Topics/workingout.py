import csv

with open("data/iris.csv", 'rb') as f:
    rdr = csv.reader(f)
    with open("result", "wb") as result:
      wtr= csv.writer( result )
      for r in rdr:
        print (wtr.writerow( (r[0], r[1], r[3]) ))
        

    

