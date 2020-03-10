N = int(input())
box = [list(map(int,input().split())) for _ in range(N)]
new_box = sorted(box, key=lambda x: x[0])
res = [0] * (new_box[-1][0] + 1)

# print('n',new_box)
top = sorted(box, key=lambda x: x[1])
stack = []
flag = 0
topI = new_box.index(top[-1])
for i in new_box[:topI+1]:
    if not stack:
        stack.append(i)
    else:
        # print(i)

        if flag == 0:
            if stack[0][1] >= i[1]:
                for j in range(stack[0][0], i[0]+1):
                    res[j] = stack[0][1]
                # print('a',res)
            elif stack[0][1] < i[1]:
                for j in range(stack[0][0], i[0]):
                    res[j] = stack[0][1]
                stack.pop()
                stack.append(i)
n_box = new_box[topI:]
n_box.reverse()
stack2 = []
for i in n_box:
    # print(stack2, i)
    if not stack2:
        stack2.append(i)
    else:
        if stack2[0][1] >= i[1]:
            for j in range(stack2[0][0], i[0], -1):
                res[j] = stack2[0][1]
            # print('a',res)
        elif stack2[0][1] < i[1]:
            for j in range(stack2[0][0], i[0], -1):
                res[j] = stack2[0][1]
            stack2.pop()
            stack2.append(i)
            # print('b',res)
res[new_box[topI][0]] = new_box[topI][1]
# print(res)
print(sum(res))