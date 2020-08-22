import sys
# sys.stdin.readline 으로 직접 읽어 들여오면 훨씬 빠른가봄
input = sys.stdin.readline
N = int(input())

for _ in range(N):
    a, b = map(int,input().split())

    print(a+b)