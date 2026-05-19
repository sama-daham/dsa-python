import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from data_structures.stacks import Stack

# --- push ---
s = Stack(3)
s.push(1)
s.push(2)
s.push(3)
assert s.length == 3
assert s.array[0] == 1
assert s.array[2] == 3
assert s.push(4) == "Error"    # full
print("push: OK")

# --- pop ---
s = Stack(3)
s.push(1)
s.push(2)
assert s.pop() == 2
assert s.length == 1
assert s.array[1] is None      # cleared

empty = Stack(2)
assert empty.pop() == -1       # empty stack
print("pop: OK")

# --- peek ---
s = Stack(3)
s.push(5)
s.push(10)
assert s.peek() == 10
assert s.length == 2           # not removed

empty = Stack(2)
assert empty.peek() == -1
print("peek: OK")

# --- is_empty ---
s = Stack(2)
assert s.is_empty() == True
s.push(1)
assert s.is_empty() == False
print("is_empty: OK")

# --- is_full ---
s = Stack(2)
assert s.is_full() == False
s.push(1)
s.push(2)
assert s.is_full() == True
print("is_full: OK")

print("\nAll tests passed.")
