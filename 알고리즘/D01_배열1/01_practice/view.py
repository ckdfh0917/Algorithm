# 디버깅용 시험 제출시 제거
import sys
sys.stdin = open('input.txt','r')            # 표준입력을 콘솔창에서 파일로 변경

q = 10

for test_case in range(1, q + 1):
    N = int(input())
    h = list(map(int, input().split()))
    view = 0

    for i in range(2, N - 2):
        #left = h[i - 2] if (h[i - 2] > h[i - 1]) else h[i - 1]
        #right = h[i+1] if (h[i+1] > h [i+2]) else h[i+2]
        # t = left if (left > right) else right

        t = max(h[i-2],h[i-1],h[i+1],h[i+2])

        if(h[i] > t):
            view = view + h[i] - t
    print('#{} {}'.format(test_case, view))