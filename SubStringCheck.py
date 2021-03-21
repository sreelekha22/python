from re import search

OriginalStr = 'check if sub string is in the original string or not'
SubStr = 'original'

# by using if else block and in operator
if SubStr in OriginalStr:
    print('Found')
else:
    print('not found')

# by using try except block and String.index() methods
try:
    OriginalStr.index(SubStr)
#    print('found')
except ValueError:
    print('not found')
else:
    print('found')

# by using String.find() method
if OriginalStr.find(SubStr) != -1:
    print('FOUND')
else:
    print('not found')

# By using regular expressions (REGEX)
if search(SubStr, OriginalStr):
    print('Sub str found')
else:
    print('not found')
