def avg(a, b, c):
    return (a + b + c) / 3


def avgargs(*args):
    count = len(args)
    sumofargs = sum(args)
    # handling zero division error
    return count and sumofargs / count


# handling zero division error by using atleat one required parameter
def avgargs2(a, *args):
    count = len(args) + 1
    sumofargs = sum(args) + a
    return sumofargs / count


# force keyword arguments
def keyargs(a, b, *args, d):
    count = len(args) + 3
    sumofargs = sum(args) + a + b + d
    return sumofargs / count


# no positional arguments
def keyargs2(*, d, e, f, g):
    sumofargs = d + e + f + g
    return sumofargs / 4


# keyword arguments **kwargs
def keyargs3(**kwargs):
    d1 = {*kwargs}
    print(d1)
    print(kwargs, len(kwargs), sum(list(kwargs.values()))/len(kwargs))


l = [10, 20, 30]
print(avg(*l))
print(avgargs())
print(avgargs2(2))
print(keyargs(1, 2, d=4))
print(keyargs2(d=1, e=2, f=3, g=4))

print(keyargs3(a=10, b=20, c=30, d=40))
