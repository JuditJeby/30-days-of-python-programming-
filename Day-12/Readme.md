 Here's a simple Python program to check if an element exists in a list without defining a function:

```
lst = [1, 2, 3, 4, 5]
element = int(input("Enter the element to check: "))

if element in lst:
    print(f"{element} exists in the list.")
else:
    print(f"{element} does not exist in the list.")
```

_Explanation:_

1. We create a sample list `lst`.
2. We ask the user to input an element to check.
3. We use the `in` operator to check if the element exists in the list.
4. If the element exists, we print a message indicating its presence.
5. If the element does not exist, we print a message indicating its absence.

_Example Output:_

Enter the element to check: 3
3 exists in the list.

Enter the element to check: 6
6 does not exist in the list.
[25/11, 7:37 am] Meta AI: Here's a simple Python program to check if an element exists in a list without defining a function:

```
lst = [1, 2, 3, 4, 5]
element = int(input("Enter the element to check: "))

if element in lst:
    print(f"{element} exists in the list.")
else:
    print(f"{element} does not exist in the list.")
`''
