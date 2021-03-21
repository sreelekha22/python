# Python3 code to demonstrate working of
# Extract digits from Tuple list
# Using map() + chain.from_iterable() + set() + loop
from itertools import chain
import re

test_list = [(15, 3), (3, 91), (61, 10), (99, 2)]
print("The original list is : " + str(test_list))

temp = map(lambda ele: str(ele), chain.from_iterable(test_list))
res = set()
for sub in temp:
    for e in sub:
        res.add(e)

print("The extracted digits : " + str(res))

# Using regex expression

temp = re.sub(r'[\[\]\(\), ]', '', str(test_list))
result = [int(ele) for ele in set(temp)]
print("The extracted digits : " + str(result))
