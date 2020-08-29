def dfs(cnt, answer):
    print(cnt, temp, answer)
    if sum(temp) == num:
        print('aaa', answer)
        answer = min(answer, cnt)
        return

    if sum(temp) > num:
        return

    if cnt > answer:
        return

    for i in range(len(cards)):
        temp.append(cards[i])
        dfs(cnt + 1, answer)
        temp.pop()



temp = []
num = 8
cards = [1,4,6]
dfs(0, 1234567890)


11
4