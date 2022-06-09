class Node:
    def __init__(self, value, leaves=[]):
        self.value = value
        self.leaves = leaves
    
    def add_leaf(self, leaf):
        self.leaves.append(leaf)
    
    def __repr__(self):
        return str({self.value: self.leaves})

class Graph:
    def __init__(self, nodes=[]):
        self.nodes = nodes
    
    def __repr__(self):
        return str(self.nodes)
    
    def get_node_from_str(self, x):
        for i in self.nodes:
            if x == i.value:
                return i
        return
    
    def dfs(self, x=None, visited=set()):
        if x is None:
            x = self.nodes[0]
        visited.add(x)
        print(x.value)
        for leaf in x.leaves:
            if leaf not in visited:
                self.dfs(self.get_node_from_str(leaf), visited)
        return visited
    
    def bfs(self, x=None):
        if x is None:
            x = self.nodes[0]
        queue = [x]
        visited = [x]
        while queue:
            x = queue.pop(0)
            print(x.value)
            for i in x.leaves:
                queue.append(self.get_node_from_str(i))
                visited.append(self.get_node_from_str(i))
        return visited
    
if __name__ == "__main__":
    A = Node(value='A', leaves=['B','C'])
    B = Node(value='B', leaves=['D', 'E'])
    C = Node(value='C', leaves=['F'])
    D = Node(value='D')
    E = Node(value='E')
    F = Node(value='F')
    
    a_graph = Graph([A,B,C,D,E,F])
    #print(a_graph.get_node_from_str('B'))
    a_graph.bfs()