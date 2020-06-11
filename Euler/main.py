import tkinter
from tkinter import messagebox, Scrollbar, VERTICAL
from tkinter.filedialog import askopenfile
from euler import check_euler, add_graph

FILE_NAME = tkinter.NONE


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
    check_euler(add_graph('input.txt'), 10, 'output.txt')

    f = open('input.txt', 'r')
    data = f.read()
    text.delete('1.0', tkinter.END)
    text.insert('1.0', data)

    message = ''
    for item in open('output.txt').read().splitlines():
        message += ' '.join(item.split()) + "\n"
    messagebox._show('Result', message)


root = tkinter.Tk()
root.title('IsEulerian?')
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
# # вот он в input txt
# G1 = {1: [2, 3, 4], 2: [1, 3], 3: [1, 2], 4: [1, 5], 5: [4]}

# # в нем ейлеров циклопыч
# G2 = {1: [2, 3, 4, 5], 2: [1, 3], 3: [1, 2], 4: [1, 5], 5: [1, 4]}

# # в нем все хуева
# G3 = {1: [2, 3, 4], 2: [1, 3, 4], 3: [1, 2], 4: [1, 2, 5], 5: [4]}

# # а вот в этом найдем циклик
# G4 = {1: [2, 3], 2: [1, 3], 3: [1, 2]}
