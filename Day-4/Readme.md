Here's a Python program to calculate the factorial of a given number using a for loop:

```
n = int(input("Enter a number: "))

fact = 1
for i in range(1, n + 1):
    fact *= i

print("Factorial of", n, "is", fact)
``

Explanation:

1. Prompt the user to enter a number.
2. Initialize `fact` to 1.
3. Use a for loop to iterate from 1 to `n` (inclusive).
4. Multiply `fact` by each number in the range.
5. Print the result.

Example:

Input: `Enter a number: 5`
Output: `Factorial of 5 is 120`
```
