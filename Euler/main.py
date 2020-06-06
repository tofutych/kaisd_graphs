from tkinter import Tk


def center(win):
    """
    centers a tkinter window
    :param win: the root or Toplevel window to center
    """
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


def main():
    root = Tk()
    root.title('Is Eulerian?')
    root.geometry('400x400')
    center(root)
    root.mainloop()


if __name__ == "__main__":
    main()

# from euler import check_euler, add_graph


# max_node = 10
# input_path = 'input.txt'
# output_path = 'output.txt'
# check_euler(add_graph(input_path), max_node, output_path)
