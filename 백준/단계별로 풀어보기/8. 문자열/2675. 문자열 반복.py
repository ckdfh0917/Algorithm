N = int(input())
for test_case in range(N):
    num, munja = map(str, input().split())
    num = int(num)
    res = ''
    for i in range(len(munja)):
        res += munja[i] * num

    print(res)