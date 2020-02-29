N = int(input())

Q = [i for i in range(1,N+1)]

while len(Q) > 1:
    Q.pop(0)    # 제일 위에 있는 카드 바닥에 버리기
    temp = Q.pop(0)
    Q.append(temp)

print(Q[0])