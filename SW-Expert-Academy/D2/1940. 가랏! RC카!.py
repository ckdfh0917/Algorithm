q = int(input())

for test_case in range(1, q + 1):
    time = int(input())

    command = []
    for i in range(time):
        temp = list(map(int, input().split()))
        command.append(temp)
    # print(command)

    # print(command[0][0])
    # print(command[1])
    velocity = 0
    distance = 0

    for i in range(time):
        if command[i] == 0:
            velocity = velocity
        elif command[i][0] == 1:
            velocity += command[i][1]
        elif command[i][0] == 2:
            velocity -= command[i][1]
            if velocity < 0:
                velocity = 0
        distance += abs(velocity)

        # if test_case == 10:
        # print(command[i])
        # print(velocity)
        # print(distance)
    print('#{} {}'.format(test_case, distance))