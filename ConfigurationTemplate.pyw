from tkinter import *
from tkinter.font import *
import sys

sys.path.insert(0, "Supporting Files")
import L3_Config_Template
import L2_Config_Template

COLOR = "gray5"

def main():
    root = Tk()
    root.config(bg = COLOR)
    cFont = Font(family = "Helvetica", size = 18)
    select = Label(root, text = "Select which template you want to configure:",\
        bg = COLOR, fg = "white", font = cFont)
    select.grid(padx = 20, pady = (40,0))
    frame = Frame(root, bg = COLOR, pady = 40)
    l2_label = Label(frame, text = "L2:", bg = COLOR, fg = "white", font = 36)
    l2_label.pack(side = LEFT)
    l2_val = BooleanVar()
    l2_check = Checkbutton(frame, bg = COLOR, var = l2_val,\
        command = lambda: l2Click(l2_val, l3_val))
    l2_check.pack(side = LEFT)
    l3_label = Label(frame, text = "L3:", bg = COLOR, fg = "white", font = 36)
    l3_label.pack(side = LEFT)
    l3_val = BooleanVar()
    l3_check = Checkbutton(frame, bg = COLOR, var = l3_val,\
        command = lambda: l3Click(l2_val, l3_val))
    l3_check.pack(side = LEFT)
    frame.grid()
    submit = Button(root, text = "Submit", command = lambda: process\
        (l2_val, l3_val, root))
    submit.grid(pady = (0, 40))

    root.mainloop()

def l2Click(l2_val, l3_val):
    if l2_val.get():
        l3_val.set(False)

def l3Click(l2_val, l3_val):
    if l3_val.get():
        l2_val.set(False)

def process(l2_val, l3_val, root):
    root.destroy()
    if l2_val.get():
        L2_Config_Template.L2()
    if l3_val.get():
        L3_Config_Template.L3()

main()
