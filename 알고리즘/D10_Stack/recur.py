def func(n,sum):
    if n < 0:
        print(sum)
        return
    else:
        func(n-1, sum+n)


func(10,0)

def sum2(k):
    if k == 0:
        return 0
    else:
        return k + sum2(k-1)
print(sum2(5))

# 정해진 횟수만큼 호출하기
# 호출횟수에 대한 정보를 인자로 전달
# 정해진 횟수에 다다르면 재귀호출 중단
def f(n,k):
    if n == k:
        return
    else:
        print(n)
        f(n+1,k)


f(0,5)  # n : 변하는 숫자, k : 지정한 횟수

'''
원하는 조건을 찾으면 중단하는 경우
주어진 집합에 v가 있으면 1, 없으면 0을 리턴하는 재귀함수
'''

a = [3,7,6,2,1,4,8,5]
v = 2

def find(n,k,v):
    if n == k:
        return 0
    if v == a[n]:
        return 1
    else:
        return find(n+1,k,v)

print(find(0,len(a),v))

def a(n):
    if n > 0:
        return n * a(n-1)
    return 1
print(a(10))

def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)

def fibo(n):
    if n >= 2:
        return fibo(n-1) + fibo(n-2)
    else:
        return 1

print(fibo(6))