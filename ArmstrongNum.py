# Python program to check Armstrong number
num = int(input("Enter a number"))
SUM = 0
temp = num
while temp > 0:
    dig = temp % 10
    SUM += dig ** 3
    temp //= 10
if SUM == num:
    print("number is an armstrong")
else:
    print("number is not an armstrong number")
