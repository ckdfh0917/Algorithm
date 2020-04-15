class Node:
    def __init__(self, d=0, p=None, n=None):
        self.data = d
        self.prev = p
        self.next = n

class DoublyLinkedList:
    def __init__(self):
        self.head = None        # 첫 번째 노드
        self.tail = None        # 마지막 노드
        self.size = 0           # 노드의 수


def addList(lst, arr):
    first = last = Node(arr[0])
    for val in arr[1:]:
        new = Node(val, last)
        last.next = new
        last = new
    if lst.head is None:
        lst.head, lst.tail = first, last
    else:
        cur = lst.head
        while cur is not None:
            if cur.data > arr[0]:
                break
            cur = cur.next

        if cur is None:     # 마지막
            first.prev = lst.tail
            lst.tail.next = first
            lst.tail = last
        elif cur.prev is None:  # 처음
            last.next = lst.head
            lst.head.prev = last
            lst.head = first
        else:   # 중간
            prev = cur.prev
            first.prev = prev
            last.next = cur
            prev.next = first
            cur.prev = last
    lst.size += len(arr)

def printList(lst):
    if lst.head is None:
        return
    # cur = lst.head
    # while cur is not None:
    #     print(cur.data, end=' ')
    #     cur = cur.next
    # print()
    cur = lst.tail
    for _ in range(10):
    # while cur is not None:
        print(cur.data, end=' ')
        cur = cur.prev
        if cur is None:
            break
    print()


T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    mylist = DoublyLinkedList()
    for _ in range(M):
        arr = list(map(int, input().split()))
        addList(mylist, arr)
    print('#{} '.format(test_case), end='')
    printList(mylist)