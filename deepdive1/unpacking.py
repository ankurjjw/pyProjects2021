l = ('a', 'b', 'c')

b = l[1:]

print(b)

# this always creates a list not tuple
c, *d = l
print(c, d)

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l = [l1, l2]
print(l)
l = [*l1, *l2]
print(l)

d1 = {'p': 1, 'y': 2, 't': 3}
d2 = {'h': 4, 'o': 5, 'n': 6}
d0 = {'h': 4, 'o': 5, 'f': 9}

d3 = {*d1, *d2, *d0}
print(d3)

d3 = [*d1, *d2, *d0]
print(d3)

a, *d4 = d1
print(d4)

d5 = {**d1, **d2, **d0}
print(d5)

# this always creates a list not dictionary or set
a, *d = d5
print(d)

a, *b, (c, *d) = [1, 2, 3, 'python']
print(d)
print(b)


