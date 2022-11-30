class DirectedGraph:
    def __init__(self):
        self.nodes = []
        self.edges = {}
    
    def add_node(self, node):
        if node in self.nodes:
            return
        self.nodes.append(node)
        self.edges[node] = []

    def add_edge(self, src, dest):
        if src not in self.nodes:
            self.add_node(src)

        if dest not in self.nodes:
            self.add_node(dest)

        #create a reference for the node adjacent to the src node
        adjacent_nodes = self.edges[src]

        #no need to do anything is the dest is already adjacent to  the src node
        if dest in adjacent_nodes: 
            return

     