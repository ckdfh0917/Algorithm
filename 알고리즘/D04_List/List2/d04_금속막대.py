'''
남는 나사가 없다 -> 모든 나사를 연결할 수 있다
'''

import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

for test_case in range(1,q+1):
    num = int(input())

    temp = list(map(int, input().split()))
    print('#{} ' .format(test_case), end='')
    #print(volt)
    volt = []
    for i in range(len(temp)//2):
        volt += [[temp[2*i],temp[2*i+1]]]

    #print(volt)
    res = []
    k = len(volt)
    i = 0
    flag = 0
    while k > 1:

        k = len(volt)
        #print(k)
        point = 0

        for j in range(len(volt)):
            #print('i',i,'j',j)
            #print(volt[i][-1],volt[j][0])
            if volt[i][-1] == volt[j][0]:
                res = volt[i] + volt[j]
                #print(res)
                if i < j:
                    volt.pop(j)
                    volt.pop(i)
                else:
                    volt.pop(i)
                    volt.pop(j)
                volt.append(res)
                #print(volt)
                k = len(volt)
                i = 0
                point = 1
                break
        if point == 1:
            i = 0
        else:
            i += 1
    print(' '.join(map(str,volt[0])))