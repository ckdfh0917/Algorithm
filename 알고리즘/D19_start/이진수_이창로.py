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

for test_case in range(1, T+1):
    N, hex = map(str, input().split())
    N = int(N)
    result = ''
    for i in range(N):
        result += transfer(hex[i])
    print('#{} {}' .format(test_case, result))