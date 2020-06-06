from tkinter import *
import os
 
def but_open():
    text_output.delete(1.0, END)
    _path = "{}\\{}".format(os.getcwd(),text_input.get())
    _in_path = open(_path,'r')
    text_output.insert(INSERT,_in_path.read())
    _in_path.close()
 
def but_save():
    _save_path = "{}\\{}".format(os.getcwd(), text_input.get())
    _out_path = open(_save_path, 'w')
    _out_path.write(text_output.get(1.0, END))
    _out_path.close()
    text_output.delete(1.0, END)
 
 
root = Tk()
root.geometry('600x600')
root.minsize(width=200, height=100)
active_frame = Frame(root)
 
text_input = Entry(active_frame, width='0')
text_output = Text(width='1', wrap=NONE)
scroll_ver = Scrollbar(command=text_output.yview)
scroll_hor = Scrollbar(command=text_output.xview, orient=HORIZONTAL)
text_output.config(yscrollcommand=scroll_ver.set, xscrollcommand=scroll_hor.set)
button_open = Button(active_frame,text='Открыть', command=but_open)
button_save = Button(active_frame,text='Сохранить', command=but_save)
 
text_input.pack(side=LEFT, expand=1, fill=X)
button_open.pack(side=LEFT, padx=1)
button_save.pack(side=LEFT, padx=1)
active_frame.pack(side=TOP, fill=X, padx=17, pady=1)
scroll_hor.pack(side=BOTTOM, fill=X)
text_output.pack(expand=1, side=LEFT, fill=BOTH, anchor=S)
scroll_ver.pack(side=RIGHT, fill=Y)
 
root.mainloop()