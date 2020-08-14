a, b, c = map(int, input().split())
R = list(map(int, input().split()))
G = list(map(int, input().split()))
B = list(map(int, input().split()))

R.sort()
G.sort()
B.sort()

res = 0
r = R.pop()
g = G.pop()
b = B.pop()
while True:
    if (r == -1 and g == -1) or (g == -1 and b == -1) or (b == -1 and r == -1):
        break

    if r >= g and r >= b:
        if g > b:
            res += r * g
            if R:
                r = R.pop()
            else:
                r = -1
            if G:
                g = G.pop()
            else:
                g = -1
        elif g == b:
            if len(G) > len(B):
                res += r * g
                if R:
                    r = R.pop()
                else:
                    r = -1
                if G:
                    g = G.pop()
                else:
                    g = -1
            else:
                res += r * b
                if R:
                    r = R.pop()
                else:
                    r = -1
                if B:
                    b = B.pop()
                else:
                    b = -1
        else:
            res += r * b
            if R:
                r = R.pop()
            else:
                r = -1
            if B:
                b = B.pop()
            else:
                b = -1
    elif g >= b and g >= r:
        if b > r:
            res += g * b
            if G:
                g = G.pop()
            else:
                g = -1
            if B:
                b = B.pop()
            else:
                b = -1
        elif b == r:
            if len(B) > len(R):
                res += g * b
                if G:
                    g = G.pop()
                else:
                    g = -1
                if B:
                    b = B.pop()
                else:
                    b = -1
            else:
                res += g * r
                if G:
                    g = G.pop()
                else:
                    g = -1
                if R:
                    r = R.pop()
                else:
                    r = -1
        else:
            res += g * r
            if G:
                g = G.pop()
            else:
                g = -1
            if R:
                r = R.pop()
            else:
                r = -1
    elif b >= r and b >= g:
        if r > g:
            res += b * r
            if B:
                b = B.pop()
            else:
                b = -1
            if R:
                r = R.pop()
            else:
                r = -1
        elif r == g:
            if len(R) > len(G):
                res += b * r
                if B:
                    b = B.pop()
                else:
                    b = -1
                if R:
                    r = R.pop()
                else:
                    r = -1
            else:
                res += b * g
                if B:
                    b = B.pop()
                else:
                    b = -1
                if G:
                    g = G.pop()
                else:
                    G = -1
        else:
            res += b * g
            if B:
                b = B.pop()
            else:
                b = -1
            if G:
                g = G.pop()
            else:
                g = -1
print(res)