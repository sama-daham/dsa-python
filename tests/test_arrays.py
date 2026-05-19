import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from data_structures.arrays import Array

# --- get ---
a = Array(3)
a.array[0] = 10
a.length = 1
assert a.get(0) == 10
try:
    a.get(1)
    assert False
except IndexError:
    pass
try:
    a.get(-1)
    assert False
except IndexError:
    pass
print("get: OK")

# --- set ---
a = Array(3)
a.set(0, 5)
assert a.array[0] == 5
try:
    a.set(5, 1)
    assert False
except IndexError:
    pass
print("set: OK")

# --- append ---
a = Array(3)
a.append(1)
a.append(2)
a.append(3)
assert a.length == 3
try:
    a.append(4)
    assert False
except OverflowError:
    pass
print("append: OK")

# --- insert ---
a = Array(5)
a.append(1)
a.append(2)
a.append(4)
a.insert(2, 3)
assert a.array[2] == 3
assert a.array[3] == 4
assert a.length == 4

full = Array(2)
full.append(1)
full.append(2)
try:
    full.insert(0, 0)
    assert False
except OverflowError:
    pass
print("insert: OK")

# --- delete ---
a = Array(4)
a.append(1)
a.append(2)
a.append(3)
a.delete(1)
assert a.array[0] == 1
assert a.array[1] == 3
assert a.length == 2
assert a.array[2] is None
try:
    a.delete(5)
    assert False
except IndexError:
    pass
print("delete: OK")

# --- find ---
a = Array(4)
a.append(10)
a.append(20)
a.append(30)
assert a.find(20) == 1
assert a.find(99) == -1
print("find: OK")

# --- contains ---
a = Array(3)
a.append(7)
assert a.contains(7) == True
assert a.contains(8) == False
print("contains: OK")

print("\nAll tests passed.")
