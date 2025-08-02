matrix=[list(map(int,input().split())) for _ in range(3)]

n = len(matrix)

print("Anti Diagonal:")
for i in range(n):
    print(matrix[i][n - 1 - i], end=" ")

