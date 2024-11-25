"""Author:Liya Binu
Date.25-11-2024
program to check if elements exists in list"""
list = [1, 2, 3, 4, 5]
element = int(input("Enter the element to check: "))

if element in list:
    print(f"{element} exists in the list.")
else:
    print(f"{element} does not exist in the list.")