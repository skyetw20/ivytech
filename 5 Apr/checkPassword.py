#Divyanshu Gupta
#Your class here 
#Name of the assignment
#Due date of the assignment

#Taking input form the user
n=input('Enter password: ')
#initialising counter variable for counting number of digits in password
d=0
#iterating over the password for counting digits
for i in n:
   if i.isdigit():
    d+=1
#displaying result 
if d>=3 and len(n)>8 and n.isalnum():
  print('valid password')
else:
  print('invalid password')