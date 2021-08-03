arr = []
for i in range(5):
  arr.append([int(j) for j in input().split()])
row = column = 0
for i in range(5):
  for j in range(5):
    if (arr[i][j]==1):
        row = i
        column = j
print(abs(row-2) + abs(column-2))