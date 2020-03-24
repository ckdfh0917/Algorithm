import sys
input = sys.stdin.readline

def f(s, n):
    if s == 'push_back':
        deck.append(n)
    elif s == 'push_front':
        deck.insert(0, n)
    elif s == 'pop_front':
        if not deck:
            return print(-1)
        t = deck.pop(0)
        return print(t)
    elif s == 'pop_back':
        if not deck:
            return print(-1)
        t = deck.pop()
        return print(t)
    elif s == 'size':
        return print(len(deck))
    elif s == 'front':
        if not deck:
            return print(-1)
        return print(deck[0])
    elif s == 'back':
        if not deck:
            return print(-1)
        return print(deck[-1])
    elif s == 'empty':
        if deck:
            print(0)
        else:
            print(1)
N = int(input())
deck = []

for _ in range(N):
    k = list(map(str, input().split()))
    s = k[0]
    if len(k) == 1:
        n = 0
        f(s, n)
    elif len(k) == 2:
        b = k[1]
        n = int(b)
        f(s, n)
