import networkx as nx

G = nx.DiGraph()

for line in open("input.txt"):
    parts = line.strip().split(': ')
    node = parts[0]
    G.add_node(node)
    edges = parts[1].split()
    for edge in edges:
        G.add_edge(node, edge)

print(len(list(nx.all_simple_paths(G, 'you', 'out'))))
