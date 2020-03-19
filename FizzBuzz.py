#!/usr/bin/env python3

byThree = False
byFive = False


#Recieve input from the user
number = int(input("Please input a number:\n----> "))

#check if number is divisable by 3 or 5

result3 = int(number % 3)
result5 = int(number % 5)

if result3 == 0:
    byThree = True

if result5 == 0:
    byFive = True


#Print results

if ((not byThree) and (not byFive)):
    print(number)
    #print("\n\nYour selected number of", number, "is not divisable by 3 or 5.\n\n")
elif byThree and byFive:
    print("fizzbuzz")
elif byThree:
    print("fizz")
else:
    print("buzz")
