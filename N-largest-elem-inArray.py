# python program to find N largest elements from list
# by using inbuilt method
li = [10, 29, 35, 100, 20, -45, 90]
n = 4
li.sort()
print('sorted list : ', li)
print(n, ' largest numbers : ', li[-n:])

# by using descending order
li1 = [100, 20, 10, 25, 78, 5, 90]
n1 = 2
li1.sort(reverse=True)
print('Descending order : ', li1)
print(n1, ' largest numbers : ', li1[:n1])


# by using logic
def NlargestNums(li2, num):
    print('given list : ', li2)
    final_list = []
    for i in range(0, num):
        max1 = 0
        for ele in li2:
            if ele > max1:
                max1 = ele
        li2.remove(max1)
        final_list.append(max1)
    print(num, ' largest numbers from given list : ', final_list)


NlargestNums([10, 29, 35, 100, 20, -45, 90], 3)
