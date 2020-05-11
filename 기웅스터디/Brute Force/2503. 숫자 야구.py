N = int(input())
game = []

res = 0
for _ in range(N):
    numbers, s, b = map(int, input().split())
    game.append([numbers,s,b])

    num_1 = numbers[0]
    num_2 = numbers[1]
    num_3 = numbers[2]


    for i in range(1, 10):
        for j in range(1, 10):
            for k in range(1, 10):
                cnt_s = 0
                cnt_b = 0
                
                if num_1 == i:
                    cnt_s += 1
                elif num_1 == j or num_1 == k:
                    cnt_b += 1

                if num_2 == i:
                    cnt_s += 1
                elif num_2 == j or num_2 == k:
                    cnt_b += 1

                if num_3 == i:
                    cnt_s += 1
                elif num_3 == j or num_3 == k:
                    cnt_b += 1

                if s == cnt_s and b == cnt_b:
                    res += 1

print(game)
print(game[0])
print(game[0][0])
print(game[0][0][0])