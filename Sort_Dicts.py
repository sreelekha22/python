# ways to sort list of dictionaries by value in python
from operator import itemgetter

dicts = [
    {"name": "Johny", "salary": 1000},
    {"name": "Emily", "salary": 3500},
    {"name": "Harry", "salary": 1500},
    {"name": "Arina", "salary": 2000}
]
# 1.by using lambda function
# ascending order
print(sorted(dicts, key=lambda item: item['salary']))
# descending order
print(sorted(dicts, key=lambda item: item['salary'], reverse=True))

# 2. by using itemgetter method
# ascending order
print(sorted(dicts, key=itemgetter('name')))
# descending order
print(sorted(dicts, key=itemgetter('name'), reverse=True))
