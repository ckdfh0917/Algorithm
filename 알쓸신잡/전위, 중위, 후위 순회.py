T = int(input())


def preorder(node):
    if node != 0:
        print(node, end=' ')
        preorder(tree[node][0])
        preorder(tree[node][1])


def inorder(node):
    if node != 0:
        inorder(tree[node][0])
        print(node, end=' ')
        inorder(tree[node][1])


def postorder(node):
    if node != 0:
        postorder(tree[node][0])
        postorder(tree[node][1])
        print(node, end=' ')


for test_case in range(1, T + 1):
    V, E, s1, s2 = map(int, input().split())
    numbers = list(map(int, input().split()))

    tree = [[0, 0, 0] for _ in range(V + 1)]

    for i in range(0, E * 2, 2):
        n1 = numbers[i]
        n2 = numbers[i + 1]
        if not tree[n1][0]:
            tree[n1][0] = n2
        else:
            tree[n1][1] = n2
        tree[n2][2] = n1
    print(tree)

    # print('전위순회')
    # preorder(1)
    # print()
    # print('중위순회')
    # inorder(1)
    # print()
    # print('후위순회')
    # postorder(1)
