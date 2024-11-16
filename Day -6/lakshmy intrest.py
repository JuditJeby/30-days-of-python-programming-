''' author = Lakshmy Byju
   date = 15-11-2024
   python program to find intrest 
'''
principal_amount=int(input("Enter a principal number"))
intrest_rate=int(input("Enter a rate number"))
time=int(input("Enter a time deposite in year"))
amout=principal_amount*(1+(intrest_rate/100))**time
intrest=amout-principal_amount
print("intrest",intrest)