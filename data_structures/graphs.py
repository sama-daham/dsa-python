class Graph:
    def __init__(self):
        self.graph = {}
    def add_node(self, node):
        if node not in self.graph:
            self.graph[node]=[]
    def add_edge(self, node1, node2):
        if node1 not in self.graph or node2 not in self.graph:
            raise KeyError("Node does not exist")
        self.graph[node1].append(node2)
        self.graph[node2].append(node1)
    def get_neighbors(self, node):
        return self.graph[node]
    
    def remove_node(self, node):
        for i in self.get_neighbors(node):
            self.graph[i].remove(node)
        del(self.graph[node])
    def remove_edge(self, node1, node2):
        self.graph[node1].remove(node2)
        self.graph[node2].remove(node1)


    
    def bfs(self, start):
        visited = set()
        queue = [start]
        visited.add(start)
        while queue:
            node = queue.pop(0)
            for neighbor in self.get_neighbors(node):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return visited
    
    def dfs(self, start):
        visited = set()
        stack = [start]
        while stack:
            node = stack.pop()
            if node not in visited:
                    visited.add(node)
                    for neighbor in self.get_neighbors(node):
                        if neighbor not in visited:
                            stack.append(neighbor)
        return list(visited)