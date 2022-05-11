# PRIME NUMBER WITHIN RANGE

first_number=int(input("ENTER YOUR FIRST NUMBER : "))
last_number=int(input("ENTER YOUR LAST NUMBER : "))

print("range of prime number are :")

for number in range(first_number,last_number+1):

    if number > 1:
        for i in range(2, number):
            if(number%i==0):
                break
        else:
            print(number, end=" ")