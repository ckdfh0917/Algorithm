# 선택 정렬 구현

arr = [5,3,2,1,4]
n = len(arr)

def selectSort(arr, n):
    for i in range(n-1):
        min_num = arr[i]
        temp = i
        for j in range(i+1,n):
            if arr[j] < min_num:
                min_num = arr[j]
                temp = j
        arr[i],arr[temp] = arr[temp],arr[i]
        print(arr)
    return print(arr)

selectSort(arr,n)