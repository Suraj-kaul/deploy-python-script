# PRIME NUMBER WITHIN RANGE

first_number = 1
last_number = 20

print("range of prime number are :")

for number in range(first_number,last_number+1):

    if number > 1:
        for i in range(2, number):
            if(number%i==0):
                break
        else:
            print(number, end=" ")