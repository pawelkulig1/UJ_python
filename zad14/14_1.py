def list_nodes(graph):
    return [i for i, _ in enumerate(graph[0])]

def list_edges(graph):
    return [[i, j] for i, row in enumerate(graph) for j, connection in enumerate(row) if connection > 0]

def count_nodes(graph):
    return len(graph[0])

def count_edges(graph):
    return round(sum([y for x in graph for y in x if y > 0 ])/2)

graph =  \
    [
     [2, 1, 0, 0, 1, 0],
     [1, 0, 1, 0, 1, 0],
     [0, 1, 0, 1, 0, 0],
     [0, 0, 1 ,0, 1, 1],
     [1, 1, 0, 1, 0, 0],
     [0, 0, 0, 1, 0, 0]
    ]

print(list_edges(graph))
print(list_nodes(graph))
print(count_nodes(graph))
print(count_edges(graph))
