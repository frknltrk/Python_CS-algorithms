graph = {}

def create_graph(**graph):
    return graph

def adjacents(vertex):
    return graph[vertex]

def BFA(source):
    distances = {}
    for vertex in graph.keys():
        distances[vertex] = 0

    OPEN = []   #       <-- QUEUE (FIFO) <--
    CLOSED = [] #       LIST <--

    OPEN.append(source)

    while len(OPEN) != 0:
        x = OPEN.pop(0)
        CLOSED.append(x)
        for adjacent in adjacents(x):           # ***
            if (adjacent not in OPEN) and (adjacent not in CLOSED):     # if the vertex (adjacent) is "brand-new"
                OPEN.append(adjacent)           # ***
                distances[adjacent] = distances[x] + 1
    return distances

graph = create_graph(A=['B', 'C'], B=['D', 'E'], C=['F'], D=['H'], E=[], F=['G'], G=['H'], H=[])
print(BFA('A'))