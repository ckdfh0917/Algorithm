res = 123.157
print(format(res, ".2f"))

res = 123.157
print(round(res, 2))

res = 123.20
print(format(res, ".2f"))

res = 123.20
print(round(res, 2))


res = 123.1578
print('{0:.3f}'.format(res))
k = '{0:.3f}'.format(res)
print(k[:-1])