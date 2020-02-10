import sys
sys.stdin = open("input.txt", 'r')


def sum3(num_list):
    result = []
    for i in range(len(num_list)):
        for j in range(i+1,len(num_list)):
            for k in range(j+1,len(num_list)):
                temp = num_list[i]+num_list[j]+num_list[k]
                result.append(temp)

    return result



q = int(input())

for test_case in range(1,q+1):
    numbers = list(map(int, input().split()))

    a = sum3(numbers)
    a = list(set(a))
    a.sort()
    #print(a)
    print("#{} {}" .format(test_case, a[-5]))
