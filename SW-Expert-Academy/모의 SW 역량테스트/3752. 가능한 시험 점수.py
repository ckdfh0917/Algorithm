
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    data = tuple(map(int,input().split()))
    res = []
    score = [0]*(sum(data)+1)
    score[0] = 1
    for j in range(N) :
        for i in range(sum(data), -1, -1) :
            if score[i] :
                score[data[j]+i] = 1
    # print(score)
    print("#{} {}".format(test_case, sum(score)))
