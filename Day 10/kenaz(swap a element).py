'''
python program
Author: Kenaz mathukutty
Created: 22/11/2024
'''
my_list=[1,2,3,4,5,6,]
print("original list,",my_list)
index1 = int(input("Enter index of first element to swap: "))
index2 = int(input("Enter index of second element to swap: "))
my_list[index1], my_list[index2] = my_list[index2], my_list[index1]
print("Swapped List:", my_list)
