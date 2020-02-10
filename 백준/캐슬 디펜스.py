'''
N * M
각 칸에 최대 적 하나
성벽은 N+1번 행 모든 칸
성벽에 궁수 3명  -->> M 칸에서 3명
궁수 3명을 i1, i2, i3 라 하면

i1 : 0 ~ M-3
i2 : i1 ~ M-2
i3 : i2 ~ M-1

화살을 맞는 사람 수를 리턴하는 함수

1. 궁수의 자리를 구하는 함수

궁수는 한번에 한발
거리는 D이하인 적중 가장 가까운 적을 공격 가능

거리가 같은 경우는 가장 왼쪽 사람을 공격
한명의 적을 여러 궁수에게 맞을 수 있음
죽은 적의 위치를 바로 지워버리면 안됨 -> 다른 궁수가 또 공격할 수 있기 때문에

궁수의 공격이 한턴 끝나면 적이 한칸 내려옴

거리가 D이내이면서 가장 가까운 적을 공격하는 방법
거리는 몇 칸 이동해야 만나냐 라고 생각하면됨

탐색을 위에서 내려오거나 아래에서 올라가거나
'''
def shoot(s, target, N, M, D):
    pass


def defence(s1, s2, s3, N, M, D):
    target = [[0]*M for _ in range(N)]  # 실제 사격해볼 적의 위치
    cnt = 0
    for i in range(N):
        for j in range(M):
            target[i][j] = enemy[i][j]
    for _ in range(N): # 사격을 반복하는 횟수
        shoot(s1, target, N, M, D)
        shoot(s2, target, N, M, D)
        shoot(s3, target, N, M, D)

        for i in range(N):
            for j in range(M):
                if target[i][j] > 0:
                    cnt += 1

    return cnt

# 입력 받기
N, M, D = map(int, input().split())
enemy = [list(map(int, input().split())) for _ in range(N)]

maxV = 0
# value, index 값 구분해서 명명하기
for i1 in range(M-2):   #맨 왼쪽 궁수
    for i2 in range(i1+1, M-1): #가운데 궁수
        for i3 in range(i2+1, M):   #오른쪽 궁수
            kill = defence(i1,i2,i3, N, M, D)
            if maxV < kill:
                maxV = kill


print(enemy)