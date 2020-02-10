import sys
sys.stdin = open('input2.txt', 'r')

q = int(input())

for test_case in range(1,q+1):
    munja = input()
    length = len(munja)
    # 첫줄
    for _ in range(length):
        print('..#.', end='')
    print('.')
    # 둘째줄
    for _ in range(length):
        print('.#.#', end='')
    print('.')
    # 셋째줄
    ###
    for i in range(length):
        print('#.{}.' .format(munja[i]), end='')
    print('#')
    ###
    # 넷째줄
    for _ in range(length):
        print('.#.#', end='')
    print('.')
    # 다섯째줄
    for _ in range(length):
        print('..#.', end='')
    print('.')