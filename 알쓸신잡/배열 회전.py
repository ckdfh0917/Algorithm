# 90 도 회전
def rotate_90(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]
    # 왜 'ret = [[0] * N] * N'과 같이 하지 않는지 헷갈리시면 연락주세요.

    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = m[r][c]
    return ret

test = [[1,2,3], [4,5,6], [7,8,9]]
print(rotate_90(test))

# [[7, 4, 1], [8, 5, 2], [9, 6, 3]] # OH yeah!!

# 180도 회전
def rotate_180(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[N-1-r][N-1-c] = m[r][c]
    return ret


test = [[1,2,3], [4,5,6], [7,8,9]]
print(rotate_180(test))


# [[9, 8, 7], [6, 5, 4], [3, 2, 1]] # OH yeah!!


def rotate_270(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[N-1-c][r] = m[r][c]
    return ret


test = [[1,2,3], [4,5,6], [7,8,9]]
print(rotate_270(test))


# [[3, 6, 9], [2, 5, 8], [1, 4, 7]] # OH yeah!!

def rotate(m, d):
    """2차원 배열을 90도 단위로 회전해 반환한다.
       이때 원 배열은 유지되며, 새로운 배열이 탄생한다. 이는 회전이 360도 단위일 때도 해당한다.
       2차원 배열은 행과 열의 수가 같은 정방형 배열이어야 한다.

       :input:
       m: 회전하고자 하는 2차원 배열. 입력이 정방형 행렬이라고 가정한다.
       d: 90도씩의 회전 단위. -1: -90도, 1: 90도, 2: 180도, ...
    """
    N = len(m)
    ret = [[0] * N for _ in range(N)]

    if d % 4 == 1:
        for r in range(N):
            for c in range(N):
                ret[c][N-1-r] = m[r][c]
    elif d % 4 == 2:
        for r in range(N):
            for c in range(N):
                ret[N-1-c][N-1-r] = m[r][c]
    elif d % 4 == 3:
        for r in range(N):
            for c in range(N):
                ret[N-1-c][r] = m[r][c]
    else:
        for r in range(N):
            for c in range(N):
                ret[r][c] = m[r][c]

    return ret