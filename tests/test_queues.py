import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from data_structures.queues import Queue

# --- enqueue ---
q = Queue(3)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
assert q.length == 3
assert q.array[0] == 1
assert q.array[2] == 3
try:
    q.enqueue(4)
    assert False
except OverflowError:
    pass
print("enqueue: OK")

# --- dequeue ---
q = Queue(3)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
assert q.dequeue() == 1        # FIFO: first in, first out
assert q.length == 2
assert q.array[0] == 2
assert q.array[2] is None      # cleared

empty = Queue(2)
try:
    empty.dequeue()
    assert False
except IndexError:
    pass
print("dequeue: OK")

# --- peek ---
q = Queue(3)
q.enqueue(5)
q.enqueue(10)
assert q.peek() == 5           # front of queue
assert q.length == 2           # not removed

empty = Queue(2)
try:
    empty.peek()
    assert False
except IndexError:
    pass
print("peek: OK")

# --- is_empty ---
q = Queue(2)
assert q.is_empty() == True
q.enqueue(1)
assert q.is_empty() == False
print("is_empty: OK")

# --- is_full ---
q = Queue(2)
assert q.is_full() == False
q.enqueue(1)
q.enqueue(2)
assert q.is_full() == True
print("is_full: OK")

print("\nAll tests passed.")
