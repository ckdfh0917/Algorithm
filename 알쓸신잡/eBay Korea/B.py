answer = 1234567890


def solution(num, cards):
    global answer

    for x in cards:
        if num % x == 0:
            answer = num // x

    temp = [0] * num

    def dfs(cnt, value):
        global answer
        # print(cnt, value)
        if value == num:
            answer = min(answer, cnt)
            return

        if value > num:
            return

        if cnt >= answer:
            return

        for i in range(len(cards) - 1, -1, -1):
            if value + cards[i] > num:
                continue

            if cnt == answer:
                continue
            dfs(cnt + 1, value+cards[i])

    dfs(0, 0)
    if answer == 1234567890:
        answer = -1

    return answer