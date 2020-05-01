T = int(input())
def transfer(hex):
    if hex == '0':
        return '0000'
    elif hex == '1':
        return '0001'
    elif hex == '2':
        return '0010'
    elif hex == '3':
        return '0011'
    elif hex == '4':
        return '0100'
    elif hex == '5':
        return '0101'
    elif hex == '6':
        return '0110'
    elif hex == '7':
        return '0111'
    elif hex == '8':
        return '1000'
    elif hex == '9':
        return '1001'
    elif hex == 'A':
        return '1010'
    elif hex == 'B':
        return '1011'
    elif hex == 'C':
        return '1100'
    elif hex == 'D':
        return '1101'
    elif hex == 'E':
        return '1110'
    elif hex == 'F':
        return '1111'

def decoder(k, x):  # k: 길이수, x: 코드
    res = ''
    for i in range(len(x)):
        res += transfer(x[i])
    print(res)
    # 필요없는 부분 지우기
    temp = 0
    for i in range(1, len(res)):
        if res[-i] == '0':
            temp += 1
        else:
            break

    temp2 = len(res) % 56
    # print(temp2, temp)
    if temp2 != 0:
        res = res[temp2-temp:-temp]
    elif temp2 == 0 and temp != 0:
        res = res[:-temp]
        for i in range(temp):
            res = '0' + res
    print('r',res,k)
    code = ''
    for i in range(0, len(res),k):
        # print('i',i, res[i])
        code += res[i]
    print('yyy',code)

    # 0001010011110000011010001010
    # print(res)
    print('c',code)
    # 숫자로 변환
    result = []
    for i in range(0,len(code), 7):
        if code[i:i+7] == '0001101':
            result.append(0)
        elif code[i:i+7] == '0011001':
            result.append(1)
        elif code[i:i+7] == '0010011':
            result.append(2)
        elif code[i:i+7] == '0111101':
            result.append(3)
        elif code[i:i+7] == '0100011':
            result.append(4)
        elif code[i:i+7] == '0110001':
            result.append(5)
        elif code[i:i+7] == '0101111':
            result.append(6)
        elif code[i:i+7] == '0111011':
            result.append(7)
        elif code[i:i+7] == '0110111':
            result.append(8)
        elif code[i:i+7] == '0001011':
            result.append(9)
    return result


for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(N)]

    # 바코드 내에서 암호코드 찾기
    key_holder = []
    for i in range(N):
        key = []
        for j in range(-1, -M, -1):
            if arr[i][j] != '0':
                key = arr[i][:j+1]
                break
        if key != []:
            for j in range(len(key)):
                if key[j] != '0':
                    key = key[j:]
                    break

        if key not in key_holder:
            print('zzz', ''.join(key))
            key_holder.append(key)

    answer = 0
    # 찾아낸 암호코드에서 코드 추출
    for x in key_holder[1:]:
        k = 0
        d = ''
        print('xx',x, len(x))
        for i in range(14, 500, 14):
            k += 1
            if i-6 <= len(x) <= i+6:
                print('l', k, len(x))
                d = decoder(k, x)
                print('d',d)
                break
        if len(d) != 8:
            continue
        else:
            define = (d[0] + d[2] + d[4] + d[6]) * 3 + (d[1] + d[3] + d[5]) + d[7]
            if define % 10 == 0:
                for i in range(len(d)):
                    answer += d[i]
            print('ppp',answer)

    print('#{} {}'.format(test_case, answer))



