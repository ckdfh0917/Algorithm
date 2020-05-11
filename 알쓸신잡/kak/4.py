dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
res1, res2 = 1234567891, 1234567891
answer = 12345678901

def dfs(board, visited, x, y, k, cnt1, cnt2, d):
    global res1, res2, answer
    if x == k - 1 and y == k - 1:
        temp = cnt1 * 100 + cnt2 * 500
        if answer > temp:
            # print(temp)
            answer = temp
            res1 = cnt1
            res2 = cnt2
        return
    elif cnt2 > res2 and cnt1 > res1:
        return
    elif cnt1 * 100 + cnt2 * 500 >= answer:
        return
    else:
        for i in range(4):
            if 0 <= x + dx[i] < k and 0 <= y + dy[i] < k:
                if board[x + dx[i]][y + dy[i]] == 0 and visited[x + dx[i]][y + dy[i]] == 0:
                    visited[x + dx[i]][y + dy[i]] = 1
                    if d == i:
                        dfs(board, visited, x + dx[i], y + dy[i], k, cnt1 + 1, cnt2, i)
                    else:
                        dfs(board, visited, x + dx[i], y + dy[i], k, cnt1 +1, cnt2 + 1, i)
                    visited[x + dx[i]][y + dy[i]] = 0

def solution(board):
    k = len(board[0])
    visited = [[0] * k for _ in range(k)]

    for i in range(4):
        if 0 <= dx[i] < k and 0 <= dy[i] < k:
            if board[dx[i]][dy[i]] == 0:
                dfs(board, visited, 0, 0, k, 0, 0, i)
    return answer

# print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))