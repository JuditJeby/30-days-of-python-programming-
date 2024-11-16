'''
Pyhon program to find Compound interest
Author: Kenaz mathukutty
Created: 16/11/2024
'''
interest_amount=int(input("Enter the principle interest: "))
rate=int(input("Enter rate of interest: "))
time=int(input("Enter time in year: "))
amount=interest_amount*(1+(rate/100))**time
intrest_amout=amount-interest_amount
print("intrest",intrest_amout)