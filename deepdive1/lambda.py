fn = lambda x: x ** 2
print(fn(3))


# higher order function
def fn(x, ln):
    return ln(x)


# regular function
def sq(x):
    return x ** 2


# using lambda
print(fn(3, lambda x: x ** 2))
# using regular func
print(fn(3, sq))


def my_func(ln, *args, **kwargs):
    print(args, kwargs)
    return ln(*args, **kwargs)


print(my_func(lambda x: x ** 2, 2))
print(my_func(lambda x, y: x ** 2 + y, 1, y=20))


dictn = {"abc": 123, "ghi": 343, "def": 50}
print(dictn)
print(sorted(dictn))
print(sorted(dictn.values()))
print(sorted(dictn, key=lambda e: dictn[e]))
print(sorted(dictn.items(), key=lambda item: item[1]))
print(dictn.items())
list_temp = []
for item in dictn.items():
    print(item[1])
    list_temp.append(item[1])

print(list_temp)

# numerical values
dictionary = {"raj": 2, "striver": 3, "vikram": 4}
print(dictionary.values())

# string values
dictionary = {"geeks": "5", "for": "3", "Geeks": "5"}
print(dictionary.values())
print(list(dictionary.values())  )



