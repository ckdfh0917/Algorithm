import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

for test_case in range(1,q+1):
    A,B,C,D = map(int,input().split())

    # A : 00, B : 01, C : 10, D : 11

    a = [['00'] * A, ['01'] * B, ['10'] * C, ['11']]
    print(a)