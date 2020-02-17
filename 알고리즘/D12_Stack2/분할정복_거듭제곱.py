# 거듭제곱 : 반복문
# def power(base, exponent):
#     if base == 0:
#         return 1
#     result = 1
#     for _ in range(exponent):
#         result *= base
#     return result
#
# print(power(2,10))

# 분할정복
'''
C^8 = C^4 * C^4         # 짝수
C^9 = C 4 * C^4 * C     # 홀수
'''
def power2(base, exponent):
    if base == 0 or exponent == 0:
        return 1
    elif exponent % 2 == 0:
        newbase = power2(base,exponent/2)
        return newbase * newbase
    elif exponent % 2 == 1:
        newbase = power2(base,(exponent-1)/2)
        return newbase * newbase * base

print(power2(2,10))