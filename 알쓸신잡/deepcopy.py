import copy

N = 8
temp = [list(map(int, input().split())) for _ in range(N)]
arr = copy.deepcopy(temp)

arr2 = [temp[i][:] for i in range(N)]