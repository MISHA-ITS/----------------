from tkinter import *
                                                            
    
def makeButton(color, function):
    button = Button(bg=color, command=function, width=17, height=1)
    button.pack()

def red():
    label.config(text="Red")
    entry.delete(0, END)
    entry.insert(0, "#ff0000")
    root["bg"] = "Red"
def orange():
    label.config(text="Orange")
    entry.delete(0, END)
    entry.insert(0, "#ff7d00")
    root["bg"] = "Orange"
def yellow():
    label.config(text="Yellow")
    entry.delete(0, END)
    entry.insert(0, "#ffff00")
    root["bg"] = "Yellow"
def green():
    label.config(text="Green")
    entry.delete(0, END)
    entry.insert(0, "#00ff00")
    root["bg"] = "Green"
def cyan():
    label.config(text="Cyan")
    entry.delete(0, END)
    entry.insert(0, "#00ffff")
    root["bg"] = "Cyan"
def blue():
    label.config(text="Blue")
    entry.delete(0, END)
    entry.insert(0, "#0000ff")
    root["bg"] = "Blue"
def purple():
    label.config(text="Purple")
    entry.delete(0, END)
    entry.insert(0, "#7d00ff")
    root["bg"] = "Purple"
def black():
    label.config(text="Black")
    entry.delete(0, END)
    entry.insert(0, "#000000")
    root["bg"] = "black"
def white():
    label.config(text="White")
    entry.delete(0, END)
    entry.insert(0, "#ffffff")
    root["bg"] = "White"
def pink():
    label.config(text="Pink")
    entry.delete(0, END)
    entry.insert(0, "#ff00ff")
    root["bg"] = "Pink"
def brown():
    label.config(text="Brown")
    entry.delete(0, END)
    entry.insert(0, "#7d3c00")
    root["bg"] = "Brown"
def grey():
    label.config(text="Grey")
    entry.delete(0, END)
    entry.insert(0, "#808080")
    root["bg"] = "Grey"
def gold():
    label.config(text="Gold")
    entry.delete(0, END)
    entry.insert(0, "#ffd700")
    root["bg"] = "Gold"

root = Tk()
root.title("Color picker")
root.geometry("250x400+400+300")
root.maxsize(400, 600)
root.minsize(100, 150)
root["background"] = "#c9c0bb"
root.resizable(False, True)

label = Label(root, anchor='center')
label.pack()

entry = Entry(root, justify='center', bd=3)
entry.pack()

makeButton("#ff0000", lambda: red())
makeButton("#ff7d00", lambda: orange())
makeButton("#ffff00", lambda: yellow())
makeButton("#00ff00", lambda: green())
makeButton("#007dff", lambda: blue())
makeButton("#7d00ff", lambda: purple())
makeButton("#000000", lambda: black())
makeButton("#ffffff", lambda: white())
makeButton("#ff00ff", lambda: pink())
makeButton("#7d3c00", lambda: brown())
makeButton("#808080", lambda: grey())
makeButton("#ffd700", lambda: gold())


root.mainloop()