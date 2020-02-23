import sys
sys.stdin = open('input.txt' ,'r')

N = int(input())

lst = []
for i in range(N):
    lst.append(int(input()))
# print(lst)

def find(s,e):
    mid = (s+e) // 2
    l = mid
    r = mid
    h = lst[mid]
    max_r = lst[mid]

    while True:
        if l==s and r==e:
            break

        lh = -1
        rh = -1

        #왼쪽으로 갈 수 있는 경우 왼쪽으로 이동시 높이 lh 를  결정
        if l > s:
            if lst[l - 1] < h:
                lh = lst[l-1]
            else:
                lh = h
        #오른쪽으로 갈 수 있는 경우 오른쪽으로 이동시 높이 rh 를 결정
        if r < e:
            if lst[r+1] < h:
                rh = lst[r+1]
            else:
                rh = h
        # print('r1',r,l,h)
        #왼쪽으로 갈지 , 오른쪽으로 갈지 결정!
        if lh >= rh:
            l-=1
            h = lh
            max_r = max(max_r, h*(r-l+1))
        else:
            r+=1
            h = rh
            max_r = max(max_r, h*(r-l+1))
        # print('r2',r,l,h)
    #     print('a',h*(r-l+1), max_r)
    # print('----------')
    return max_r



def find_max(s,e):  # n = len(lst)
    global arr
    if (e-s) == 1:
        arr.append(find(s,e))
        return
    else:
        temp = find(s,e-1)
        arr.append(temp)

        find_max(s,(s+e)//2)
        find_max((s+e)//2, e-1)


# res = find(0,len(lst)-1)
# find(4,6)
n = len(lst)
arr = []
find_max(0, len(lst))
print(max(arr))