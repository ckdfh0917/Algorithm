import sys
sys.stdin = open('input.txt', 'r')


for test_case in range(1,11):
    q = int(input())

# 현 위치에서 갈 수 있는 위치를 스택에 쌓고
# pop을 하면서 이동하고 방문표시함
# 이동을 하면서 3을 찾는다