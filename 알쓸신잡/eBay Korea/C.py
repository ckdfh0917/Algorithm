answer = 1234567890


def solution(num, cards):
    global answer

    for x in cards:
        if num % x == 0:
            answer = num // x

    temp = []

    def dfs(cnt):
        global answer
        if sum(temp) == num:
            answer = min(answer, cnt)
            return

        if sum(temp) > num:
            return

        if cnt >= answer:
            return

        for i in range(len(cards) - 1, -1, -1):
            if sum(temp) + cards[i] > num:
                continue

            if cnt == answer:
                continue
            temp.append(cards[i])
            dfs(cnt + 1)
            temp.pop()

    dfs(0)
    if answer == 1234567890:
        answer = -1

    return answer