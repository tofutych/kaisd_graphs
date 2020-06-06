def add_graph(path):
    try:
        file = open(path)
        vertex = file.read().splitlines()
        graph = {i + 1: list(map(int, vertex[i].split()))
                 for i in range(0, len(vertex))}
        return graph
    except IOError:
        print("File error!")
    finally:
        file.close()


def dfs(u, graph, visited_edge, path=[]):
    path = path + [u]
    for v in graph[u]:
        if visited_edge[u][v] is False:
            visited_edge[u][v], visited_edge[v][u] = True, True
            path = dfs(v, graph, visited_edge, path)
    return path


# for checking in graph has euler path or circuit
def check_circuit_or_path(graph, max_node):
    odd_degree_nodes = 0
    odd_node = -1
    for i in range(max_node):
        if i not in graph.keys():
            continue
        if len(graph[i]) % 2 == 1:
            odd_degree_nodes += 1
            odd_node = i
    if odd_degree_nodes == 0:
        return 1, odd_node
    if odd_degree_nodes == 2:
        return 2, odd_node
    return 3, odd_node


def check_euler(graph, max_node, output_path):
    visited_edge = [[False for _ in range(max_node + 1)]
                    for _ in range(max_node + 1)]
    check, odd_node = check_circuit_or_path(graph, max_node)
    try:
        file = open(output_path, 'a')
        if check == 3:
            file.write("Graph is not Eulerian!\nno path\n")
            return
        start_node = 1
        if check == 2:
            start_node = odd_node
            file.write("Graph has a Euler path -> semi-Eulerian graph!\n")
        if check == 1:
            file.write("Graph has a Euler cycle -> Eulerian graph!\n")
        path = dfs(start_node, graph, visited_edge)
        for i, v in enumerate(path):
            if i == len(path) - 1:
                file.write(str(v) + '\n\n')
                break
            file.write(str(v) + " -> ")
    except IOError:
        print("File error!")
    finally:
        file.close()
