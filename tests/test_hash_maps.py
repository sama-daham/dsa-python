import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from data_structures.hash_maps import Hash_Map

# --- set ---
h = Hash_Map(10)
h.set("a", 1)
h.set("b", 2)
assert h.length == 2
h.set("a", 99)             # update existing key
assert h.get("a") == 99
assert h.length == 2       # length unchanged on update
print("set: OK")

# --- get ---
h = Hash_Map(10)
h.set("x", 10)
h.set("y", 20)
assert h.get("x") == 10
assert h.get("y") == 20
try:
    h.get("z")
    assert False
except KeyError:
    pass
print("get: OK")

# --- delete ---
h = Hash_Map(10)
h.set("a", 1)
h.set("b", 2)
h.delete("a")
assert h.length == 1
assert h.contains("a") == False
try:
    h.delete("z")
    assert False
except KeyError:
    pass
print("delete: OK")

# --- contains ---
h = Hash_Map(10)
h.set("a", 1)
assert h.contains("a") == True
assert h.contains("z") == False
print("contains: OK")

# --- keys ---
h = Hash_Map(10)
h.set("a", 1)
h.set("b", 2)
h.set("c", 3)
assert set(h.keys()) == {"a", "b", "c"}
print("keys: OK")

# --- values ---
h = Hash_Map(10)
h.set("a", 1)
h.set("b", 2)
h.set("c", 3)
assert set(h.values()) == {1, 2, 3}
print("values: OK")

print("\nAll tests passed.")
