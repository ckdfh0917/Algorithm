N = int(input())
game = []

for _ in range(N):
    numbers, s, b = map(int, input().split())
    game.append([numbers,s,b])

res = 0

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            temp = 0
            if i == j or j == k or k == i:
                continue
            for x in range(N):
                nums = game[x]
                n = nums[0]
                s = nums[1]
                b = nums[2]

                num_1 = n // 100
                num_2 = (n // 10) % 10
                num_3 = n % 10

                cnt_s = 0
                cnt_b = 0

                if num_1 == i:
                    cnt_s += 1
                elif num_1 == j or num_1 == k:
                    cnt_b += 1

                if num_2 == j:
                    cnt_s += 1
                elif num_2 == i or num_2 == k:
                    cnt_b += 1

                if num_3 == k:
                    cnt_s += 1
                elif num_3 == i or num_3 == j:
                    cnt_b += 1


                if s == cnt_s and b == cnt_b:
                    temp += 1
                else:
                    break
            # print(temp)
            if temp == N:
                res += 1

print(res)