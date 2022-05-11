
import sys
first_num = sys.argv[1]
last_num = sys.argv[2]

number = 1


if number > 1:
    for i in range(2, number):
            if(number%i==0):
                break
            else:
                print("prime numbers:",number)