Here is the Python program to interchange the first and last element in a list:

my_list = [1, 2, 3, 4, 5]
print("Original List:", my_list)

my_list[0], my_list[-1] = my_list[-1], my_list[0]
print("Swapped List:", my_list)

This program directly swaps the first and last elements of the list using tuple packing and unpacking.
