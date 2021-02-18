def process(s):
    s.append('d')
    # s = s + ['d']
    print(id(s))
    return s


def string_var(s):
    s = s + ' world'
    print(id(s))
    return s


my_var = ['a', 'b', 'c']
print(process(my_var))
print(id(my_var))
print(my_var)

my_var1 = 'hello'

print(string_var(my_var1))
print(id(my_var1))
print(my_var1)
