import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from data_structures.heaps import Heap

# --- insert ---
h = Heap(10)
h.insert(5)
h.insert(10)
h.insert(3)
h.insert(15)
assert h.array[0] == 15      # max at root
assert h.length == 4

full = Heap(2)
full.insert(1)
full.insert(2)
try:
    full.insert(3)
    assert False
except OverflowError:
    pass
print("insert: OK")

# --- pop ---
h = Heap(10)
for v in [5, 10, 3, 15, 8]:
    h.insert(v)
assert h.pop() == 15         # removes max
assert h.pop() == 10
assert h.pop() == 8
assert h.length == 2

empty = Heap(5)
try:
    empty.pop()
    assert False
except IndexError:
    pass
print("pop: OK")

# --- peek ---
h = Heap(5)
h.insert(7)
h.insert(2)
h.insert(9)
assert h.peek() == 9         # max without removing
assert h.length == 3         # unchanged

empty = Heap(5)
try:
    empty.peek()
    assert False
except IndexError:
    pass
print("peek: OK")

# --- is_empty ---
h = Heap(5)
assert h.is_empty() == True
h.insert(1)
assert h.is_empty() == False
print("is_empty: OK")

# --- is_full ---
h = Heap(2)
assert h.is_full() == False
h.insert(1)
h.insert(2)
assert h.is_full() == True
print("is_full: OK")

print("\nAll tests passed.")
