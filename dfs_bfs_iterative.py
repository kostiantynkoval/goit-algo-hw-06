def dfs_iterative(graph, start_vertex):
    visited = list()
    stack = [start_vertex]

    while stack:
        vertex = stack.pop()

        if vertex not in visited:
            visited.append(vertex)
            stack.extend(reversed(graph[vertex]))

    return visited


from collections import deque

def bfs_iterative(graph, start):
    visited = list()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()

        if vertex not in visited:
            visited.append(vertex)
            queue.extend([x for x in graph[vertex] if x not in visited])

    return visited


def dijkstra_iterative(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.nodes.keys())

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, edge_data in graph[current_vertex].items():
            distance = float(round(distances[current_vertex] + edge_data[0]['length'], 2))

            if distance < distances[neighbor]:
                distances[neighbor] = float(round(distance,2))

        unvisited.remove(current_vertex)

    return distances