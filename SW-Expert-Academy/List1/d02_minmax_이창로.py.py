q = int(input())

for test_case in range(1,q+1):
    numbers = int(input())
    
    num_list = list(map(int, input().split()))
    
    #print(num_list)
    
    max_num = 0
    min_num = num_list[0]
    for i in range(numbers):
        if num_list[i] > max_num:
            max_num = num_list[i]
        if num_list[i] < min_num:
            min_num = num_list[i]
    result = max_num - min_num
    print('#{} {}' .format(test_case,result))