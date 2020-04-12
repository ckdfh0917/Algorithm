class Node:
    def __init__(self, d=0, p=None, n=None):
        self.data = d
        self.prev = p
        self.next = n

class DoublyLinkedList:
    def __init__(self):
        self.head = None        # 첫 번째 노드
        self.size = 0           # 노드의 수

def addLast(lst, new):
    if lst.head is None:
        lst.head = new
        new.prev = new.next = new
    else:
        tail = lst.head.prev
        new.prev = tail
        new.next = lst.head
        tail.next = new
        lst.head.prev = new
    lst.size += 1


def printList(lst):
    if lst.head is None:
        return
    cur = lst.head.prev
    for i in range(1, 11):
        print(cur.data, end=' ')
        cur = cur.prev
        if lst.size == i:
            break
    print()

T = int(input())
for test_case in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    mylist = DoublyLinkedList()
    for val in arr:
        addLast(mylist, Node(val))
    cur = mylist.head
    for _ in range(K):
        for _ in range(M):
            cur = cur.next

        prev = cur.prev
        new = Node(prev.data + cur.data, prev, cur)
        prev.next = new
        cur.prev = new
        cur = new
        mylist.size += 1
    print('#{} '.format(test_case), end='')
    printList(mylist)