N = list(map(int, input()))

N.sort(reverse=True)
print(''.join(map(str, N)))