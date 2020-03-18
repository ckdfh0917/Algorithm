card = list(input())
P = [1] + [0] * 13
K = [1] + [0] * 13
H = [1] + [0] * 13
T = [1] + [0] * 13

flag = 0
for i in range(0,len(card),3):
    # print(card[i],card[i+1],card[i+2])
    if card[i] == 'P':
        temp = int(card[i+1]) * 10
        temp += int(card[i+2])
        if P[temp] == 1:
            flag = 1
            break
        P[temp] = 1
    elif card[i] == 'K':
        temp = int(card[i+1]) * 10
        temp += int(card[i+2])
        if K[temp] == 1:
            flag = 1
            break
        K[temp] = 1
    elif card[i] == 'H':
        temp = int(card[i+1]) * 10
        temp += int(card[i+2])
        if H[temp] == 1:
            flag = 1
            break
        H[temp] = 1
    elif card[i] == 'T':
        temp = int(card[i+1]) * 10
        temp += int(card[i+2])
        if T[temp] == 1:
            flag = 1
            break
        T[temp] = 1

if flag == 1:
    print('GRESKA')
else:
    print(P.count(0), K.count(0), H.count(0), T.count(0))