# 반복문을 이용하여 순열을 구현해보세요
# 1, 2, 3
list_a = [1, 2, 3]

for i in range(1,4):
    for j in range(1,4):
        if i != j:
            #print(i,j)
            for k in range(1,4):
                if i != k and j != k:
                    print(i,j,k)
