n, c = map(int, input().split())

home = []
for _ in range(n):
    home.append(int(input()))
home.sort()
# print(home)
def possi(a):
    cnt = 0
    pre = -10 ** 9
    for i in range(n):
        now = home[i]
        if now-pre >= a:
            cnt += 1
            pre = now
    if cnt >= c:
        print('t', c)
        return True
    print('f', c)
    return False

s = 0
e = 10 ** 9
ans = 0

while s <= e:
    mid = (s+e) // 2
    print('m', s, mid, e)
    if possi(mid):
        ans = mid
        s = mid + 1
    else:
        e = mid - 1
    print('a', ans)
print(ans)