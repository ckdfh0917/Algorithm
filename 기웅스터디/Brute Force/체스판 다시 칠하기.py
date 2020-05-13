N, M = map(int, input().split())

chess = [input() for _ in range(N)]

for i in range(N):
    print(chess[i])

new_chess =[]

print(chess)

for i in range(0,N-8+1):
    for j in range(0,M-8+1):
        print('ii', i, j)
        print('cc', chess[i][j:j+8])
        for k in range(8):
            new_chess.append(chess[i+k][j:j+8])
        print('nn', new_chess)

        for k in range(8):
            print('99', new_chess[k])


            zzzz