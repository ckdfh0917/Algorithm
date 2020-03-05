q = int(input())

def dfs(n, lst):
    print('=============================')
    print(n)
    visited[n] = True
    print(visited)
    for i in range(N):
        if not used[i]:
            print('b', n, grade[i], n+grade[i])
            n += grade[i]
            used[i] = True
            print('a',used)
            if not visited[n] and lst != used:
                dfs(n, used)
                n -= grade[i]
                used[i] = False
            else:
                n -= grade[i]
                used[i] = False
    return

for test_case in range(1, q+1):
    N = int(input())
    grade = list(map(int, input().split()))
    used = [False] * len(grade)
    visited = [False] * (sum(grade) + 1)
    dfs(0, used)
    print(visited)
    # print(res)
    print('#{} {}'.format(test_case,visited.count(True)))

# T = int(input())
# for test_case in range(1, T+1):
#     N = int(input())
#     data = tuple(map(int,input().split()))
#     res = []
#     score = [0]*(sum(data)+1)
#     score[0] = 1
#     for j in range(N) :
#         for i in range(sum(data), -1, -1) :
#             if score[i] :
#                 score[data[j]+i] = 1
#     print(score)
#     print("#{} {}".format(test_case, sum(score)))