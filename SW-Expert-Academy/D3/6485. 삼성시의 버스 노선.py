import sys
sys.stdin = open('input.txt', 'r')

'''
입력 c1,c2,c3,c4,c5 가 버스정류장의 번호
c의 순서대로 버스가 지나가는 수를 세어야함
'''

q = int(input())


for test_case in range(1,q+1):
    N = int(input())    # 버스 노선 N 개

    station = []
    for i in range(N):
        station.append(list(map(int,input().split())))
    #print(station)
    C = []
    P = int(input())
    for i in range(P):
        C.append(int(input()))
    #print(C)
    #print(len(C))
    result = [0] * P
    for i in range(len(station)):
        for j in range(station[i][0],station[i][1]+1):
            for k in range(len(C)):
                #print('a',C[k])
                #print(i,j)
                if C[k] == j:
                    #print('c', C[k])
                    result[k] += 1
                    #print(result)
                #print()
    #print(result)
    aa = ' '.join(map(str, result))
    print('#{} {}' .format(test_case, aa))