N = int(input())

def find(N):
    result = N
    for temp in range(N,-1,-1):
        res = 0
        k = temp
        while temp >= 1:
            a = temp % 10
            temp = temp // 10

            res += a
            # print('a',res, a)
        # print(res, k, N)
        res += k
        if res == N:
            result = min(result, k)
    if result == N:
        return print(0)
    else:
        return print(result)

find(N)