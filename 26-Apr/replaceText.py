#Divyanshu Gupta
#SDEV 220
#Replacing word in the givel text file
#26th April 2022

filename = input("Enter a filename: ").strip() #accepting the name of file with extension prensent in same directory as programm
string = input("Enter the old string to be replaced: ") #accepting the string to be replaced
new = input("Enter the new string to replace the old string: ") #accepting the new string
file = open(filename, 'r') #opening the file in read mode
data = ''
for line in file:#iterating line by line in file
    data += line.replace(string, new)

resFile = open(filename, 'w')#opening the file in write mode
resFile.write(data)#writing the data back to the file
resFile.close()
print("done")
