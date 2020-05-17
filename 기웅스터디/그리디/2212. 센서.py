N = int(input())
K = int(input())

sensor = sorted(list(map(int, input().split())))

print(sensor)
visited = [0] * max(sensor)
# visited[0] = 1
# visited[-1] = 1

def find(k, v):
    global ans
    if k == 0:
        print(v)
        for i in range(len(v)):
            if v[i] == 1:
                pass
        return
    else:
        for i in range(min(sensor)+1, max(sensor)):
            print('aaa', i)
            if v[i] == 0 and i in sensor:
                print('bbb', i)
                v[i-1] = 1
                find(k-1, v)
                v[i-1] = 0

ans = 1234567891
find(K*2 - 2, visited)