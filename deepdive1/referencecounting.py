import sys
import ctypes

a = [1, 2, 3]
print(id(a))
print(sys.getrefcount(a))


print(ctypes.c_long.from_address(id(a)).value)

b = a
print(id(b))
print(sys.getrefcount(b))
print(ctypes.c_long.from_address(id(b)).value)


print(id(a))
print(sys.getrefcount(a))
print(ctypes.c_long.from_address(id(a)).value)

