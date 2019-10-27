
def list_edges(graph):
    return [[i, j] for i, row in enumerate(graph) for j, connection in enumerate(row) if connection > 0]

def save_edges(graph, filename):
    out = ""
    for x, y in list_edges(graph):
        out += str(x) + " " + str(y) + "\n"

    f = open(filename, "w")
    f.write(out)
    f.close()


graph =  \
    [
     [2, 1, 0, 0, 1, 0],
     [1, 0, 1, 0, 1, 0],
     [0, 1, 0, 1, 0, 0],
     [0, 0, 1 ,0, 1, 1],
     [1, 1, 0, 1, 0, 0],
     [0, 0, 0, 1, 0, 0]
    ]

save_edges(graph, "data.out")
