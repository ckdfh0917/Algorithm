N = int(input())

n = 666
cnt = 0
while True:
    n = str(n)
    if '666' in n:
        cnt += 1

    if cnt == N:
        print(n)
        break
    else:
        n = int(n) + 1