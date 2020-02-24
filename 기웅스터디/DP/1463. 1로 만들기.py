num = int(input())
arr = [i for i in range(num+1)]
DP = [0] * (num+1)

for i in range(2,num+1):
    if i % 3 == 0:
        DP[i] = DP[i//3] + 1
    elif i % 2 == 0:
        if DP[i-1] < DP[i//2]:
            DP[i] = DP[i-1] + 1
        else:
            DP[i] = DP[i//2] + 1
    else:
        DP[i] = DP[i-1] + 1
    # print('i',i,DP[i])
# print(arr)
print(DP[num])


