'''
python program to find factorial of a number
Author:kevin joseph
date:12/11/2024
'''
num=int(input("enter the number:"))
factorial=1
for i in range(1,num + 1):
    factorial=factorial*i
print("The factorial of",num,"is",factorial,)
