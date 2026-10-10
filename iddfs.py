
# Iterative Deepening Search (IDS)

def dls(graph, node, goal, depth):
    if node == goal:
        return [node]

    if depth == 0:
        return None

    for neighbor in graph.get(node, []):
        path = dls(graph, neighbor, goal, depth - 1)
        if path:
            return [node] + path

    return None


def ids(graph, start, goal):
    depth = 0

    while True:
        print("Searching at depth:", depth)
        result = dls(graph, start, goal, depth)

        if result:
            return result

        depth += 1


# Graph representation
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

start = 'A'
goal = 'G'

path = ids(graph, start, goal)

print("\nGoal found!")
print("Path:", " -> ".join(path))
