def sqr(a):
    return a * a


print(sqr(5))

h = lambda b: b * b
answer = h(6)
print((lambda b: b * b)(7))
print(answer)


def mult(l, j):
    return l + j


print(mult(6, 7))

g = lambda a, c: a + c
point = g(5, 6)
print((lambda a, c: a + c)(5, 7))
print(point)
