# 문자열 비교함수
# 맞으면 1, 아니면 0을 리턴
def f(s1, s2):
    if len(s1) == len(s2):
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                return 0
        return 1
    else:
        return 0

# 두 문자열 비교
s1 = input()
s2 = input()

if s1 == s2:        # == 연산자를 이용해서 문자열 비교
    print(1)
else:
    print(0)