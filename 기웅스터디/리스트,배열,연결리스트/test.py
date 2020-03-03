N, K = map(int, input().split())

lst = ['?'] * N
apb = [False] * 26
idx = 0
for _ in range(N):
    S, K = map(str, input().split())
    S = int(S)

    idx = (idx + S) % N
    # print(apb)
    if lst[idx] == '?':
        if not apb[ord(K) - ord('A')]:
            apb[ord(K) - ord('A')] = True
            lst[idx] = K
        else:
            print('!')
            break
    else:
        if lst[idx] != K:
            print('!')
            break
else:
    # print(lst)
    for i in range(idx+1):
        temp = lst.pop(0)
        lst.append(temp)
    # print(lst)
    lst.reverse()
    print(''.join(lst))


