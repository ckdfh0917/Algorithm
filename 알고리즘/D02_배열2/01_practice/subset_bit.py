# << 연산자 : 피연산자의 비트열을 왼쪽으로 이동ㅅ이킴
# 1 << n : 원소가 n인 경우 n 만큼 이동

print(1<<1)
print(1<<2)
print(1<<3)

# & 연산자 : 비트연산자
# 10을 2진수로?
# 10은 16보다 작고 8보다 큼
# 7을 2진수로?

arr = [1,2,3]
n = 3  # arr의 원소 수

for i in range(1<<n):
    for j in range(n):
        if i & (1<<j):
            print(arr[j], end=' ')
    print()

def getSubset(lst):
    n = len(lst)
    for i in range(1<<n): # i: 0000, 0001, 0010, 0011, 0100, 0101, 0110, 0111
        for j in range(n): # j: 0001, 0010, 0100
            t_f = i & (1 << j)
            if t_f: # t_f 가 0 이 아닌 경우에는 출력.
                print(lst[j], end=' ') # 0, 1, 2
        print()

