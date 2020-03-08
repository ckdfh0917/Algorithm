N, M = map(int, input().split())
dna = [input() for _ in range(N)]

new_dna = ''
for i in range(M):
    alpabet = [0] * 26
    for j in range(N):
        alpabet[ord(dna[j][i]) - ord('A')] += 1
    new_dna += chr(ord('A') + alpabet.index(max(alpabet)))
print(new_dna)
result = 0
for i in range(N):
    for j in range(M):
        if new_dna[j] != dna[i][j]:
            result += 1
print(result)