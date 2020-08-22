a = []
b = [0] * 42
for i in range(10):
    a.append(int(input()))

for i in a:
    c = int(i) % 42
    b[c] += 1
    
cnt = 0
for i in b:
    if i != 0:
        cnt += 1
print(cnt)