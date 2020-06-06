from tkinter import Tk, messagebox, Button, LEFT
from euler import check_euler, add_graph


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


def inputText():
    message = ''
    for item in open('input.txt').read().splitlines():
        message += '\t'.join(item.split()) + "\n"
    messagebox._show('input.txt', message)


def outputText():
    message = ''
    for item in open('output.txt').read().splitlines():
        message += ' '.join(item.split()) + "\n"
    messagebox._show('output.txt', message)


def exec():
    try:
        check_euler(add_graph(input_path), max_node, output_path)
        messagebox._show('Успех!', 'гатова')
    except Exception:
        messagebox._show("Варнинг!")


root = Tk()
root.title('Euler')
root.geometry('165x100')
root.resizable(width=False, height=False)
center(root)
input_button = Button(root, text='input', command=inputText)
output_button = Button(root, text='output', command=outputText)
max_node = 10
input_path = 'input.txt'
output_path = 'output.txt'
execute_button = Button(root, text='execute', command=exec)
input_button.pack(side=LEFT, padx=5)
output_button.pack(side=LEFT, padx=5)
execute_button.pack(side=LEFT, padx=5)
root.mainloop()


# # вот он в input txt
# G1 = {1: [2, 3, 4], 2: [1, 3], 3: [1, 2], 4: [1, 5], 5: [4]}

# # в нем ейлеров циклопыч
# G2 = {1: [2, 3, 4, 5], 2: [1, 3], 3: [1, 2], 4: [1, 5], 5: [1, 4]}

# # в нем все хуева
# G3 = {1: [2, 3, 4], 2: [1, 3, 4], 3: [1, 2], 4: [1, 2, 5], 5: [4]}

# # а вот в этом найдем циклик
# G4 = {1: [2, 3], 2: [1, 3], 3: [1, 2]}
