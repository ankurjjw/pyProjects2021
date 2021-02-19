x = 5
y = 10


def my_func(a: 'an integer with a max value of ' + str(max(x,y)), b: 'a string',
            *args: 'a bunch of positional parameters',
            c: 'a keyword only argument', d: 'another keyword only argument' = 'hello',
            **kwargs: 'a bunch of other keyword parameters') -> 'returns the product of a and b':
    """
    This is some documentation(docstring) about the function 'my_func()'
    :param a:
    :param b:
    :param args:
    :param c:
    :param d:
    :param kwargs:
    :return:
    """
    return a * b


print(my_func(2, 'x', c='c'))
print(my_func.__annotations__)
print(my_func.__doc__)