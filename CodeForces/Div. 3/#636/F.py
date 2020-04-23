t = int(input())

for _ in range(t):
    n = int(input())
    result = []
    for i in range(n-1):
        num = list(map(int, input().split()))
        k = num[0]

        # 순서를 조작해야함



        for j in range(1, len(num)):
            if num[j] not in result:
                result.append(num[j])
    print(' '.join(map(str, result)))
