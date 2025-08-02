matrix=[list(map(int,input().split())) for _ in range(3)]

rows = len(matrix)
cols = len(matrix[0])

print("Column-wise traversal:")
for col in range(cols):
    for row in range(rows):
        print(matrix[row][col], end=" ")
