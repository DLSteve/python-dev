

GRAPH = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


def df_search_loop(graph, start):
    """Depth-First Loop"""
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

def df_search_recurseve(graph, start, visited=None):
    """Depth-First Recurseve"""
    if visited is None:
        visited = set()
    visited.add(start)
    for nxt in graph[start] - visited:
        df_search_recurseve(graph, nxt, visited)
    return visited

def dfs_paths(graph, start, goal):
    """Depth-First Paths"""
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for nxt in graph[vertex] - set(path):
            if nxt == goal:
                yield path + [nxt]
            else:
                stack.append((nxt, path + [nxt]))

def bf_search_loop(graph, start):
    """Breath-First Loop"""
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

def bf_search_paths(graph, start, goal):
    """Breath-First Paths"""
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

def bfs_shortest_path(graph, start, goal):
    """Breath-First sShortest Path"""
    try:
        return next(bf_search_paths(graph, start, goal))
    except StopIteration:
        return None


if __name__ == "__main__":
    print(df_search_loop(GRAPH, 'A'))
    print(df_search_recurseve(GRAPH, 'A'))
    print(list(dfs_paths(GRAPH, 'A', 'F')))
    print(bf_search_loop(GRAPH, 'A'))
    print(list(bf_search_paths(GRAPH, 'A', 'F')))
    print(bfs_shortest_path(GRAPH, 'A', 'F'))
