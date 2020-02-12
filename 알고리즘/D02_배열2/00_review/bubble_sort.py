# 버블정렬을 구현하세요

arr = [5,2,3,4,1]


max_arr = 0

for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i] < arr[j]:
            arr[i],arr[j] = arr[j],arr[i]

print(arr)