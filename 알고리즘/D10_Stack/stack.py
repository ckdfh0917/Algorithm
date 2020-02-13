'''
스택 구현하기

구현한 스택을 이용해서 3개의 데이터를 스택에 저장하고

다시 3번 꺼내서 출력하기
'''

# 크기가 정하재니 리스트를 사용해서 스택 구현
stack = [0] * 10
top = -1
# push 연산 : top을 하나 늘리고 stack의 top 인덱스에 원소를 삽입
def push(item,stack,top):
    top += 1
    stack.append(item)
    return stack
# pop 연산 : top 인덱스 원소 리턴(출력)하고 top를 하나 줄임
def pop(stack,top):
    temp = stack.pop(top)
    top -= 1
    return temp

def isEmpty(top):
    if top == -1:
        return False
    else:
        return True
# 모든 원소 꺼내기 : 스택이 비어있지 않으면 스택의 원소를 꺼내 출력(isEmpty가 될때까지)

def all_pop(list,top):

    while isEmpty():
        pop()

# 리스트 기능을 이용해서 스택 구현하기
s = list()     # 빈 리스트 만들기
# push : list의 append
s.append(10)
s.append(20)
s.append(30)
print(s)

# 스택의 모든 원소 꺼내서 출력하기
while len(s) != 0:
    print(s.pop())
print(s)