num = int(input())
arr = [i for i in range(num+1)]
DP = [0] * (num+1)

for i in range(2,num+1):
    DP[i] = DP[i - 1] + 1
    if i % 3 == 0:
        DP[i] = min(DP[i], DP[i // 3] + 1)
    elif i % 2 == 0:
        DP[i] = min(DP[i], DP[i // 2] + 1)
print(DP[num])
