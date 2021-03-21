X = [[2, 3, 4],
     [5, 6, 7]]
Y = [[1, 8],
     [9, 1],
     [3, 2]]
Z = [[0, 0],
     [0, 0]]
# iterate through rows of X
for i in range(len(X)):
    # iterate through columns of Y
    for j in range(len(Y[0])):
        # iterate through rows of Y
        for k in range(len(Y)):
            Z[i][j] += X[i][k] * Y[k][j]

for r in Z:
    print(r)

# by using zip function
# result is 3x4
result = [[sum(a * b for a, b in zip(X_row, Y_col)) for Y_col in zip(*Y)] for X_row in X]
print('result matrix is : ')
for n in result:
    print(n)
