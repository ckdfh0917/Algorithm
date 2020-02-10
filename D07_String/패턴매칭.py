p = 'is'    # 찾을 패턴
t = 'This is a book~!'  # 전체 텍스트
M = len(p)  # 찾을 패턴의 길이
N = len(t)  # 전체 텍스트의 길이

def BruteFocce(p, t):
    i = 0   # t의 인덱스
    j = 0   # p의 인덱스
    while j < M and i < N:
        if t[i] != p[j]:
            i -= j
            j -= 1
        i += 1
        j += 1
    if j == M: return i
    else: return -1

