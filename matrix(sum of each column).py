matrix=[list(map(int,input().split())) for _ in range(3)]

rows = len(matrix)
cols = len(matrix[0])

for col in range(cols):
    col_sum = 0
    for row in range(rows):
        col_sum += matrix[row][col]
    print(f"Sum of column {col+1}: {col_sum}")
