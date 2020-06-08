import numpy as np

MAX = 100

store = [0] * MAX

graph = np.zeros((MAX, MAX))

d = [0] * MAX


def is_clique(b):
    for i in range(1, b):
        for j in range(i + 1, b):
            if (graph[store[i]][store[j]] == 0):
                return False

    return True


def print_cli(n):
    clique = []
    for i in range(1, n):
        print(store[i], end="\t")
        clique.append(store[i])
    cliques.append(clique)
    print("\n")


def findCliques(i, l, s):
    for j in range(i + 1, n - (s - l) + 1):
        if (d[j] >= s - 1):
            store[l] = j
            if (is_clique(l + 1)):
                if (l < s):
                    findCliques(j, l + 1, s)
                else:
                    print_cli(l + 1)


if __name__ == "__main__":
    edges = [[1, 2],
             [2, 3],
             [3, 1],
             [4, 3],
             [4, 5],
             [5, 3]]
    nodes = []
    for edge in edges:
        for node in edge:
            nodes.append(node)
    k = 3  # clique size
    size = len(edges)
    n = len(set(nodes))
    cliques = []
    # for i in range(size):
    #     graph[edges[i][0]][edges[i][1]] = 1
    #     graph[edges[i][1]][edges[i][0]] = 1
    #     d[edges[i][0]] += 1
    #     d[edges[i][1]] += 1
    # findCliques(0, 1, k)

    for j in range(2, size):
        for i in range(size):
            graph[edges[i][0]][edges[i][1]] = 1
            graph[edges[i][1]][edges[i][0]] = 1
            d[edges[i][0]] += 1
            d[edges[i][1]] += 1
        findCliques(0, 1, j)

    print(cliques)
    max_clique = cliques[0]
    for clq in cliques:
        if len(clq) > len(max_clique):
            max_clique = clq

    print(max_clique)
