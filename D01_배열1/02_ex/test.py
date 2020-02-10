# 디버깅용 시험 제출시 제거
import sys
sys.stdin = open('input.txt','r')            # 표준입력을 콘솔창에서 파일로 변경

munja_dict = {}
list_a = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','+','/']

print(list_a)

k = 0
for i in list_a:
    munja_dict[i] = k
    k += 1

print(munja_dict)

q = int(input())

for test_case in range(1, q + 1):
    a_str = input()

