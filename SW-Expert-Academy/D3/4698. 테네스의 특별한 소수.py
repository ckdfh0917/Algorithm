import sys
sys.stdin = open('input.txt', 'r')

# https://wikidocs.net/21638
# 에라토스테네스의 소수
# 1. 2를 제외한 모든 2의 배수를 False
# 2. 3을 제외한 모든 3의 배수를 False
# 3. 4는 2의 배수로 False 이므로 제외
# 4. 5를 제외한 모든 5의 배수를 False
#
#
# 원하는 숫자까지 반복

q = int(input())

def sosu():
    temp = [False, False] + [True] * (999999)
    print(temp)
    a = []
    for i in range(2,1000001):
        if temp[i]:     # temp[i] 가 False 이면 조건 성립 안함
            a.append(i)
            for j in range(2*i, 1000001, i):
                temp[j] = False
    return a

SS = sosu()
#print(SS)

for test_case in range(1, q + 1):
    D, A, B = map(int, input().split())

    K = str(D)
    cnt = 0
    for i in range(len(SS)):
        if A <= SS[i] <= B:
            a = str(SS[i])
            #print(len(a))
            for j in range(len(a)):

                if K == a[j]:
                    #print(a)
                    cnt += 1
                    break
    print('#{} {}' .format(test_case,cnt))