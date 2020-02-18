import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

for test_case in range(1,q+1):
    a, b = map(int, input().split())

    
    if a >= b:
        for x in range(1,100):
            for y in range(1,100):
                if a*x > b*y:
                    if a*x - b*y == 1:
                        flag = 1
                        break

            if flag == 1:
                break
