T = int(input())

for test_case in range(1, T+1):
    cards = list(map(int, input().split()))

    v = [0] * 19
    for card in cards:
        v[card] = 1

    extra = []
    for i in range(1, 19):
        if v[i] == 0:
            extra.append(i)

    # print(extra)
    visited = [0] * 9
    cnt = 0

    def check():
        global ans_A, ans_B
        # print(visited)
        gyu = 0
        en = 0
        for i in range(9):
            for j in range(9):
                if visited[j] == i:
                    if extra[j] > cards[i]:
                        en += extra[j] + cards[i]
                    elif extra[j] < cards[i]:
                        gyu += extra[j] + cards[i]
                    break
        if gyu > en:
            ans_A += 1
        elif gyu < en:
            ans_B += 1

    def dfs(idx):
        global cnt
        if idx == 9:
            cnt += 1
            check()
            return

        for i in range(0, 9):
            if visited[i] == 0:
                visited[i] = idx
                new.append(extra[i])
                dfs(idx+1)
                visited[i] = 0
                new.pop()
    new = []
    ans_A = 0
    ans_B = 0
    dfs(1)


    print('#{} {} {}' .format(test_case, ans_A, ans_B))