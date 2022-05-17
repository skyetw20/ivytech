#Divyanshu Gupta
#Your class here 
#Name of the assignment
#Due date of the assignment

num=0                     #Counter variable for keeping track of numbers printed per line
for i in range(200,400):  #Begning of for loop for iterating over the number between 200 and 400
  if i%7==0 and i%8!=0:   #Condition to check divisibility
    num+=1
    print(i, end=' ')
    if num%10==0:         #Condition to move to the new row after ten printed in each row
      print('\n')         #Print '\n' for moving to new row