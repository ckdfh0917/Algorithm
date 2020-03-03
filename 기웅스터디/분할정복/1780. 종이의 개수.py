N = int(input())

def paper(lst):
    global resA, resB, resC
    # print(lst)
    cntA, cntB, cntC = 0, 0, 0  # -1, 0 ,1
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i][j] == -1:
                cntA += 1
            elif lst[i][j] == 0:
                cntB += 1
            elif lst[i][j] == 1:
                cntC += 1

    if cntA == len(lst) * len(lst):
        resA += 1
        return
    elif cntB == len(lst) * len(lst):
        resB += 1
        return
    elif cntC == len(lst) * len(lst):
        resC += 1
        return
    else:
        temp = []
        for i in range(len(lst) // 3):
            temp.append(lst[i][0:len(lst) // 3])
        paper(temp)
        temp = []
        for i in range(len(lst) // 3, len(lst) * 2 // 3):
            temp.append(lst[i][0:len(lst) // 3])
        paper(temp)
        temp = []
        for i in range(len(lst) * 2 // 3, len(lst) * 3 // 3):
            temp.append(lst[i][0:len(lst) // 3])
        ###############################
        paper(temp)
        temp = []
        for i in range(len(lst) // 3):
            temp.append(lst[i][len(lst) // 3:len(lst) * 2 // 3])
        paper(temp)
        temp = []
        for i in range(len(lst) // 3, len(lst) * 2 // 3):
            temp.append(lst[i][len(lst) // 3:len(lst) * 2 // 3])
        paper(temp)
        temp = []
        for i in range(len(lst) * 2 // 3, len(lst) * 3 // 3):
            temp.append(lst[i][len(lst) // 3:len(lst) * 2 // 3])
        ###############################
        paper(temp)
        temp = []
        for i in range(len(lst) // 3):
            temp.append(lst[i][len(lst) * 2 // 3:len(lst) * 3 // 3])
        paper(temp)
        temp = []
        for i in range(len(lst) // 3, len(lst) * 2 // 3):
            temp.append(lst[i][len(lst) * 2 // 3:len(lst) * 3 // 3])
        paper(temp)
        temp = []
        for i in range(len(lst) * 2 // 3, len(lst) * 3 // 3):
            temp.append(lst[i][len(lst) * 2 // 3:len(lst) * 3 // 3])
        paper(temp)

lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))

# for i in range(N):
#     print(lst[i])
resA, resB, resC = 0, 0, 0

paper(lst)
print(resA)
print(resB)
print(resC)
###############################