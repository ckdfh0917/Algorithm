q = int(input())

for _ in range(q):
    lst = list(map(int, input().split()))
    a, b = lst[0], lst[1]
    if a == b:
        print(0)
    elif a < b:
        if (b-a) % 2 == 0: # 짝수 차이면
            print(2)
        else:    # 홀수 차이면
            print(1)
    elif a > b:
        if (a-b) % 2 == 1:  # 홀수 차이면
            print(2)
        else:
            print(1)