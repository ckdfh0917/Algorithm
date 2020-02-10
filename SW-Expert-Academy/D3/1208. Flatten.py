
for test_case in range(1,11):
    dump = int(input())

    box_list = list(map(int, input().split()))

    result = 0

    for j in range(dump):
        a_max = 0
        a_min = box_list[0]
        max_temp = 0
        min_temp = 0
        # 최고층 최하층 찾기
        for i in range(len(box_list)):
            if box_list[i] > a_max:
                a_max = box_list[i]
                max_temp = i
            if box_list[i] < a_min:
                a_min = box_list[i]
                min_temp = i

        box_list[max_temp] -= 1
        box_list[min_temp] += 1

        a_max = 0
        a_min = box_list[0]

        for i in range(len(box_list)):
            if box_list[i] > a_max:
                a_max = box_list[i]
            if box_list[i] < a_min:
                a_min = box_list[i]

        result = a_max - a_min
    print('#{} {}' .format(test_case, result))