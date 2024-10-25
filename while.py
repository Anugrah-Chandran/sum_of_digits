'''Author: Anugrah Chandran
Date: 25-10-24
Description: Python program to find the number of digits of the given number'''
number=int(input("Enter your number:"))
sum_of_digits=0
while number>0:
    remainder=number%10
    sum_of_digits=sum_of_digits+remainder
    number=number//10
print("Sum of the digits of the given number:",sum_of_digits)