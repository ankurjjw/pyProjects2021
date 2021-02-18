l1 = [1, 2, 3, 'python']
d = l1[-1][-5:]
print(d)

a, *d = l1[-1][-6:]
print(d)


a, *b, (c, *d) = l1
print(d)