from collections import deque

dq = deque()
dq.append(1)
dq.append(2)
dq.append(3)

dq.appendleft(9)
dq.popleft()
dq.pop()

# dq는 처음과 마지막 원소에 대해서만 중간 값 안됨

