# from tkinter import *


# def center(win):
#     """
#     centers a tkinter window
#     :param win: the root or Toplevel window to center
#     """
#     win.update_idletasks()
#     width = win.winfo_width()
#     frm_width = win.winfo_rootx() - win.winfo_x()
#     win_width = width + 2 * frm_width
#     height = win.winfo_height()
#     titlebar_height = win.winfo_rooty() - win.winfo_y()
#     win_height = height + titlebar_height + frm_width
#     x = win.winfo_screenwidth() // 2 - win_width // 2
#     y = win.winfo_screenheight() // 2 - win_height // 2
#     win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
#     win.deiconify()


# if __name__ == "__main__":
#     root = Tk();
#     root.title('Is Eulerian?')
#     root.geometry('400x400')
#     center(root)
#     root.mainloop()


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


def main():
    # G1 = {1: [2, 3, 4], 2: [1, 3], 3: [1, 2], 4: [1, 5], 5: [4]}
    # G2 = {1: [2, 3, 4, 5], 2: [1, 3], 3: [1, 2], 4: [1, 5], 5: [1, 4]}
    # G3 = {1: [2, 3, 4], 2: [1, 3, 4], 3: [1, 2], 4: [1, 2, 5], 5: [4]}
    # G4 = {1: [2, 3], 2: [1, 3], 3: [1, 2]}
    # G5 = {
    #     1: [],
    #     2: []
    #     # all degree is zero
    # }
    max_node = 10
    input_path = 'input.txt'
    output_path = 'output.txt'
    check_euler(add_graph(input_path), max_node, output_path)
    # print("\n\nG2")
    # check_euler(G2, max_node)
    # print("\n\nG3")
    # check_euler(G3, max_node)
    # print("\n\nG4")
    # check_euler(G4, max_node)
    # print("\n\nG5")
    # check_euler(G5, max_node)


if __name__ == "__main__":
    main()
