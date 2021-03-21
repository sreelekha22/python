import re
# \d	Returns a match where the string contains digits (numbers from 0-9)

sentence = "There are 1210 people in this city-1, 1587 in the city-2 and 1877 in the city-3."
occ = re.findall("\d+", sentence)

num_list = map(int, occ)

print(max(num_list))

# num_list = map(int, occ)
# print(list(num_list))

"""
RegEx is a sequence of characters that forms a search pattern.
RegEx can be used to check if a string contains the specified search pattern.

function     Description
findall	     Returns a list containing all matches
search	     Returns a Match object if there is a match anywhere in the string
split	     Returns a list where the string has been split at each match
sub	         Replaces one or many matches with a string
"""
