A, B, C = map(int, input().split())

res = 1
temp = A
cnt = 0
while B > 0:
    if B%2==1:
        res *= temp
        res %= C

    B //= 2
    temp = (temp*temp) % C
    # print(B,res, temp)
print(res)
