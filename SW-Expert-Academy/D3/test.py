q = int(input())

def perm(lst): # permutation을 얻어내기 위한 함수를 정의한다. 인수로는 나열해야할 숫자들을 리스트로 받는다.
    n = len(lst)
    if n == 1:
        return [lst]    # 만약 나열해야할 리스트에 원소가 1개 밖에 없다면 그냥 인수로 받은 리스트를 반환
    else:
        result = []
        for i in lst:
            temp = lst.copy()
            temp.remove(i)
            temp.sort()
            for j in perm(temp):
                j.insert(0, i)
                if j not in result:
                    result.append(j)
    return result



for test_case in range(1, q+1):
    N = int(input())
    A, B, C, D = map(int, input().split())     # +,-,*,/
    numbers = list(map(int, input().split()))
    op = ['+'] * A + ['-'] * B + ['*'] * C + ['/'] * D
    # print(test_case, op)
    new_op = perm(op)

    min_V = 987654321
    max_V = -987654321
    # print(new_op)
    for i in range(len(new_op)):
        temp = numbers[0]
        for j in range(len(new_op[i])):
            # print(temp,new_op[i][j],numbers[j+1], end=' = ')
            if new_op[i][j] == '+':
                temp += numbers[j+1]
            elif new_op[i][j] == '-':
                temp -= numbers[j+1]
            elif new_op[i][j] == '*':
                temp *= numbers[j+1]
            elif new_op[i][j] == '/':
                if temp < 0:
                    temp = -temp // numbers[j+1]
                    temp = -temp
                else:
                    temp //= numbers[j+1]
            # print(temp)
        # print(temp)
        max_V = max(max_V, temp)
        min_V = min(min_V, temp)
    # print(max_V, min_V)
    result = max_V - min_V
    print('#{} {}'.format(test_case,result))


