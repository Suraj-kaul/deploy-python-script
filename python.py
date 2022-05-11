# PRIME NUMBER WITHIN RANGE
import sys
first_number = sys.argv[1]
last_number = sys.argv[2]



print("range of prime number are :")

for number in range(first_number,last_number+1):

    if number > 1:
        for i in range(2, number):
            if(number%i==0):
                break
        else:
            print(number, end=" ")