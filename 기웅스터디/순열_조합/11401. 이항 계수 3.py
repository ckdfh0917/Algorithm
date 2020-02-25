# 큰수를 제곱수를 2**n 으로 나누어 생각하기
# mod를 O(N) 사용하는 것에 비해 이는 O(lonN)

N, K = map(int, input().split())
p = 1000000007
def factorial(a, b):
    result = 1
    for i in range(a, b+1):
        result *= i % 1000000007
        result %= 1000000007
        # print(i, result)
    return result

def combination(n, k):
    result = (factorial(n-k+1, n) * res) % p
    return result

temp = factorial(1, K)
res = 1
q = p-2
# print('t',temp)
while q > 0:
    if q % 2 == 1:
        res *= temp
        res %= p
    q //= 2
    temp = (temp * temp) % p

print(combination(N, K))
