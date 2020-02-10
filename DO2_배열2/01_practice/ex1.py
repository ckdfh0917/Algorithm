# 2 7 4 3 6
# 8 5 8 3 2
# 2 2 3 6 9
# 5 9 2 5 7
# 3 6 2 9 4

# 사방 탐색

arr = [list(map(int, input().split())) for _ in range(5)]

dx = [-1,0,1,0]     # 위, 오른, 아래, 왼
dy = [0,1,0,-1]

for i in range(len(arr)):
    print(arr[i])
print('-----------------')
result = 0
mylist = [[0 for _ in range(5)] for _ in range(5)]
for x in range(len(arr)):
    result = 0
    for y in range(len(arr[0])):
        for i in range(4):
            nextX = x + dx[i]
            nextY = y + dy[i]
            if nextX >= 0 and nextX < len(arr) and nextY >= 0 and nextY < len(arr[0]):
                result += abs(arr[nextX][nextY]-arr[x][y])
        mylist[x][y] = result
print(mylist)