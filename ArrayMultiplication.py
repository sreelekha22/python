# python program for find remainder of an array multiplication and divided by n
arr = [1, 2, 3, 4, 5]
print(arr)
n = len(arr)
mul = 1
for i in range(0, n):
    mul *= arr[i]

print(mul % n)
