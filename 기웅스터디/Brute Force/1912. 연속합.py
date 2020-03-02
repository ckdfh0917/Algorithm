n = int(input())
numbers = list(map(int, input().split()))
max_V = 0
for i in range(1,n+1):  # i 씩 더하기
    for j in range(n-i+1):  #
        print('a',i,j, end=' ')
        temp = 0
        for k in range(j,j+i):
            temp += numbers[k]
        print('t',temp)
        max_V = max(temp, max_V)

print(max_V)