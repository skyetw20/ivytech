#Divyanshu Gupta
#SDEV 220
#Game: nine heads and tails
#19th April 2022

def dec_to_bin(num): # function to convert the given number to binary format 
    bin = []
    while num > 0:
        bin.append(num % 2)
        num = num // 2

    while len(bin) < 9:
        bin.append(0)

    bin.reverse()
    return bin


def print_matrix(mat): # function to print the H and T in the form of a matrix corresponding to the 0 and 1 respectively 
    for i in range(len(mat)):
        if mat[i] == 0:
            print('H', end=' ')
        else:
            print('T', end=' ')

        if (i + 1) % 3 == 0:
            print()


num = int(input("Enter a number between 0 and 511: ")) # taking input from the user 
mat = dec_to_bin(num) # taking the binary form of the given number
print_matrix(mat) #calling print matrix function to print the matrix in desired form
