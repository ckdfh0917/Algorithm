import sys
sys.stdin = open('input2.txt', 'r')

q = int(input())

for test_case in range(1,q+1):
    T = int(input())

    numbers = list(map(int, input().split()))

    grade = [0 for _ in range(101)]
    for i in range(len(numbers)):
        for j in range(101):
            if j == numbers[i]:
                grade[j] += 1

    max_grade = 0
    result = 0
    for i in range(101):
        if grade[i] >= max_grade:
            max_grade = grade[i]
            result = i
    print('#{} {}' .format(T, result))