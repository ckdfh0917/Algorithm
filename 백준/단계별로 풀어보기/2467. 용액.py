N = int(input())
numbers = list(map(int, input().split()))

num1 = []  # 양수
num2 = []  # 음수

for i in range(N):
    if numbers[i] >= 0:
        num1.append(numbers[i])
    else:
        num2.append(numbers[i])


minV = 12345678901
left, right = 0, N-1
res = [0, 0]

while left < right:
    a = numbers[left]
    b = numbers[right]

    if abs(a + b) < minV:
        minV = abs(a+b)
        res[0] = numbers[left]
        res[1] = numbers[right]

    if a + b > 0:
        right -= 1
    else:
        left += 1

print(' '.join(map(str, res)))