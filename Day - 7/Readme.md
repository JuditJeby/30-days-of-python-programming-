Here is the original Python program to check whether a number is Armstrong:

*Input a number*
num = int(input("Enter a number: "))

*Calculate number of digits*
num_digits = len(str(num))

*Initialize sum*
sum = 0

*Calculate sum of digits raised to power of num_digits*
temp = num
while temp > 0:
digit = temp % 10
sum += digit ** num_digits
temp //= 10

*Check if sum equals original number*
if sum == num:
print(f"{num} is an Armstrong number.")
else:
print(f"{num} is not an Armstrong number.")
