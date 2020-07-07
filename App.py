import tkinter as tk
from tkinter import messagebox as mbox
from AutoSegregate import AutoSegregateFiles


root = tk.Tk()
root.title("Auto Segregate Files")


def fix_directory(path):
    fixed = ""
    for character in path:
        if character == "\\":
            fixed += "/"
        else:
            fixed += character
    if fixed[-1] != "/":
        fixed += "/"
    return fixed


def process():
    raw_directory = r"%s" % entry.get()
    if len(raw_directory) == 0:
        mbox.showerror(title="No Directory", message="You didn't enter a directory!")
    else:
        try:
            fixed_directory = fix_directory(raw_directory)
            segregation = AutoSegregateFiles(fixed_directory)
            segregation.segregate()
        except FileNotFoundError:
            mbox.showerror(title="Directory Not Found", message="Can't Find the Directory Specified")
        else:
            mbox.showinfo(title="Success!", message="Files Successfully Segregated!")


def hover_button(event):
    button = event.widget
    button.config(bg="#ade88a")


def leave_button(event):
    button = event.widget
    button.config(bg="#89cf60")


def hover_entry(event):
    entry = event.widget
    entry.config(bg="#c6ddb8")


def leave_entry(event):
    entry = event.widget
    entry.config(bg="#b1cca2")


pane = tk.Canvas(root, height="300", width="600", bg="#deeed5")
pane.pack()

label = tk.Label(pane, text="Enter Directory", font=("calibri", 20), bg="#deeed5")
label.place(relx=0.1, rely=0.1, anchor="nw")

entry = tk.Entry(pane, font=("calibri", 20), bg="#b1cca2")
entry.bind("<Enter>", hover_entry)
entry.bind("<Leave>", leave_entry)
entry.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.15)

button = tk.Button(pane, bg="#89cf60", activebackground="#0c782b",
    text="Segregate", font=("calibri", 26), command=process)
button.bind("<Enter>", hover_button)
button.bind("<Leave>", leave_button)
button.place(relx=0.1, rely=0.55, relheight=0.15, relwidth=0.3)

root.mainloop()
