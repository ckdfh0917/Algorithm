import sys
sys.stdin = open('input.txt', 'r')

for test_case in range(1,11):
    N = int(input())

    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))

    cnt = 0
    # 1: N. 2: S
    for j in range(N):
        stack = []
        temp = 0
        for i in range(N):
            if arr[i][j] != 0:
                stack.append(arr[i][j])
        # print('s',stack)
        if stack:
            while stack[-1] == 1:
                stack.pop()
            while stack[0] == 2:
                stack.pop(0)
            for k in range(len(stack)-1):
                # print('b',k,stack[k],stack[k+1])
                if stack[k] == 1 and stack[k+1] == 2:
                    temp += 1
            cnt += temp
    print('#{} {}'.format(test_case,cnt))