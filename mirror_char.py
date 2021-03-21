# method 1 : by using zip 
original = 'abcdefghijklmnopqrstuvwxyz'
reverse =  'zyxwvutsrqponmlkjihgfedcba'
dictChars = dict(zip(original, reverse))
string = 'python'
print('given string is : ', string)
mirror = ''
for i in range(0, len(string)):
    mirror = mirror + dictChars[string[i]]

    # concat prefix and mirrored part
print('mirror string is: ', mirror)

# method 2 : by using ASCII values
alpha_rev = "zyxwvutsrqponmlkjihgfedcba"
result = ""
str1 = 'lekha'
print('Given : ', str1)
l = len(str1)
for i in range(0, l):
    result = (result + alpha_rev[ord(str1[i]) - ord('a')]);
print('mirror: ', result)
