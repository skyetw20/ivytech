#Divyanshu Gupta
#SDEV 220
#Generating random numbers and counting their frequency
#19th April 2022

import random  #importing random for generating random numbers

lst = [] #empty list for storing the numbers
for i in range(1000):  #loop iterating 1000 times and each time adding a random number to the list
    lst.append(random.randint(0, 9)) 

counts = []  #empty list for storing the frequency of occurance of each digit
for i in range(10): #iterating over all the digits and counting their frequency
    counts.append(lst.count(lst[i]))

for i in range(10): #loop to print the frequency of each number
    print(i, ":", counts[i], "times")