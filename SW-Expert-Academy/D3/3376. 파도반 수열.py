# 처음에 재귀로 짜서 예시 테스트케이스는 맞았으나
# 제한시간 초과가 뜸
# 그래서 직접 리스트에 추가하는 방식으로 함

import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

def f(n):
    tri = [1,1,1,2,2,3,4]

    if n < 7:
        return tri[n-1]
    else:
        return f(n-5) + f(n-1)

def a(n):
    tri = [1,1,1,2,2,3,4]
    if n > 7:
        for i in range(7,n):
            tri.append(tri[i-5]+tri[i-1])
    return tri[n-1]

#result = []
for test_case in range(1,q+1):
    N = int(input())
    arr = a(N)
    print('#{} {}' .format(test_case,arr))

#     result += '#' + str(test_case) + ' ' + str(f(N)) + '\n'
# print(''.join(result))

