q = int(input())
grade_dict = {1: 'A+', 2: 'A0',
              3: 'A-', 4: 'B+', 5: 'B0',
              6: 'B-', 7: 'C+', 8: 'C0',
              9: 'C-', 10: 'D0'}

for test_case in range(1, q + 1):
    N, K = map(int, input().split())  # 학생수 N, 학점을 알고 싶은 학생의 번호 K
    grade = []
    # print('#{} ' .format(test_case))
    for i in range(1, N + 1):
        temp = 0
        mid_exam, final_exam, homework = map(int, input().split())

        temp = mid_exam * 0.35 + final_exam * 0.45 + homework * 0.2
        grade.append(temp)
    # print(grade)
    K_grade = grade[K - 1]
    grade.sort()

    # if test_case == 3:
    #	print(K_grade)
    #	print(grade)

    rank = 1
    for i in grade:
        if K_grade == i:
            rank = (N - rank + 1)
            break
        rank += 1
    temp_a = N // 10
    # print(rank)

    rank = rank / temp_a
    # print(rank)
    result = rank - int(rank)
    rank = int(rank)
    # print(result)
    if 0 < result < 1:
        rank += 1
    rank = grade_dict[rank]

    print('#{} {}'.format(test_case, rank))