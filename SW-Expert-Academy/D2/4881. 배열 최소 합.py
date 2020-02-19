from itertools import permutations
import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

def permute(arr):
    result = [arr[:]]
    c = [0] * len(arr)
    i = 0
    while i < len(arr):
        if c[i] < i:
            if i % 2 == 0:      # 짝수
                arr[0], arr[i] = arr[i], arr[0]
            else:               # 홀수
                arr[c[i]], arr[i] = arr[i], arr[c[i]]
            result.append(arr[:])
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
    return result

for test_case in range(1,q+1):
    N = int(input())

    arr = []
    for _ in range(N):
        arr.append(list(map(int,input().split())))
    #print(arr)
    arr = [1, 2, 3]
    new_arr = permute(arr)
    print(new_arr)