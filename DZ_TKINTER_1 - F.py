from tkinter import *

def makeButton(color, function):
  button = Button(root, bg=color, command=function)
  button.pack(expand=True, fill=BOTH)

root = Tk()
root.title("Color picker")
root.geometry("250x600+400+300")
root.maxsize(400, 700)
root.minsize(100, 150)
root["background"] = "#c9c0bb"
root.resizable(False, True)

label = Label(root, anchor='center', font=("Arial", 14, "bold",), fg="#FFFFFF")
label.pack()

entry = Entry(root, justify='center', bd=2, font=("Arial", 10))
entry.pack()

makeButton("red", lambda: (label.config(text=" red ", background="red"), entry.delete(0, END), entry.insert(0, "#FF0000")))
makeButton("orange", lambda: (label.config(text=" orange ", background="orange"), entry.delete(0, END), entry.insert(0, "#FFA500")))
makeButton("yellow", lambda: (label.config(text=" yellow ", background="yellow"), entry.delete(0, END), entry.insert(0, "#FFFF00")))
makeButton("green", lambda: (label.config(text=" green ", background="green"), entry.delete(0, END), entry.insert(0, "#008000")))
makeButton("blue", lambda: (label.config(text="blue  ", background="blue"), entry.delete(0, END), entry.insert(0, "#0000FF")))
makeButton("purple", lambda: (label.config(text=" purple ", background="purple"), entry.delete(0, END), entry.insert(0, "#800080")))
makeButton("black", lambda: (label.config(text=" black ", background="black"), entry.delete(0, END), entry.insert(0, "#000000")))
makeButton("gray", lambda: (label.config(text=" gray ", background="gray"), entry.delete(0, END), entry.insert(0, "#808080")))
makeButton("brown", lambda: (label.config(text=" brown ", background="brown"), entry.delete(0, END), entry.insert(0, "#A52A2A")))
makeButton("pink", lambda: (label.config(text=" pink ", background="pink"), entry.delete(0, END), entry.insert(0, "#FFC0CB")))
makeButton("cyan", lambda: (label.config(text=" cyan ", background="cyan"), entry.delete(0, END), entry.insert(0, "#00FFFF")))
makeButton("gold", lambda: (label.config(text=" gold ", background="gold"), entry.delete(0, END), entry.insert(0, "#FFD700")))
makeButton("silver", lambda: (label.config(text=" silver ", background="silver"), entry.delete(0, END), entry.insert(0, "#C0C0C0")))
makeButton("lime", lambda: (label.config(text=" lime ", background="lime"), entry.delete(0, END), entry.insert(0, "#00FF00")))
makeButton("maroon", lambda: (label.config(text=" maroon ", background="maroon"), entry.delete(0, END), entry.insert(0, "#800000")))
makeButton("olive", lambda: (label.config(text=" olive ", background="olive"), entry.delete(0, END), entry.insert(0, "#808000")))
makeButton("navy", lambda: (label.config(text=" navy ", background="navy"), entry.delete(0, END), entry.insert(0, "#000080")))
makeButton("teal", lambda: (label.config(text=" teal ", background="teal"), entry.delete(0, END), entry.insert(0, "#008080")))
makeButton("aqua", lambda: (label.config(text=" aqua ", background="aqua"), entry.delete(0, END), entry.insert(0, "#00FFFF")))
makeButton("fuchsia", lambda: (label.config(text=" fuchsia ", background="fuchsia"), entry.delete(0, END), entry.insert(0, "#FF00FF")))


root.mainloop()