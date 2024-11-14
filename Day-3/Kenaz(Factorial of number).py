'''Python program to find factorial of a Number
Author:kenaz mathukutty
created:14/11/2024'''
integer=int(input("enter a number: "))
fact=1
for i in range(1,integer+1):
    fact*=i
print("Factorial of",integer,"is",fact)