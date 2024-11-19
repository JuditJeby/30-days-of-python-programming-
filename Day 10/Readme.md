Here's a Python program to swap two elements in a list:

```
# Define a list
my_list = [1, 2, 3, 4, 5]

# Print original list
print("Original List:", my_list)

# Input indices to swap
index1 = int(input("Enter index of first element to swap: "))
index2 = int(input("Enter index of second element to swap: "))

# Swap elements
my_list[index1], my_list[index2] = my_list[index2], my_list[index1]

# Print swapped list
print("Swapped List:", my_list)
```
