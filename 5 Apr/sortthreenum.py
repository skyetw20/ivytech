#Divyanshu Gupta
#Your class here 
#Name of the assignment
#Due date of the assignment

num1,num2,num3= [x for x in input("Enter three numbers: ").split(', ')]   #Taking the three numbers from user as input seperated by comma and space into three variables
def displaySortedNumbers(num1, num2, num3):                               #Function to sort the numbers in increasing order
  l=[num1,num2,num3]
  l.sort()
  print('The sorted numbers are ',end='')
  for i in l:
    print(i,end=' ')
  return('')
def displaySortedNumbers_decreasing(num1,num2,num3):                      #Function to sort the numbers in decreasing order
  l=[num1,num2,num3]
  l.sort()
  l.reverse()
  print('The sorted numbers in decreasing order are ',end='')
  for i in l:
    print(i,end=' ')
  return('')
print(displaySortedNumbers(num1,num2,num3))                              #Displaying the numbers sorted in increasing order
print(displaySortedNumbers_decreasing(num1,num2,num3))                   #Displaying numbers sorted in decreasing order