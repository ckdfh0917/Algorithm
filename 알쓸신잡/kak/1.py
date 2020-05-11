def solution(numbers, hand):
    answer = ''
    left_pos = 10
    right_pos = 12
    for x in numbers:
        # 1 4 7
        if x == 1 or x == 4 or x == 7:
            answer += 'L'
            left_pos = x
        # 3 6 9
        elif x == 3 or x == 6 or x == 9:
            answer += 'R'
            right_pos = x
        # 2 5 8 0
        else:
            if x == 0:
                x = 11
            # 기준 맞추기
            if x == 1 or x == 4 or x == 7:
                temp = left_pos + 2
            else:
                temp = left_pos
            # 위상이 같으면 주 손잡이 쓰기
            if temp == right_pos:
                if hand == 'right':
                    answer += 'R'
                    right_pos = x
                else:
                    answer += 'L'
                    left_pos = x
            # 왼쪽 위상이 더 높으면
            # elif temp > right_pos:
            else:
                if left_pos == 1 or left_pos == 4 or left_pos == 7:
                    temp -= 1
                    k1 = abs(x - temp)
                    print(k1)
                else:
                    temp = left_pos
                    if abs(x - temp) == 3:
                        k1 = 0
                    elif abs(x - temp) == 6:
                        k1 = 3
                    elif abs(x - temp) == 9:
                        k1 = 6
                    elif abs(x - temp) == 0:
                        answer += 'L'
                        continue
                    print(temp, x)
                if right_pos == 3 or right_pos == 6 or right_pos == 9:
                    temp2 = right_pos - 1
                    k2 = abs(x - temp2)
                else:
                    temp2 = right_pos
                    if abs(x - temp2) == 3:
                        k2 = 0
                    elif abs(x - temp2) == 6:
                        k2 = 3
                    elif abs(x - temp2) == 9:
                        k2 = 6
                    elif abs(x - temp2) == 0:
                        answer += 'R'
                        continue

                print(x)
                print(k1, k2)
                if k1 == k2:
                    if hand == 'right':
                        answer += 'R'
                        right_pos = x
                    else:
                        answer += 'L'
                        left_pos = x
                elif k1 > k2:
                    answer += 'R'
                    right_pos = x
                else:
                    answer += 'L'
                    left_pos = x
            # elif temp < right_pos:

    return answer