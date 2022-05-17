#Divyanshu Gupta
#Your class here 
#Name of the assignment
#Due date of the assignment

#importing class from account file
from account import Account
#defining variables as given
id=3345
balance=35000
annual_rate=4.5
#creating object of the class with given parameters
a=Account(id,balance,annual_rate)
#withdrawing an amount of 2500
a.withdarw(2500)
#depositing an amount of 3000
a.deposit(3000)
#printing the final values
print('Account ID:',a.get_id())
print('Balance :',a.get_balance())
print('Monthly Interest Rate: ',a.getMonthlyInterestRate())
print('Monthly Interest: ',a.getMonthlyInterest())