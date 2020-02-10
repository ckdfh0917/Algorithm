q = int(input())

for test_case in range(1, q + 1):
    num = int(input())
    card = list(map(int, input()))
    
    count_a = [0 for _ in range(10)]
    
    for i in range(num):
        for j in range(10):
            if card[i] == j:
                count_a[j] += 1
     
    #print(count_a)
    k = 0
    max_num = 0
    for i in range(10):
        if count_a[i] > max_num:
            max_num = count_a[i]
            k = i
        elif count_a[i] == max_num:
            if i > k:
                k = i
    print('#{} {} {}' .format(test_case,k,max_num))
        