T = int(input())

for test_case in range(1, T+1):
    card = list(map(int, input().split()))
    print('#{} '.format(test_case), end='')
    player1 = [0] * 10
    player2 = [0] * 10
    # player1_staus = 0
    # player2_staus = 0
    for i in range(6):
        player1[card[i*2]] += 1
        player2[card[i*2+1]] += 1

        player1_staus = 0
        player2_staus = 0
        # run 판별
        for k in range(8):
            if player1[k] != 0 and player1[k + 1] != 0 and player1[k + 2] != 0:
                player1_staus += 1
            if player2[k] != 0 and player2[k + 1] != 0 and player2[k + 2] != 0:
                player2_staus += 1

        # triple 판별
        for k in range(10):
            if player1[k] >= 3:
                player1_staus += 1
            if player2[k] >= 3:
                player2_staus += 1

        if player1_staus != 0 and player1_staus >= player2_staus:
            print(1)
            break
        elif player1_staus < player2_staus:
            print(2)
            break
    if player1_staus == 0 and player2_staus == 0:
        print(0)
