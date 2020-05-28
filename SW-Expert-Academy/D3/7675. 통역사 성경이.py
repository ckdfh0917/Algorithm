import sys
sys.stdin = open('input.txt', 'r')


# 조건조차 잘못줌
#
# 첫글자는 대문자 두번째 글자는 소문자이어야 하며 그 이후에 대문자가 또 있어도 이름으로 쳐줌
#
# 대신 숫자가 있으면 이름이 아님
#
# 예시 입력에 대한 예시 출력이 틀렸음

# 1 3 1
# 2 2 0 1  이 맞음




q = int(input())

ABC = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W'
    , 'X', 'Y', 'Z']
gudu = ['.', '?', '!']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

for test_case in range(1, q + 1):
    num = int(input())
    words = list(map(str, input().split()))
    #print(words)
    #print(len(words))
    # print(words)
    print('#{} '.format(test_case), end='')
    result = [] #* num

    index = 0
    name = []
    temp = []
    for i in range(len(words)):

        if words[i][-1] not in gudu:
            temp += [words[i]]
        elif words[i][-1] in gudu:
            temp += [words[i][:-1]]
            name.append(temp)
            temp = []

    # name : 구두점으로 분류한 리스트
    for i in range(len(name)):
        count = 0
        for j in range(len(name[i])):
            for _ in range(len(name[i][j])):
                if name[i][j][0] in ABC:  # 첫번째 글자가 대문자이면
                    if len(name[i][j]) == 1:  # 첫번째 글자가 대문자이고 한글자이면
                        count += 1
                        break
                    elif len(name[i][j]) > 1:  # 첫번째 글자가 대문자이고 두글자 이상이면
                        if name[i][j][1] not in ABC and name[i][j][1:].isalpha():  # 두번째 글자가 소문자이고 전부 영어이면
                                count += 1
                                break
        result.append(count)




    print(" ".join(map(str, result)))