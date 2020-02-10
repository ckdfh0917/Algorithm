'''
런타임 에러
3중 포문을 썻기 때문
그래프로 풀어야 한다함
나중에 그래프 배우고 ㄱㄱㄱ

'''


import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

for test_case in range(1, q+1):
    N, M = map(int, input().split())
    cnt = 0
    a = []
    for i in range(M):
        temp = list(map(int, input().split()))
        #print(temp)
        a.append(temp)
    print('a',a)

    # a 리스트에서 3개씩 b 리스트에 저장
    b = []
    for i in range(len(a)-2):
        for j in range(i+1,len(a)-1):
            if a[i][1] == a[j][0] or a[i][1] == a[j][1] or a[i][0] == a[j][0] or a[i][0] == a[j][1]:
                for k in range(j+1,len(a)):
                    temp = []
                    temp += a[i]+a[j]+a[k]
                    #print(temp)
                    if len(set(temp)) == 3:
                        cnt += 1
    print('#{} {}'. format(test_case,cnt))

