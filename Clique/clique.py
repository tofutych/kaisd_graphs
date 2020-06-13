import numpy as np
import tkinter
from tkinter import messagebox, Scrollbar, VERTICAL
from tkinter.filedialog import askopenfile

FILE_NAME = tkinter.NONE

MAX = 100

store = [0] * MAX

graph = np.zeros((MAX, MAX))

d = [0] * MAX


def save_file():
    data = text.get('1.0', tkinter.END)
    out = open(FILE_NAME, 'w')
    out.write(data)
    out.close()


def open_file():
    global FILE_NAME
    inp = askopenfile(mode='r')
    if inp is None:
        return
    FILE_NAME = inp.name
    data = inp.read()
    text.delete('1.0', tkinter.END)
    text.insert('1.0', data)


def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()


def execute():
    max_clique = cliques[0]
    for clq in cliques:
        if len(clq) > len(max_clique):
            max_clique = clq
    word = ''
    with open('output.txt') as f:
        for s in max_clique:
            word += str(s) + ' -> '
    word = word[0:len(word) - 4]
    print(word)
    f = open('output.txt', 'w')
    f.write(word)
    f.close()
    f = open('input.txt', 'r')
    data = f.read()
    text.delete('1.0', tkinter.END)
    text.insert('1.0', data)
    f.close()

    messagebox._show('Result', 'Max clique is:\n' + word)


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


def make_edges(path):
    lines = open(path).read().splitlines()  # stroki fila
    result = []
    for line in lines:
        result.append(list(map(int, line.split())))
    return result


edges = make_edges('input.txt')
nodes = []
for edge in edges:
    for node in edge:
        nodes.append(node)

size = len(edges)
n = len(set(nodes))
cliques = []

for j in range(2, size):
    for i in range(size):
        graph[edges[i][0]][edges[i][1]] = 1
        graph[edges[i][1]][edges[i][0]] = 1
        d[edges[i][0]] += 1
        d[edges[i][1]] += 1
    findCliques(0, 1, j)

print(cliques)

root = tkinter.Tk()
root.title('Max clique')
root.geometry('400x400')
root.resizable(False, False)
center(root)

text = tkinter.Text(root, width=100, height=100, wrap='word')
scroll_bar = Scrollbar(root, orient=VERTICAL, command=text.yview)
scroll_bar.pack(side='right', fill='y')
text.configure(yscrollcommand=scroll_bar.set)
text.pack()

menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)

file_menu = tkinter.Menu(menu_bar, tearoff=False)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_file)

menu_bar.add_cascade(label='File', menu=file_menu)
menu_bar.add_cascade(label='Execute', command=execute)

root.mainloop()
