matrix=[list(map(int,input().split())) for _ in range(3)]

n = len(matrix)

print("Main Diagonal:")
for i in range(n):
    print(matrix[i][i], end=" ")
