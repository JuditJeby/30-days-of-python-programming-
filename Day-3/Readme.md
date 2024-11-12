Program to print n numbers using for loop.
Explanation
Here's how to print numbers from 1 to n using a for loop in Python:

```
n = int(input("Enter a number: "))
for i in range(1, n+1):
    print(i)
```

Explanation:

- `n = int(input("Enter a number: "))` asks the user to input a number.
- `range(1, n+1)` generates numbers from 1 to n (inclusive).
- `for i in range(1, n+1)` iterates over these numbers.
- `print(i)` prints each number.

Example:

Input: `Enter a number: 5`
Output:

```
1
2
3
4
5
```
