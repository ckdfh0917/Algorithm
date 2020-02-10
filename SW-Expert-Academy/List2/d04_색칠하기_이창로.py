import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

for test_case in range(1,q+1):
    num = int(input())

    box_list = [[0 for _ in range(10)] for _ in range(10)]
    #print(box_list)

    result = 0
    for k in range(num):
        x1,y1,x2,y2,color = map(int,input().split())
        #print(x1,y1,x2,y2,color)

        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                if box_list[i][j] == 0:
                    box_list[i][j] += color
                elif box_list[i][j] == 1 and color == 2:
                    box_list[i][j] = 3
                elif box_list[i][j] == 2 and color == 1:
                    box_list[i][j] = 3
                # else:
                #     box_list[i][j] = box_list[i][j]
                #print(box_list[i])
        #print('=========================')
    for i in range(10):
        for j in range(10):
            if box_list[i][j] == 3:
                result += 1
        #print(box_list[i])
    print('#{} {}'.format(test_case, result))
