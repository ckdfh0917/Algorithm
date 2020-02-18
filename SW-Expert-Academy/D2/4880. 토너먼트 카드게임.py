import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

def g(lst,lst2):
    if lst[0] == 1 and lst[1] == 2:
        lst = 2
        lst2 = lst2[1]
    elif lst[0] == 1 and lst[1] == 3:
        lst = 1
        lst2 = lst2[0]
    elif lst[0] == 1 and lst[1] == 1:
        lst = 1
        lst2 = lst2[0]
    elif lst[0] == 2 and lst[1] == 3:
        lst = 3
        lst2 = lst2[1]
    elif lst[0] == 2 and lst[1] == 1:
        lst = 2
        lst2 = lst2[0]
    elif lst[0] == 2 and lst[1] == 2:
        lst = 2
        lst2 = lst2[0]
    elif lst[0] == 3 and lst[1] == 1:
        lst = 1
        lst2 = lst2[1]
    elif lst[0] == 3 and lst[1] == 2:
        lst = 3
        lst2 = lst2[0]
    elif lst[0] == 3 and lst[1] == 3:
        lst = 3
        lst2 = lst2[0]
    return lst, lst2

# 쪼개고 가위바위보 하기
def s(lst,lst2,N):
    global stack
    global arr_II

    if N <= 2:
        if len(lst) == 2:
            temp = list(g(lst,lst2))
            lst = [temp[0]]
            lst2 = [temp[1]]

        stack += [lst]
        arr_II += [lst2]
        return
    elif 2 < N:
        if N % 2 == 0:
            s(lst[:N//2],lst2[:N//2],N//2)
            s(lst[N//2:N],lst2[N//2:N],N//2)
        else:
            s(lst[:N//2+1],lst2[:N//2+1],N//2)
            s(lst[N//2+1:N],lst2[N//2+1:N],N//2)


# 합치기
def f(stack, arr_II):
    s2 = []
    temp = []
    if len(stack) % 2 == 0:         # 짝수 합치기
        for i in range(len(stack)//2):
            a = stack.pop(0)
            b = stack.pop(0)
            s2 += (a+b)
            c = arr_II.pop(0)
            d = arr_II.pop(0)
            temp += (c+d)
    else:                           # 홀수 합치기
        for i in range(len(stack)//2):
            a = stack.pop(0)
            b = stack.pop(0)
            s2 += (a + b)
            c = arr_II.pop(0)
            d = arr_II.pop(0)
            temp += (c + d)
        s2 += (stack.pop(0))
        temp += (arr_II.pop(0))
    return s2, temp

def length(N):
    if 1 <= N <= 2:
        k = 1
    elif 3 <= N <= 4:
        k = 2
    elif 5 <= N <= 8:
        k = 3
    elif 9 <= N <= 16:
        k = 4
    elif 17 <= N <= 32:
        k = 5
    elif 33 <= N <= 64:
        k = 6
    elif 65 <= N <= 128:
        k = 7
    elif 129 <= N <= 256:
        k = 8
    return k

for test_case in range(1,q+1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr_I = [i for i in range(1,N+1)]
    print('#{} ' .format(test_case), end='')
    print(arr)
    k = length(N)

    stack = []
    arr_II = []

    s(arr,arr_I, N)
    print(stack,arr_II)
    
    # temp2 = list(f(stack,arr_II))
    # stack2 = temp2[0]
    # index = temp2[1]
    # print(stack2, index)
    # for i in range(k-1):
    for i in range(len(stack)):
        for j in range(length(len(stack[i]))):
            s(stack[j],arr_II,len(stack[i]))
        # print(stack, arr_II)
        # temp2 = list(f(stack,arr_II))
        # stack2 = temp2[0]
        # index = temp2[1]
        # print(stack2, index)
    #print(arr_II[0])