import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

for test_case in range(1,q+1):
    N, K = map(int, input().split())    # N: 총 사람수
                                        # K: 제출한 사람수
    student = list(map(int,input().split()))

    #print(student)
    res = [0] * N
    for i in range(len(student)):
        res[student[i]-1] = 1
    #print(res)
    result = []
    for i in range(len(res)):
        if res[i] == 0:
            result.append(i+1)
    result = ' '.join(map(str, result))
    print('#{} {}'.format(test_case,result))