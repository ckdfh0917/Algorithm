l, w, h = map(int, input().split())
n = int(input())

cube = [0] * 25
for _ in range(n):
    a, b = map(int, input().split())
    cube[a+1] = b

# print(cube)
cube.sort(reverse=True)
# print(cube)
vol = l * w * h
cnt = 0
flag = 0
for i in range(n):
    if l >= 2**cube[i][0] and w >= 2**cube[i][0] and h >= 2**cube[i][0]:
        while cube[i][1] > 0:
            print(vol, cube)
            if vol - (2 ** cube[i][0]) ** 3 < 0:
                break
            elif vol - (2 ** cube[i][0])**3 == 0:
                flag = 1
                cnt += 1
                break
            else:
                vol -= (2 ** cube[i][0]) ** 3
                cube[i][1] -= 1
                cnt += 1
    if flag == 1:
        break
if flag == 1:
    print(cnt)
else:
    print(-1)