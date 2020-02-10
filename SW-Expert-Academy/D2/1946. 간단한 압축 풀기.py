q = int(input())

for test_case in range(1, q + 1):
    num = int(input())
    print('#{}'.format(test_case))
    a_list = []
    b_list = []
    length = 0
    for i in range(num):
        munja, K = map(str, input().split())
        k = int(K)
        length += k
        a_list += munja * k

    # print(a_list)
    # print(length)
    # print(length // 10)
    temp = length // 10
    if length % 10 != 0:
        temp += 1
    for i in range(temp):
        b_list.append(a_list[10 * i:10 * i + 10])

    str_b = str(b_list)

    new_str = str_b.replace('[[', '')
    new_str = new_str.replace('\'', '')
    new_str = new_str.replace(',', '')
    new_str = new_str.replace('] [', '\n')
    new_str = new_str.replace(']]', '')
    new_str = new_str.replace(' ', '')
    print(new_str)