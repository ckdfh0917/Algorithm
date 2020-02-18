from itertools import permutations
import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

def ss(N):
    arr = []

    for i in range(N):
        


for test_case in range(1,q+1):
    N = int(input())

    arr = []
    for _ in range(N):
        arr.append(list(map(int,input().split())))
    #print(arr)

    min_V = 0
    min_I = 0
    visited = [0] * N
    for i in range(N):
        if min_V > arr[0][i]:
            min_V = arr[0][i]
            min_I = i
    visited[i] = 1