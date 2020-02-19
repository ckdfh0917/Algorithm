# H, M = map(int, input().split())

# if M - 45 < 0:
#     H -= 1
#


def f(x):
    m = 0
    for i in range(1, x):
        if x >= i ** 2:
            m = i
    n = m + 1
    k = m
    while True:
        if x == k**2:
            return k
        elif round(m,3) == round(n,3):
            return round(m,3)

        k = (m+n) / 2
        if x > k**2:
            m = k
            k = (n+k) / 2
        elif x < k**2:
            n = k
            k = (m+k) / 2



print(f(2))

#
# def calc(a, b):
#     c1 = a + b
#     c2 = a - b
#     c3 = a * b
#     try:
#         c1 = a + b
#         c2 = a - b
#         c3 = a * b
#         c4 = a / b
#         return c1, c2, c3, c4
#     except ZeroDivisionError:
#         print('0으로 나눌 수 없습니다.')
#
# def my_sum(a, b):
#     return a+b
#
# def my_sub(a, b):
#     return a-b
#
# def my_mul(a, b):
#     return a*b
#
# def my_div(a, b):
#     try:
#         return a/b
#     except ZeroDivisionError:
#         print('0으로 나눌 수 없습니다.')
#
#
# print(my_div(10,0))
