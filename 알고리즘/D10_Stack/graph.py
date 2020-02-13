'''
그래프

비선형 자료 구조
그래프 G는 (V,E)의 쌍이다
    V : 정점의 집합
    E : 간선의 집합
    정점은 독립된 개체로 동그라미로 표현
    간선은 두 정점을 이어주는 개체로 선이나 화살표가 있는 선을 표현
    선 : 무방향 그래프
    화살표 : 방향 그래프

인접
     u, v라는 간선이 있다면 정점 u와 정점 v가 인접하다(연결되어있다)

그래프의 표현
    인접행렬로 표현
        크기가 V * V인 행렬
        두 정점 i,j 를 잇는 간선이 있다면 인접행렬의 i,j는 1, 아니면 0

    무방향 그래프
        양방향으로 간선이 존재한다는 의미이므로 대칭행렬
    방향 그래프
        대칭 아님
'''
n, m = map(int, input().split())

arr = [[0] * n for _ in range(n)]

line = list(map(int, input().split()))

for k in range(0,len(line),2):
    arr[line[k]-1][line[k+1]-1] = 1
    arr[line[k+1]-1][line[k]-1] = 1

for i in range(m-1):
    print(arr[i])
