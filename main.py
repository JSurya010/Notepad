import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog
import os

def createwidget():
    global TextArea
    TextArea = Text(root)
    TextArea.grid(sticky=N + S + W + E)

    menubar = Menu(root)
    root.config(menu=menubar)
    
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=NewFile)
    filemenu.add_command(label="Open", command=Openfile)
    filemenu.add_command(label="Save", command=SaveFile)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=exit_program)
    menubar.add_cascade(label="File", menu=filemenu)

    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Cut", command=cut)
    editmenu.add_command(label="Copy", command=copy)
    editmenu.add_command(label="Paste", command=paste)
    menubar.add_cascade(label="Edit", menu=editmenu)

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="About NotePad", command=help)
    menubar.add_cascade(label="Help", menu=helpmenu)

def NewFile():
    global TextArea
    root.title("Untitled - NotePad")
    TextArea.delete(1.0, END)

def Openfile():
    global TextArea, file
    file = filedialog.askopenfilename(defaultextension='.txt', filetypes=[("All files", "*.*"), ("Text Documents", "*.txt")])

    if file:
        root.title(os.path.basename(file) + " - NotePad")
        TextArea.delete(1.0, END)
        with open(file, "r") as f:
            TextArea.insert(1.0, f.read())

def SaveFile():
    global TextArea, file
    if file is None:
        file = filedialog.asksaveasfilename(initialfile="Untitled.txt", defaultextension='.txt', filetypes=[("All files", "*.*"), ("Text Documents", "*.txt")])

    if file:
        with open(file, "w") as f:
            f.write(TextArea.get(1.0, END))
        root.title(os.path.basename(file) + " - NotePad")

def exit_program():
    root.destroy()

def cut():
    global TextArea
    TextArea.event_generate("<<Cut>>")

def copy():
    global TextArea
    TextArea.event_generate("<<Copy>>")

def paste():
    global TextArea
    TextArea.event_generate("<<Paste>>")

def help():
    messagebox.showinfo("NotePad", "This Simple NotePad is made by Surya")

root = tk.Tk()
root.title("Untitled - NotePad")
file = None

createwidget()

root.mainloop()
