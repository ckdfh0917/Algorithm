S = list(input())
N = int(input())

arr = [[] for x in range(26)]
dp = [0] * 111

for _ in range(N):
    ss = input()
    x = ord(ss[-1]) - ord('a')
    arr[x].append(ss)

dp[len(S)] = True
# print(arr)

for i in range(len(S)-1, -1, -1):
    # print('cc', i+1, dp)
    if not dp[i+1]: continue

    now = ord(S[i]) - ord('a')
    for it in arr[now]:

        L = len(it)

        To = i - L + 1
        if To < 0: continue

        ok = True
        for j in range(L):
            # print(S[i-j], it[L-1 - j])
            if S[i-j] != it[(L-1) - j]:
                ok = False
                break
        # print()
        if ok: dp[To] = True
    # print('eeee', dp)
if dp[0] == True:
    print(1)
else:
    print(0)