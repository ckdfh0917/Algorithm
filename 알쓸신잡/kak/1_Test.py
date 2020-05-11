def solution(numbers, hand):
    answer = ''
    left_pos = 10
    right_pos = 12
    for x in numbers:
        if x == 0:
            x = 11
        # 1 4 7
        if x == 1 or x == 4 or x == 7:
            # print('147')
            answer += 'L'
            left_pos = x
        # 3 6 9
        elif x == 3 or x == 6 or x == 9:
            # print('369')
            answer += 'R'
            right_pos = x
        # 2 5 8 0
        else:
            if x == left_pos:
                answer += 'L'
                left_pos = x
            elif x == right_pos:
                answer += 'R'
                right_pos = x

            # 왼손이 147 오른손이 369
            elif left_pos in [1, 4, 7, 10] and right_pos in [3, 6, 9, 12]:
                # print('aaaa')
                tL = left_pos + 1
                tL = abs(tL - x)
                tR = right_pos - 1
                tR = abs(tR - x)
                # print('ttt',tL, tR)
                if tL < tR:
                    answer += 'L'
                    left_pos = x
                elif tL > tR:
                    answer += 'R'
                    right_pos = x
                else:
                    if hand == 'right':
                        answer += 'R'
                        right_pos = x
                    elif hand == 'left':
                        answer += 'L'
                        left_pos = x
                        # 왼손이 147 오른손 2580
            elif left_pos in [1, 4, 7, 10]:
                # print('bbbb')
                tL = left_pos + 1
                tL = abs(tL - x) // 3 + 1
                tR = abs(right_pos - x) // 3
                # print('ttt',tL, tR)
                if tL < tR:
                    answer += 'L'
                    left_pos = x
                elif tL > tR:
                    answer += 'R'
                    right_pos = x
                else:
                    if hand == 'right':
                        answer += 'R'
                        right_pos = x
                    elif hand == 'left':
                        answer += 'L'
                        left_pos = x

                        # 왼손이 2580 오른손이 369
            elif right_pos in [3, 6, 9, 12]:
                # print('cccc', left_pos, right_pos, x)
                tR = right_pos - 1
                tL = abs(left_pos - x) // 3
                tR = abs(tR - x) // 3 + 1
                # print('ttt',tL, tR)
                if tL < tR:
                    answer += 'L'
                    left_pos = x
                elif tL > tR:
                    answer += 'R'
                    right_pos = x
                else:
                    if hand == 'right':
                        answer += 'R'
                        right_pos = x
                    elif hand == 'left':
                        answer += 'L'
                        left_pos = x
            # 양손이 2580
            else:
                # print('dddd')
                tL = abs(left_pos - x) // 3
                tR = abs(right_pos - x) // 3
                # print('ttt',tL, tR)
                if tL < tR:
                    answer += 'L'
                    left_pos = x
                elif tL > tR:
                    answer += 'R'
                    right_pos = x
                else:
                    if hand == 'right':
                        answer += 'R'
                        right_pos = x
                    elif hand == 'left':
                        answer += 'L'
                        left_pos = x
    return answer