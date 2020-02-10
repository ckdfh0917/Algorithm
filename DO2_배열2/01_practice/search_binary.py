# 이진탐색 구현
'''
검색 시작점, 종료점을 설정함 (반복이 진해오디면서 시작점, 종료점 갱신)
반복시작
    중앙값을 구함
    중아점의 값과 찾고자하는 값을 비교해봄
        같다면? 찾았으니까 True 리턴
        중앙점의 값이 크면?      왼쪽 탐색 -> 종료점을 갱신
        중앙점의 값이 작으면?    오른쪽 탐색 -> 시작점을 갱신
반복 종료후 아직도 리턴을 못했다면? 없다는 의미이므로 False 리턴
'''


# a : 배열
# n : 배열의 길이
# key : 찾고자 하는 수

arr = [2, 4, 7, 9, 11, 19, 23]
n = len(arr)
#print(n)
def binarySearch(arr, key):
    start = 0
    end = len(a)-1
    while True:
        middle = (start+end)//2
        if a[middle] == key:
            return True
        elif a[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
    return False
print(binarySearch(arr,7))