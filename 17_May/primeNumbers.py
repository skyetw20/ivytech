#Divyanshu Gupta
#SDEV 220
#Finding prime numbers and storing them in a STACK
#17th May 2022
class Stack:
		def __init__(self):
			self.__elements = []

		# Return true if the tack is empty
		def isEmpty(self):
			return len(self.__elements) == 0

		# Returns the element at the top of the stack
		# without removing it from the stack.
		def peek(self):
			if self.isEmpty():
				return None
			else:
				return self.__elements[len(self.__elements) - 1]

		# Stores an element into the top of the stack
		def push(self, value):
			self.__elements.append(value)

		# Removes the element at the top of the stack and returns it
		def pop(self):
			if self.isEmpty():
				return None
			else:
				return self.__elements.pop()

		# Return the size of the stack
		def getSize(self):
			return len(self.__elements)

stack=Stack() # creates an object of the class Stack 
def isprime(num): #defining a fucntion to check whether a number is prime or not
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True
i=1 #declaring a int type variable for iterating
while stack.getSize()<51:# iterating from 1 till the size of the stack becomes 50
    if isprime(i): # checking the number for prime condition
        stack.push(i) # pushing into the stack if a number is prime
    i+=1
while not stack.isEmpty():#iterating on the stack to get out all the prime numbers stored
    print(stack.pop())# using pop fucntion to get the number at the top
