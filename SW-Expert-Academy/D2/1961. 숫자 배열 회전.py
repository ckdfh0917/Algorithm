q = int(input())

for test_case in range(1, q + 1):
    N = int(input())
    print('#{}'.format(test_case))
    list_a = []
    for i in range(N):
        temp = list(map(int, input().split()))
        list_a += [temp]

    angle_a = []
    angle_b = []
    angle_c = []


    def phase90(N, list_a, angle_a):
        for j in range(N):
            temp_a = []
            for i in range(N):
                temp_a += [list_a[N - 1 - i][j]]
            angle_a.append(temp_a)

        return angle_a


    angle_90 = phase90(N, list_a, angle_a)
    angle_180 = phase90(N, angle_90, angle_b)
    angle_270 = phase90(N, angle_180, angle_c)

    # print(len(angle_90))

    new_list = []
    for i in range(N):
        temp_list = [angle_90[i]] + [angle_180[i]] + [angle_270[i]]

        new_list.append(temp_list)
    str_list = str(new_list)
    new_list = str_list.replace(', ', '')
    new_list = new_list.replace('[[[', '')
    new_list = new_list.replace(']]]', '')
    new_list = new_list.replace(']][[', '\n')
    new_list = new_list.replace('][', ' ')
    print(new_list)
    # print(new_list[0])