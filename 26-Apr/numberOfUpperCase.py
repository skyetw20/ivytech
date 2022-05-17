#Divyanshu Gupta
#SDEV 220
#Counting the number of upper care alphabets in the string given by user
#26th April 2022

count = 0


def countUppercase(s):
    return countUppercaseHelper(s, len(s))


def countUppercaseHelper(s, high):#helper function for counting the number of upper case letters
    global count
    if s == '':
        return count

    if s[0].isupper():
        count += 1
    return countUppercaseHelper(s[1:high], high)#recusive function call


print(countUppercase(input("Enter a string: ")))