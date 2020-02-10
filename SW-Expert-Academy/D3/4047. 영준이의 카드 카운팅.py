import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

for test_case in range(1, q+1):
    temp = list(input())
    cards = []
    print('#{} ' .format(test_case), end='')
    for i in range(0,len(temp),3):
        cards += temp[i]
        cards += [temp[i+1] + temp[i+2]]
    #print(cards)

    # S,D,H,C 0으로 초기화
    S = [0] * 13
    D = [0] * 13
    H = [0] * 13
    C = [0] * 13
    for i in range(len(cards)):
        if i % 2 == 0:
            if cards[i] == 'S':
                S[int(cards[i+1])-1] += 1
            elif cards[i] == 'D':
                D[int(cards[i+1])-1] += 1
            elif cards[i] == 'H':
                H[int(cards[i+1])-1] += 1
            elif cards[i] == 'C':
                C[int(cards[i+1])-1] += 1
    # count, flag 초기화
    cntS,cntD,cntH,cntC,flag = 0,0,0,0,0
    for i in range(len(S)):
        if S[i] > 1:
            print('ERROR')
            flag = 1
            break
        elif S[i] == 0:
            cntS += 1
    for i in range(len(D)):
        if D[i] > 1:
            print('ERROR')
            flag = 1
            break
        elif D[i] == 0:
            cntD += 1
    for i in range(len(H)):
        if H[i] > 1:
            print('ERROR')
            flag = 1
            break
        elif H[i] == 0:
            cntH += 1
    for i in range(len(C)):
        if C[i] > 1:
            print('ERROR')
            flag = 1
            break
        elif C[i] == 0:
            cntC += 1
    if flag == 1:
        continue
    print('{} {} {} {}' .format(cntS,cntD,cntH,cntC))