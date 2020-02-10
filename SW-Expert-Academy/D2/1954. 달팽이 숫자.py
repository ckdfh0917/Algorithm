import sys
sys.stdin = open('input.txt', 'r')

q = int(input())
for test_case in range(1, q+1):
    num = int(input())
    snail_list = [[0 for _ in range(num)] for _ in range(num)]
    print('#{}' .format(test_case))

    #print(snail_list)
    x , y = 0, -1
    k = 1

    for i in range(num):
        for _ in range(num):
            y += 1
            #print('x {} y {}'.format(x, y))
            snail_list[x][y] = k
            k += 1
        #print()
        for _ in range(num-1):
            x += 1
            #print('x {} y {}'.format(x, y))
            snail_list[x][y] = k
            k += 1
        #print()
        for _ in range(num-1):
            y -= 1
            #print('x {} y {}'.format(x, y))
            snail_list[x][y] = k
            k += 1
        #print()
        for _ in range(num-2):
            x -= 1
            #print('x {} y {}'.format(x, y))
            snail_list[x][y] = k
            k += 1
        #print()
        num -= 2
    #print()
    snail_str = str(snail_list)
    snail_str = snail_str.replace('[[', '')
    snail_str = snail_str.replace('], [', '\n')
    snail_str = snail_str.replace(',', '')
    snail_str = snail_str.replace(']', '')
    snail_str = snail_str.replace('[', '')

    print(snail_str)