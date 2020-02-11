import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

for test_case in range(1, q+1):
    str1 = input()
    str2 = input()

    max_num = 0
    for j in range(len(str1)):
        cnt = 0
        for i in range(len(str2)):
            #print(str2[i],str1[j])
            if str2[i] == str1[j]:
                cnt += 1
        if max_num < cnt:
            max_num = cnt

    print('#{} {}' .format(test_case, max_num))