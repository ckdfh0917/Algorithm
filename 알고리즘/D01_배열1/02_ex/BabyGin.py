
#list_a = [3, 2, 5, 5, 1, 5]
list_a = [6,6,7,7,6,7]



def BubbleSort(a):
    for j in range(len(a) - 1, 0, -1):
        for i in range(j):
            if a[i] > a[i + 1]:
                a[i],a[i+1] = a[i+1],a[i]

BubbleSort(list_a)
#print(list_a)
count_a = [0 for _ in range(10)]

for i in range(len(list_a)):
    count_a[list_a[i]] += 1

#print(count_a)

run, triple = 0, 0

for i in range(5):
    if count_a[i] == True and count_a[i+1] == True and count_a[i+2] == True:
        print('run')
        run += 1
        count_a[i] -= 1
        count_a[i+1] -= 1
        count_a[i+2] -= 1

for i in count_a:
    if i == 3:
        triple += 1
        print('triple')
    elif i == 6:
        triple = 2
        print('double triple')

result = run + triple

if result == 2:
    print('!!!!!BabyGin!!!!!')
