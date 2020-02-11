# 입력이 예시 테스트 케이스 처럼 20개씩 나눠진게 아님 -> C언어로 문제를 낸 것, 파이썬 고려안해줌
# 이 때 for문으로 20개씩 나눠서 받는게 아니라
# while으로 en()을 이용해서 N까지 input()을 받아와야함

import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

for test_case in range(1, q+1):
    arr = [False for i in range(1000)]
    num = int(input())

    numbers = []
    while True:
        numbers += list(map(int, input().split()))
        if len(numbers) == num:
            break
    # 일의 자리
    for i in numbers:
        arr[i] = True

    # 십의 자리
    for i in range(len(numbers)-1):
        num10 = numbers[i] * 10
        num1 = numbers[i+1]
        temp = num10 + num1
        arr[temp] = True

    for i in range(len(numbers)-2):
        num100 = numbers[i] * 100
        num10 = numbers[i+1] * 10
        num1 = numbers[i+2]
        temp = num100 + num10 + num1
        arr[temp] = True
    # 없는 숫자 찾기
    for i in range(len(arr)):
        if arr[i] == False:
            result = i
            break
    #print(arr)
    print('#{} {}'.format(test_case, i))