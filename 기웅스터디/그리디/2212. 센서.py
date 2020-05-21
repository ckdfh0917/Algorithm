N = int(input())
K = int(input())

sensor = sorted(list(map(int, input().split())))

print(sensor)
visited = [0] * (max(sensor) + 1)
visited[min(sensor)] = 1
visited[-1] = 1

def find(k, v):
    global ans
    if k == 0:
        print('a', v)
        arr = v[:]
        cnt = 0
        s = 0
        for i in range(min(sensor), len(arr)):
            if arr[i] == 1:
                cnt += 1
            if cnt % 2 == 1 and s == 0:
                s = i
                print('s', s)
            elif cnt % 2 == 0 and cnt != 0:
                e = i
                print(s, e)
                for j in range(s, e+1):
                    arr[j] = 1
                cnt = 0
                s = 0
        print('b', arr)
        return
    else:
        for i in range(min(sensor)+1, max(sensor)):
            if v[i] == 0 and i in sensor:
                v[i] = 1
                find(k-1, v)
                v[i] = 0

ans = 1234567891
find(K*2 - 2, visited)