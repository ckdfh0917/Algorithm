Xa, Ya, Xb, Yb, Xc, Yc = map(int, input().split())

M1 = 987654321
M2 = 987654321
if Xa != Xb: M1 = (Ya-Yb) / (Xa-Xb)
if Xb != Xc: M2 = (Yb-Yc) / (Xb-Xc)

if M1 == M2:
    print(-1)
else:
    a1 = ((Xa-Xb)**2 + (Ya-Yb)**2)**0.5
    b1 = ((Xb - Xc) ** 2 + (Yb - Yc) ** 2) ** 0.5
    c1 = ((Xc - Xa) ** 2 + (Yc - Ya) ** 2) ** 0.5

    a = (a1 + b1) * 2
    b = (b1 + c1) * 2
    c = (c1 + a1) * 2
    #
    # a2 = ((Xa-Xc)**2 + (Ya-Yc)**2)**0.5
    # b2 = ((Xb-Xa)**2 + (Yb-Ya)**2)**0.5
    #
    # c2 = ((Xc-Xb)**2 + (Yc-Yb)**2)**0.5
    # print(a,b,c)
    max_V = max(a,b,c)
    min_V = min(a,b,c)

    result = max_V - min_V
    print(result)