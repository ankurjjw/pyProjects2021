import time


def calc(a):
    print(a)
    for i in range(10000000):
        b = a * 2


start = time.perf_counter()
calc(2**10000)
end = time.perf_counter()

print(end - start)
print(10/5)
