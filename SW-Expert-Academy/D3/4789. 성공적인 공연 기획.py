import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

for test_case in range(1, q+1):
    numbers = input()
    cnt = 0
    guest = 0
    print('#{} '.format(test_case), end='')
    guest = int(numbers[0])
    for i in range(1,len(numbers)):
        #print(i,int(numbers[i]), guest+cnt)
        if i > guest + cnt:
            cnt += 1
        if i <= guest + cnt:
            guest += int(numbers[i])

    print(cnt)