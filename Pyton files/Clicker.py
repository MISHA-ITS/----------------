from tkinter import *

bomb = 100
score = 0
press_return = True

def start(event):
    global press_return
    global bomb
    global score
    if not press_return:
        pass
    else:
        bomb = 100
        score = 0
        label.config(text="")
        update_bomb()
        update_point()
        update_display()
        press_return = False

def update_display():
    global score
    global bomb
    if bomb>50:
        bomb_label.config(image = normal_photo)
    elif 0<bomb<50:
        bomb_label.config(image = no_photo)
    elif bomb<=0:
        bomb_label.config(image = bang_photo)
    fuse_label.config(text="Fuse : " + str(bomb))
    score_label.config(text="Score : " + str(score))
    fuse_label.after(100,update_display)

def update_point():
    global score
    score +=1
    if is_alive():
        score_label.after(3000, update_point)

def update_bomb():
    global bomb
    bomb-=5
    if is_alive():
        fuse_label.after(400, update_bomb)

def click():
    global bomb
    if is_alive():
        bomb+=1

def is_alive():
    global bomb
    global press_return
    if bomb<=0:
        label.config(text="Bang! Bang! Bang!")
        press_return = True
        return False
    else:
        return True

root = Tk()
root.title("Bang Bang!!!")
root.geometry("400x450+10+10")

label = Label(root, text="Press \"Enter\" to start the game", font=("Tahoma", 16))
label.pack()

fuse_label = Label(root, text='Fuse : ' + str(bomb), font=("Tahoma", 14))
fuse_label.pack() #side=LEFT, anchor='ne', padx=40, pady=20

score_label = Label(root, text='Score : ' + str(score), font=('Tahoma', 14))
score_label.pack() #side=RIGHT, anchor='nw', padx = 40, pady = 20

normal_photo = PhotoImage(file="img/bomb_normal.gif")
no_photo = PhotoImage(file="img/bomb_no.gif")
bang_photo = PhotoImage(file="img/pow.gif")

bomb_label = Label(root, image=normal_photo)
bomb_label.pack()

click_button = Button(root, text="Click me", bg="red", command=click, font=('Tahoma', 14), width=20, height=1)
click_button.pack()

root.bind('<Return>', start)

root.mainloop()