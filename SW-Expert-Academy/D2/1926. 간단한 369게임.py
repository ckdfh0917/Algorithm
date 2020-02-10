q = int(input())

list_a = []
for i in range(1, q + 1):
    list_a += [i]

str_a = list(map(str, list_a))

for j in str_a:

    if j == '3' or j == '6' or j == '9':
        print('-', end=' ')
    elif j == '1' or j == '2' or j == '4' or j == '5' or j == '7' or j == '8':
        print(j, end=' ')

    elif j[1] == '3' or j[1] == '6' or j[1] == '9':

        if j[0] == '3' or j[0] == '6' or j[0] == '9':
            # print('b{}{}\n' .format(j[0],j[1]))
            print('--', end=' ')
        else:
            # print('c{}{}\n' .format(j[0],j[1]))
            print('-', end=' ')
    elif j[0] == '3' or j[0] == '6' or j[0] == '9':
        print('-', end=' ')
    else:
        print(j, end=' ')
    # print('#{0} {1}' .format(j[0],j[1]))