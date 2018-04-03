# Simon McLain 2018-03-17
# Problems: Python Fundamentals
# Write a function simpleinterest that, for a loan with simple interest, takes a principal
# amount, an interest rate, and a number of periods, and returns the total amount
# repaid.

Capital = int(input("Please enter the loan amount: "))
Capital = float(Capital)

Interest = int(input("Please enter the the interest rate: "))
Interest = float(Interest)/ 100

Period = int(input("Please enter the term of the loan: "))
Period = float(Period)

Total_repayment = Capital + (Capital * Interest * Period)

print("The total loan amount is: €", Total_repayment)






