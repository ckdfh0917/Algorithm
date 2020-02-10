# 반복문으로 부분집합 구하기
bit = [0,0,0,0]     # 각 원소가 포함되었는지의 여부를 0,1로 구분

arr = [1,2,3,4]

for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l
                for n in range(len(bit)):
                    if bit[n] == 1:
                        print(arr[n], end=' ')
                    print()