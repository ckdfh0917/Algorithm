from collections import deque
N, L, R = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 연합한 국가 인구수 더하기 및 연합 나라 숫자 세기
def check():
    visited = [[0] * N for _ in range(N)]
    flag = False
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 1:
                continue
            cnt = 0
            q = deque([[i, j]])
            visited[i][j] = 1
            sumV = 0
            stack = [[i, j]]
            # 연합할 수 있는 국가 찾기
            #   - cnt : 연합한 국가 수
            #   - sumV : 연합한 국가 사람들의 합
            while q:
                x, y = q.popleft()
                cnt += 1
                sumV += arr[x][y]
                for k in range(4):
                    if 0 <= x+dx[k] < N and 0 <= y+dy[k] < N:
                        if visited[x+dx[k]][y+dy[k]] == 1:
                            continue
                        if L <= abs(arr[x][y] - arr[x+dx[k]][y+dy[k]]) <= R:
                            flag = True
                            q.append([x+dx[k], y+dy[k]])
                            stack.append([x+dx[k], y+dy[k]])
                            visited[x+dx[k]][y+dy[k]] = 1

            # 연합한 국가들 1/N 적용
            if cnt > 1:
                for x, y in stack:
                    arr[x][y] = sumV // cnt

    if flag:
        return True
    else:
        return False

res = 0
while check():
    res += 1

print(res)