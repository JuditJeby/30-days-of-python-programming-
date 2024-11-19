"""
Program to find the factorial of a number
Author: Judit Jeby
created on 12/11/2024
 """



num=int(input("Enter a number"))
fact=1
for i in range(1,(num+1)):
    fact*=i
    
print(f"Factorial of the number is  {fact}")