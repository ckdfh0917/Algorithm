T = int(input())

for _ in range(T):
    n, m, k = map(int, input().split())
    result = 0
    card = n // k

    player = [0] * k
    if m == 0:
        result = 0
    elif card >= m:
        result = m
    elif card < m:
        player[0] = card
        m -= card
        while m > 0:
            for i in range(1, k):
                player[i] += 1
                m -= 1
                if m == 0:
                    break
        result = player[0] - player[1]
    print(result)
