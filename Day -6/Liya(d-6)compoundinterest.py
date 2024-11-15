"""Author:Liya Binu
Date:15-11-2024
program to calculate the compound interest"""
principal_amount=float(input("Enter the principle amount:"))
interest_rate=float(input("Enter the rate of interest:"))
time=float(input("Enter time of deposit in years:"))
amount=principal_amount*(1+(interest_rate/100))**time
compound_interest=amount-principal_amount
print("compund interest is",compound_interest)