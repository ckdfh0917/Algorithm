# 방법1

s = 'Revesr this string'
s_rev = ''
for ch in s:
    #print(ch)
    s_rev = ch + s_rev
    #print(s_rev)

# 방법2
s = 'Reverse this string'
s_list = list(s)        # 문자열을 리스트로
s_list.reverse()        # 리스트 메소드 : reverse // str은 reverse 못함
#print(s_list)
#print(''.join(s_list))

# 방법3
s = 'Reverse this string'
ss = reversed(s)
#print(reversed(s))

# 슬라이싱 사용
s = 'Reverse this string'
# print(s[:])     # 모든 문자열
# print(s[0:3])   # 시작 구간에서 끝 구간까지 +1씩
# print(s[3:0:-1])    # 끝 구간에서 시작까지 -1씩
#print(s[::-1])      # 전체 구간을 뒤에서부터 앞으로

# 앞뒤 글자 바꾸기
# ABCD
s = list(input())   # ['A', 'B', 'C', 'D']
print(s)
'''
A <-> D , B <-> C
  0    1    2    3
['A', 'B', 'C', 'D']
'''
print(len(s))
for i in range(len(s) // 2):
    s[i], s[len(s)-i-1] = s[len(s)-i-1], s[i]

print(s)