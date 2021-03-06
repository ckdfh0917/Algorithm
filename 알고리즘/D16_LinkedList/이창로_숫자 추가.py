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
        insertFirst(lst, new)
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
        pass

def Search(lst, idx):
    cur = lst.head

    for i in range(idx):
        cur = cur.next
    print(cur.data)


mylist = LinkedList()

# for i in range(5):
#     insertFirst(mylist, Node(i))
#     printList(mylist)
#
# for i in range(3):
#     insertAt(mylist, 2, Node(i + 10))
#     printList(mylist)
#
# insertAt(mylist, 6, Node(-1))
# printList(mylist)

T = int(input())
for test_case in range(1, T+1):
    N, M, L = map(int, input().split())
    numbers = list(map(int, input().split()))
    print('#{} '.format(test_case), end='')
    newlist = LinkedList()

    for i in numbers:
        insertLast(newlist, Node(i))
    # printList(newlist)

    for i in range(M):
        idx, num = map(int, input().split())
        insertAt(newlist, idx, Node(num))
    Search(newlist, L)