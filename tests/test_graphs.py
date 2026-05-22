import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from data_structures.graphs import Graph

# --- add_node ---
g = Graph()
g.add_node("A")
g.add_node("B")
assert "A" in g.graph
assert "B" in g.graph
g.add_node("A")            # duplicate — should be ignored
assert len(g.graph) == 2
print("add_node: OK")

# --- add_edge ---
g = Graph()
g.add_node("A")
g.add_node("B")
g.add_edge("A", "B")
assert "B" in g.graph["A"]
assert "A" in g.graph["B"]
try:
    g.add_edge("A", "Z")   # node doesn't exist
    assert False
except KeyError:
    pass
print("add_edge: OK")

# --- get_neighbors ---
g = Graph()
g.add_node("A")
g.add_node("B")
g.add_node("C")
g.add_edge("A", "B")
g.add_edge("A", "C")
assert set(g.get_neighbors("A")) == {"B", "C"}
print("get_neighbors: OK")

# --- remove_edge ---
g = Graph()
g.add_node("A")
g.add_node("B")
g.add_edge("A", "B")
g.remove_edge("A", "B")
assert "B" not in g.graph["A"]
assert "A" not in g.graph["B"]
print("remove_edge: OK")

# --- remove_node ---
g = Graph()
g.add_node("A")
g.add_node("B")
g.add_node("C")
g.add_edge("A", "B")
g.add_edge("A", "C")
g.remove_node("A")
assert "A" not in g.graph
assert "A" not in g.graph["B"]
assert "A" not in g.graph["C"]
print("remove_node: OK")

# --- bfs ---
g = Graph()
for node in ["A", "B", "C", "D"]:
    g.add_node(node)
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
result = g.bfs("A")
assert set(result) == {"A", "B", "C", "D"}   # all nodes reachable
print("bfs: OK")

# --- dfs ---
g = Graph()
for node in ["A", "B", "C", "D"]:
    g.add_node(node)
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
result = g.dfs("A")
assert set(result) == {"A", "B", "C", "D"}   # all nodes reachable
print("dfs: OK")

print("\nAll tests passed.")
