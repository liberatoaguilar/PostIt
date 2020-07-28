import tkinter
from tkinter import *
root = tkinter.Tk()
root.wm_title("Enter Text")
text = Label(root,text="Enter Text")
text.pack(side=LEFT)
e = Entry(root)
def on():
    global inpute
    inpute = e.get()
    if len(inpute) >= 30:
        cstart = 130
    else:
        cstart = 100
    split = inpute.split()
    if split[0].lower() == "color":

        color = split[1]
        if split[2] == "fill":
            cfill = split[3]
            inpute = split[4:]
        else:
            cfill = "black"
            inpute = split[2:]
    elif split[0].lower() == "fill":
        cfill = split[1]
        inpute = split[2:]
        color = "#ffff7a"
    else:
        color = "#ffff7a"
        cfill = "black"
    def post():
        root2 = tkinter.Tk()
        root2.wm_title("Postit")
        c = tkinter.Canvas(root2, bg=color,borderwidth=0,highlightthickness=0,)
        l = tkinter.Label(c,width=16,height=8,text=inpute,font=(" ",20, "bold"),fg=cfill,bg=color)
        c.pack(expand=YES,fill=BOTH)
        l.pack(expand=YES,fill=BOTH)
        root2.mainloop()
    post()
button = tkinter.Button(root,text="Enter",bg="#800000", command=on)
button.pack(side=BOTTOM)
e.pack(side=RIGHT)
root.mainloop()
