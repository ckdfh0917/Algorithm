N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

cnt = N
for x in A:
    x -= B
    if x <= 0:
        continue
    if x % C == 0:
        cnt += x // C
    else:
        cnt += x // C + 1

print(cnt)