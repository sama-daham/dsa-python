import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from data_structures.trees import BST

# --- insert + search ---
t = BST()
t.insert(8)
t.insert(3)
t.insert(10)
t.insert(1)
t.insert(5)
assert t.search(8) == True
assert t.search(3) == True
assert t.search(1) == True
assert t.search(99) == False
t.insert(8)                    # duplicate — should be ignored
assert t.inorder().count(8) == 1
print("insert + search: OK")

# --- inorder ---
t = BST()
for v in [8, 3, 10, 1, 5, 9, 12]:
    t.insert(v)
assert t.inorder() == [1, 3, 5, 8, 9, 10, 12]   # sorted order
print("inorder: OK")

# --- preorder ---
t = BST()
for v in [8, 3, 10, 1, 5]:
    t.insert(v)
assert t.preorder() == [8, 3, 1, 5, 10]          # root first
print("preorder: OK")

# --- postorder ---
t = BST()
for v in [8, 3, 10, 1, 5]:
    t.insert(v)
assert t.postorder() == [1, 5, 3, 10, 8]         # root last
print("postorder: OK")

# --- delete leaf ---
t = BST()
for v in [8, 3, 10]:
    t.insert(v)
t.delete(10)
assert t.search(10) == False
assert t.inorder() == [3, 8]
print("delete leaf: OK")

# --- delete one child ---
t = BST()
for v in [8, 3, 10, 9]:
    t.insert(v)
t.delete(10)                   # 10 has one child (9)
assert t.search(10) == False
assert t.search(9) == True
print("delete one child: OK")

# --- delete two children ---
t = BST()
for v in [8, 3, 10, 9, 12]:
    t.insert(v)
t.delete(10)                   # 10 has two children, successor is 12
assert t.search(10) == False
assert t.search(9) == True
assert t.search(12) == True
assert t.inorder() == [3, 8, 9, 12]
print("delete two children: OK")

# --- delete missing key ---
t = BST()
t.insert(5)
try:
    t.delete(99)
    assert False
except KeyError:
    pass
print("delete missing: OK")

print("\nAll tests passed.")
