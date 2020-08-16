N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

def confirmX(n):
    visited = [0] * N
    preH = arr[n][0]
    idx = 1
    while idx < N:
        if preH == arr[n][idx]:
            idx += 1
            continue
        elif preH == arr[n][idx] + 1:
            cnt = 0
            while cnt != L:
                if idx+cnt >= N:
                    return False
                if visited[idx+cnt] == 1:
                    return False
                if preH == arr[n][idx + cnt] + 1:
                    visited[idx+cnt] = 1
                    cnt += 1
                    continue
                else:
                    return False
            idx += L - 1
            preH = arr[n][idx]
        elif preH == arr[n][idx] - 1:
            nextH = arr[n][idx]
            cnt = 1
            while cnt != L+1:
                if idx-cnt < 0:
                    return False
                if visited[idx-cnt] == 1:
                    return False
                if arr[n][idx - cnt]+1 == nextH:
                    visited[idx-cnt] = 1
                    cnt += 1
                    continue
                else:
                    return False
            preH = arr[n][idx]
            idx += 1
        else:
            return False

    if idx > N:
        return False
    elif idx == N:
        return True

def confirmY(n):
    visited = [0] * N
    preH = arr[0][n]
    idx = 1
    while idx < N:
        if preH == arr[idx][n]:
            idx += 1
            continue
        elif preH == arr[idx][n] + 1:
            cnt = 0
            while cnt != L:
                if idx+cnt >= N:
                    return False
                if visited[idx+cnt] == 1:
                    return False
                if preH == arr[idx + cnt][n] + 1:
                    visited[idx+cnt] = 1
                    cnt += 1
                    continue
                else:
                    return False
            idx += L - 1
            preH = arr[idx][n]
        elif preH == arr[idx][n] - 1:
            nextH = arr[idx][n]
            cnt = 1
            while cnt != L+1:
                if idx-cnt < 0:
                    return False
                if visited[idx-cnt] == 1:
                    return False
                if arr[idx - cnt][n]+1 == nextH:
                    visited[idx-cnt] = 1
                    cnt += 1
                    continue
                else:
                    return False
            preH = arr[idx][n]
            idx += 1
        else:
            return False

    if idx > N:
        return False
    elif idx == N:
        return True


ans = 0
for i in range(N):
    if confirmX(i):
        ans += 1
for i in range(N):
    if confirmY(i):
        ans += 1
print(ans)