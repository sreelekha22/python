def Pattern(num):
    G = ""
    for row in range(0, num):
        for column in range(0, num):
            if ((column == 1 and row != 0 and row != num - 1) or ((row == 0 or
                row == num - 1) and 1 < column < num - 2) or (row == ((num - 1) / 2)
                and num - 5 < column < num - 1) or (column == num - 2 and
                   row != 0 and row != num - 1 and row >= ((num - 1) / 2))):

                G = G + "#"
            else:
                G = G + " "
        G = G + "\n"
    return G


line = 7
print(Pattern(line))
"""
00 01 ## ## ## 05 06
10 ## 12 13 14 15 16
20 ## 22 23 24 25 26
30 ## 32 ## ## ## 36
40 ## 42 43 44 ## 46
50 ## 52 53 54 ## 56
60 61 ## ## ## 65 66
"""