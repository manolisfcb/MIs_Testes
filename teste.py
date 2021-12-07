import tkinter as tk
from TkinterDnD2 import *

def drop_indide_listbox(event):
    listb.insert("end", event.data)
    tbox.delete("1.0", "end")
    if event.data.endswith(".txt"):
        with open(event.data, "r") as file:
            for line in file:
                line = line.strip()
                tbox.insert("end", f"{line} \n")

def drop_inside_textbox(event):
    tbox.delete("1.0", "end")
    if event.data.endswith(".txt"):
        with open(event.data, "r") as file:
            for line in file:
                line = line.strip()
                tbox.insert("end", f"{line} \n")





root = TkinterDnD.Tk()
root.geometry("800x500")


listb = tk.Listbox(root, selectmode=tk.SINGLE, background="#ffe0d6")
listb.pack(fill=tk.X)
listb.drop_target_register(DND_FILES)
listb.dnd_bind("<<Drop>>",drop_indide_listbox)



tbox = tk.Text(root)
tbox.pack()
tbox.drop_target_register(DND_FILES)
tbox.dnd_bind("<<Drop>>",drop_inside_textbox)



root.mainloop()