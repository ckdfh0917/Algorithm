# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

A = [[2, 7, 5], [3, 1, 1], [2, 1, -7], [0, 2, 1], [1, 6, 8]]

def solution(A):
    # write your code in Python 3.6
    print(A)
    sum_row = []
    for i in range(len(A)):
        print(A[i])
        sum_row.append(sum(A[i]))
    print(sum_row)

    all_sum_row = sum(sum_row)
    print(all_sum_row)

    cnt1 = 0
    above = 0
    below = all_sum_row - sum_row[0]
    for i in range(len(A)):
        if i != 0:
            above += sum_row[i-1]
            below -= sum_row[i]
        print(i, above, below)
        if above == below:
            cnt1 += 1
    print(cnt1)
    print()
    sum_col = []
    for j in range(len(A[0])):
        temp = 0
        for i in range(len(A)):
            print(A[i][j])
            temp += A[i][j]
        sum_col.append(temp)
        print()
    print(sum_col)
    cnt2 = 0
    for i in range(len(A[i])):
        if 0 < i < len(A[i])-1:
            if sum_col[i-1] == sum_col[i+1]:
                cnt2 += 1
            elif i == 0:
                if sum_col[i+1] == 0:
                    cnt2 += 1
            else:
                if sum_col[i-1] == 0:
                    cnt2 += 1
    print(cnt1, cnt2)
    return cnt1 * cnt2
solution(A)