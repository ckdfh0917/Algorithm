
list_a = [3, 2, 5, 4, 1]

# '''
# for j in range(len(list_a)-1,0,-1):
#     for i in range(j):
#         if list_a[i] > list_a[i+1]:
#             temp = list_a[i]
#             list_a[i] = list_a[i+1]
#             list_a[i+1] = temp
#         print(list_a)
# '''

def BubbleSort(a):
    for j in range(len(a) - 1, 0, -1):
        for i in range(j):
            if a[i] > a[i + 1]:
                a[i],a[i+1] = a[i+1],a[i]

BubbleSort(list_a)
print(list_a)