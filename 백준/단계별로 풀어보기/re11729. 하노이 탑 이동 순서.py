N = int(input())
stack = []
def f(n, a, b, k):  # n개 a에서 k로 b가 옮겨짐
    print(n,a,b,k)
    if n == 1:
        print('aaaaaaaaaaa',n,a,b,k)
        stack.append([a,k])
    else:
        f(n-1,a,k,b)
        print('bbbbbbbbbbb',n,a,b,k)
        stack.append(([a,k]))
        f(n-1,b,a,k)

f(N,1,2,3)
print(len(stack))
for i in range(len(stack)):
    print(' '.join(map(str, stack[i])))