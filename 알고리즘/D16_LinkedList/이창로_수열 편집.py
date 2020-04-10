class Node:
    def __init__(self, d=0, n=None):
        self.data = d
        self.next = n

class LinkedList:
    def __init__(self):
        self.head = None        # 첫 번째 노드
        self.tail = None        # 마지막 노드
        self.size = 0           # 노드의 수

def printList(lst):     # lst: LinkedList 객체체
    if lst.head is None:    # 빈 lst
        print('empty')
        return
    cur = lst.head

    print(lst.size, '[', end=' ')
    while cur is not None:
        print(cur.data, end=' ')
        cur = cur.next
    print(']')

def insertLast(lst, new):   # new: 새로 추가할 노드 객체
    # 빈 리스트일 경우
    if lst.head is None:
        lst.head = lst.tail = new
    else:
        # 마지막 노드를 찾는다.
        lst.tail.next = new
        lst.tail = new
    lst.size += 1

def deleteLast(lst):
    if lst.tail is None:
        return

    pre, cur = None, lst.head
    while cur.next is not None:
        pre = cur
        cur = cur.next
    if pre is None:
        lst.head = lst.tail = None
    else:
        pre.next = None
        lst.tail = pre
    lst.size -= 1

def insertFirst(lst, new):
    if lst.head is None:
        lst.head = lst.tail = new
    else:
        new.next = lst.head
        lst.head = new
    lst.size += 1

def deleteFirst(lst):
    if lst.head is None:
        return
    # 노드가 1개일 경우를 주의한다.

    lst.head = lst.head.next
    if lst.head is None:
        lst.tail = None
    lst.size -= 1

def insertAt(lst, idx, new):    # idx: 인덱스 값
    # 빈 리스트일 경우, idx == 0
    if lst.head is None or idx == 0:
        insertFirst(lst, new)
    # 마지막 추가하는 경우 idx >= lst.size
    elif idx >= lst.size:
        insertLast(lst, new)
    # 중간에 추가하는 경우
    else:
        pre, cur = None, lst.head
        for _ in range(idx):
            pre = cur
            cur = cur.next
        new.next = cur
        pre.next = new
        lst.size += 1

def deleteAt(lst, idx):
    if lst.head is None or idx == 0:
        deleteFirst(lst)
    elif idx >= lst.size:
        deleteLast(lst)
    else:
        pre, cur = None, lst.head
        for _ in range(idx):
            pre = cur
            cur = cur.next
        pre.next = cur.next
        lst.size -= 1

def Search(lst, idx):
    cur = lst.head
    # if idx >= lst.size or lst.head is None:
    #     return print(-1)
    for _ in range(idx):
        if cur is None:
            return print(-1)
        if cur.next is None:
            return print(-1)
        cur = cur.next
    print(cur.data)

def Change(lst, idx, num):
    cur = lst.head
    for _ in range(idx):
        cur = cur.next
    cur.data = num

T = int(input())
for test_case in range(1, T+1):
    N, M, L = map(int, input().split())
    numbers = list(map(int, input().split()))
    print('#{} '.format(test_case), end='')
    newlist = LinkedList()

    for i in numbers:
        insertLast(newlist, Node(i))
    # printList(newlist)

    for _ in range(M):
        command = list(map(str, input().split()))
        # print(command)
        cmd = command[0]
        idx = int(command[1])
        if cmd == 'I':
            num = int(command[2])
            insertAt(newlist, idx, Node(num))
            # print('i')
            # printList(newlist)
        elif cmd == 'D':
            deleteAt(newlist, idx)
            # print('d')
            # printList(newlist)
        elif cmd == 'C':
            num = int(command[2])
            Change(newlist, idx, num)
            # print('c')
            # printList(newlist)
    # printList(newlist)

    Search(newlist, L)