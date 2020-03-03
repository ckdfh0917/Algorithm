N, M = map(int,input().split())

lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))

def bfs():
    