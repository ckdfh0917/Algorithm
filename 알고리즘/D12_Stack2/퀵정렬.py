def partition(arr, low, high):
    pivot = (low + high) // 2   # 피봇으로 중간값 설정
    L = low     # L,R의 초기값 설정
    R = high

    while L < R:
        while arr[L] < arr[pivot] and L < R:    # L의 값이 pivot 보다 작을 때 까지
            L += 1      # 오른쪽으로 이동
        while arr[R] >= arr[pivot] and L < R:   # R의 값이 pivot 보다 크거나 같을 때까지
            R -= 1      # 왼쪽으로 이동
        if L < R:
            if L == pivot:
                pivot = R
            arr[L], arr[R] = arr[R], arr[L]
        arr[pivot], arr[R] = arr[R], arr[pivot]
    return R

def quicksort(arr,low,high):
    if low < high:
        p = partition(arr, low, high)
        quicksort(arr,low,p-1)
        quicksort(arr,p+1,high)


arr = [10,7,8,9,1,5]
n = len(arr)
quicksort(arr,0,n-1)    # 시작점, 끝점
print(arr)
