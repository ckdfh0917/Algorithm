# << 연산자 : 피연산자의 비트열을 왼쪽으로 이동ㅅ이킴
# 1 << n : 원소가 n인 경우 n 만큼 이동

# print(1<<1)
# print(1<<2)
# print(1<<3)

# & 연산자 : 비트연산자
print(10&7)
# 10을 2진수로?
# 10은 16보다 작고 8보다 큼
# 7을 2진수로?

arr = [1,2,3]
n = 3  # arr의 원소 수

for i in range(1<<n):
    print('i :', i)
    for j in range(n):
        # print(1<<j)
        #print(i&(1<<j))
        if i & (i<<j):
            print(arr[j], end=' ')
    print()