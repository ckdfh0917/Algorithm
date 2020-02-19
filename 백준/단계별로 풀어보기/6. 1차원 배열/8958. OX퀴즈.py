n = int(input())

for _ in range(n):
    cnt = 0
    quiz = input()
    temp = 0
    for i in range(len(quiz)):
        if quiz[i] == 'O':
            temp += 1
            cnt += temp
        else:
            temp = 0
    print(cnt)