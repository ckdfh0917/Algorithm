import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

for test_case in range(1, q+1):
    N, K = map(int, input().split())

    grade = list(map(int, input().split()))
    grade.sort()
    grade.reverse()

    #print(grade)

    sum = 0
    for i in range(K):
        sum += grade[i]
    print('#{} {}' .format(test_case,sum))