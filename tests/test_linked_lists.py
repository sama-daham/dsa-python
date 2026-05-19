import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from data_structures.linked_lists import Node, Linked_List

# --- append ---
ll = Linked_List()
ll.append(1)
ll.append(2)
ll.append(3)
assert ll.length == 3
assert ll.head.val == 1
assert ll.head.next.val == 2
assert ll.head.next.next.val == 3
print("append: OK")

# --- prepend ---
ll = Linked_List()
ll.append(2)
ll.prepend(1)
assert ll.head.val == 1
assert ll.head.next.val == 2
assert ll.length == 2
print("prepend: OK")

# --- get ---
ll = Linked_List()
ll.append(10)
ll.append(20)
ll.append(30)
assert ll.get(0) == 10
assert ll.get(1) == 20
assert ll.get(2) == 30
try:
    ll.get(-1)
    assert False
except IndexError:
    pass
try:
    ll.get(5)
    assert False
except IndexError:
    pass
print("get: OK")

# --- insert ---
ll = Linked_List()
ll.append(1)
ll.append(3)
ll.insert(1, 2)
assert ll.get(0) == 1
assert ll.get(1) == 2
assert ll.get(2) == 3
assert ll.length == 3

ll2 = Linked_List()
ll2.append(2)
ll2.insert(0, 1)
assert ll2.get(0) == 1
assert ll2.get(1) == 2

try:
    ll.insert(99, 0)
    assert False
except IndexError:
    pass
print("insert: OK")

# --- delete ---
ll = Linked_List()
ll.append(1)
ll.append(2)
ll.append(3)
ll.delete(1)
assert ll.get(0) == 1
assert ll.get(1) == 3
assert ll.length == 2

ll.delete(0)
assert ll.head.val == 3
assert ll.length == 1

ll.delete(0)
assert ll.head is None
assert ll.length == 0

try:
    ll.delete(0)
    assert False
except IndexError:
    pass
print("delete: OK")

# --- find ---
ll = Linked_List()
ll.append(10)
ll.append(20)
ll.append(30)
assert ll.find(20) == 1
assert ll.find(99) == -1
print("find: OK")

# --- contains ---
ll = Linked_List()
ll.append(7)
assert ll.contains(7) == True
assert ll.contains(8) == False
print("contains: OK")

print("\nAll tests passed.")
