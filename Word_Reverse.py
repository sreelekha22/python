# by using split() method and reversed() method

Sentence = 'split the given sentence in python way'
print(' Given sentence is : ')
print(Sentence)
words = Sentence.split(' ')
Sent_Rev = ' '.join(reversed(words))
print(' After word reverse : ')
print(Sent_Rev)

# by using slicing

Sent = ' '.join(Sentence.split(' ')[::-1])
print('by using slicing : ')
print(Sent)

# by using list

li = list(Sentence.split(' '))
li.reverse()
li1 = ' '.join(li)
print('by using list : ')
print(li1)


# Function to reverse each word in the string
def reverse_word(S, first, last):
    while first < last:
        S[first], S[last] = S[last], S[first]
        first = first + 1
        last -= 1


s = list(Sentence)
start = 0
while True:
    try:
        end = s.index(' ', start)
        reverse_word(s, start, end-1)
        start = end + 1
    except ValueError:
        reverse_word(s, start, len(s)-1)
        break
s.reverse()
s = "".join(s)
print('by using function : ')
print(s)
