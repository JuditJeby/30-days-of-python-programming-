number=int(input("Enter a number"))
armstrong=number
sum=0
while(number>0):
    reminder=number%10
    sum=sum+reminder*reminder*reminder
    number=number//10
print(sum)
if sum==armstrong:
    print("the number is armstrong")
else:
     print("the number is not armstrong")
