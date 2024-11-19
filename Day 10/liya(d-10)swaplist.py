"""Author:Liya Binu
Date:19-11-2024
program to swap two elements in a list"""
list=[1,2,3,4,5,6]
print("list =",list)
swap1=int(input('Enter the index of first element to swap:'))
swap2=int(input("enter the index of the second element to swap:"))
list[swap1],list[swap2]=list[swap2],list[swap1]
print("swapped list=",list)