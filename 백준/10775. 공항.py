G = int(input())
P = int(input())

def make_set(x):
    p[x] = x

def find_set(x):
    if x == p[x]:
        return x
    else:
        p[x] = find_set(p[x])
        return p[x]

def union(x, y):
    py = p[find_set(y)]
    px = p[find_set(x)]
    p[py] = px


gate = []
p = [0] * (G+1)

for i in range(P):
    gate.append(int(input()))

for i in range(G+1):
    make_set(i)

cnt = 0
for i in range(P):
    idx = find_set(gate[i])
    if idx != 0:
        union(idx-1, idx)
        cnt += 1
    else:
        break

print(cnt)
