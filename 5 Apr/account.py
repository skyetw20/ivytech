#Divyanshu Gupta
#Your class here 
#Name of the assignment
#Due date of the assignment

class Account:
  #Constructor for defining variables 
  def __init__(self,id=0,balance=100,annualInterestRate=0):
    #assigning private variables
    self.__id=int(id)
    self.__balance=float(balance)
    self.__annualInterestRate=float(annualInterestRate)
  #Mutators
  def set_id(self,new_id):
    self.__id=new_id
  def set_balance(self,new_balance):
    self.__balance=new_balance
  def set__annualInterestRate(self,new_rate):
    self.__annualInterestRate=new_rate
  #accessors
  def get_id(self):
    return(self.__id)
  def get_balance(self):
    return(self.__balance)
  def get_annualInterestRate(self):
    return(self.__annualInterestRate)
  #Function for calculating Monthly interest rate
  def getMonthlyInterestRate(self):
    return(self.__annualInterestRate/12)
  #function for calculating monthly interest
  def getMonthlyInterest(self):
    rate=(self.__annualInterestRate/100)/12
    return(self.__balance*rate)
  #Function to perform withdraw operation
  def withdarw(self,amount):
    self.__balance-=amount
    print('Withdrawal done')
  #function to perform deposit operation
  def deposit(self,amount):
    self.__balance+=amount
    print('Done!!!')