str_num = '123'
print(str_num)

print(type(str_num))    # type() : 타입확인함수
num = int(str_num)      # int() : 타입변환함수 : str -> int
print(type(num))        # type() : 타입확인함수

# 실수 변환
print(float('3.14'))
print(type(float('3.14')))

# 수를 문자로
print(str(123))     # str() : 문자열로

print('AscII a', ord('a'))
print('AscII 0', ord('0'))
print(type(ord('a')))

def atoi(s):
    num = 0
    for i in range(len(s)):
        temp = ord(s[i])
        temp -= 48
        num += (10 ** (len(s)-1-i)) * temp
    return num

s = input()
print(type(s))
# 숫자로 생긴 문자 -> 숫자로 변경하는 함수
r = atoi(s) # 문자를 입력받아서 int형으로 변환해서 리턴
print(r)
print(type(r))