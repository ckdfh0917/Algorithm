# 카운팅 정렬
# https://bowbowbow.tistory.com/8

import sys
input = sys.stdin.readline

N = int(input())

numbers = [0] * 10000
maxV = 0
for i in range(N):
    numbers[int(input())-1] += 1

for i in range(10000):
    for j in range(numbers[i]):
        print(i+1)

