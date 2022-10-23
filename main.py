import random
from tkinter import *
from PIL import Image, ImageDraw, ImageTk
from tkinter import ttk
import subprocess
import time


def center_window(w=300, h=200):
    # get screen width and height
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    # calculate position x, y
    x = (ws / 2) - (w / 2)
    y = (hs / 3) - (h / 3)
    root.geometry("%dx%d+%d+%d" % (w, h, x, y))


user = 1
plyrs = 1
LARGE_FONT = ("Verdana", 12)
NORM_FONT = ("Helvetica", 10)
SMALL_FONT = ("Helvetica", 8)
bord = [0, 0, 0, 0, 0, 0, 0, 0, 0]
positions = [
    [80, 100],
    [200, 100],
    [320, 100],
    [80, 220],
    [200, 220],
    [320, 220],
    [80, 340],
    [200, 340],
    [320, 340],
]
root = Tk()
center_window(500, 500)
root.title("Tic Tac Toe")
root.resizable(False, False)


def winning_condition(user):
    for i in range(0, len(bord)):
        if (
            (bord[0] == user and bord[1] == user and bord[2] == user)
            or (bord[0] == user and bord[3] == user and bord[6] == user)
            or (bord[2] == user and bord[5] == user and bord[8] == user)
            or (bord[6] == user and bord[7] == user and bord[8] == user)
            or (bord[3] == user and bord[4] == user and bord[5] == user)
            or (bord[1] == user and bord[4] == user and bord[7] == user)
            or (bord[0] == user and bord[4] == user and bord[8] == user)
            or (bord[2] == user and bord[4] == user and bord[6] == user)
        ):
            winner_msg(user)
            Button(
                root,
                text="Exit",
                bg="#ff2e2e",
                width=8,
                font=("bold", 20),
                fg="white",
                command="exit",
            ).place(x=270, y=240)
            Button(
                root,
                text="ReMatch",
                bg="#ff2e2e",
                width=8,
                font=("bold", 20),
                fg="white",
                command=rematch,
            ).place(x=100, y=240)
            return 1
    return 0


def winner_msg(i):
    label_3 = Label(
        root,
        bg="brown",
        fg="#5feb38",
        text="Match Finished",
        width=20,
        font=("bold", 15),
    )
    label_3.place(x=150, y=60)
    msg = "!! Congrats User " + str(i) + " won the match !!"
    Label(root, bg="#b6ff69", fg="red", text=msg, width=44, font=("bold", 15)).place(
        x=5, y=460
    )
    btn1["state"] = DISABLED
    btn2["state"] = DISABLED
    btn3["state"] = DISABLED
    btn4["state"] = DISABLED
    btn5["state"] = DISABLED
    btn6["state"] = DISABLED
    btn7["state"] = DISABLED
    btn8["state"] = DISABLED
    btn9["state"] = DISABLED


def rematch():
    root.destroy()
    subprocess.call(["python", "main.py"])


def clicked(pos, a, b):
    global user, zeros, crosses, bord, positions, plyrs
    if user == 1:
        label_3 = Label(
            root,
            bg="brown",
            fg="#5feb38",
            text="User 2's turn",
            width=10,
            font=("bold", 15),
        )
        label_3.place(x=200, y=60)
        Button(root, width=110, height=110, bg="white", fg="white", image=o).place(
            x=a, y=b
        )
        bord[pos - 1] = user
        if winning_condition(1):
            return
        user = 2
        if plyrs == 1:
            t = random.randint(1, 9)
            while bord[t - 1]:
                t = random.randint(1, 9)
            clicked(t, positions[t - 1][0], positions[t - 1][1])

    else:
        label_2 = Label(
            root,
            bg="brown",
            fg="yellow",
            text="User 1's turn",
            width=10,
            font=("bold", 15),
        )
        label_2.place(x=200, y=60)
        Button(root, width=110, height=110, bg="white", fg="white", image=x).place(
            x=a, y=b
        )
        bord[pos - 1] = user
        if winning_condition(2):
            return
        user = 1


def SelectUser(u):
    global plyrs
    plyrs = u
    selectusr.pack_forget()
    mainFrame.pack()


mainFrame = Frame(root)

canvas = Canvas(mainFrame, width=500, height=500)
image = ImageTk.PhotoImage(Image.open("imgs/wood.jpg"))
canvas.pack()
canvas.create_image(0, 0, anchor=NW, image=image)
selectusr = Frame(root)
canvas2 = Canvas(selectusr, width=500, height=500)
canvas2.create_image(0, 0, anchor=NW, image=image)
canvas2.pack()

selectusr_label = Label(
    selectusr, fg="red", text="Select The Mode", width=20, font=("bold", 18)
)
selectusr_label.place(x=90, y=10)

UvUbtn = Button(
    selectusr,
    text="User Vs User",
    bg="blue",
    fg="yellow",
    width=20,
    font=("bold", 20),
    command=lambda: SelectUser(2),
)
UvUbtn.place(x=50, y=150)
UvCbtn = Button(
    selectusr,
    text="User Vs Computer",
    bg="blue",
    fg="yellow",
    width=20,
    font=("bold", 20),
    command=lambda: SelectUser(1),
)
UvCbtn.place(x=50, y=330)

selectusr.pack()

o = ImageTk.PhotoImage(Image.open("imgs/circle.jpg"))
x = ImageTk.PhotoImage(Image.open("imgs/cross.jpg"))
white = ImageTk.PhotoImage(Image.open("imgs/white.jpg"))

label_0 = Label(mainFrame, text="Tic Tac Toe", width=20, font=("bold", 20))
label_0.place(x=90, y=10)

label_2 = Label(
    mainFrame,
    bg="brown",
    fg="yellow",
    text="User 1's turn",
    width=10,
    font=("bold", 15),
)
label_2.place(x=200, y=60)

############
btn1 = Button(
    mainFrame,
    width=110,
    height=110,
    bg="white",
    fg="white",
    image=white,
    command=lambda: clicked(1, 80, 100),
)
btn1.place(x=80, y=100)

btn2 = Button(
    mainFrame,
    width=110,
    height=110,
    bg="white",
    fg="white",
    image=white,
    command=lambda: clicked(2, 200, 100),
)
btn2.place(x=200, y=100)

btn3 = Button(
    mainFrame,
    width=110,
    height=110,
    bg="white",
    fg="white",
    image=white,
    command=lambda: clicked(3, 320, 100),
)
btn3.place(x=320, y=100)

###########
btn4 = Button(
    mainFrame,
    width=110,
    height=110,
    bg="white",
    fg="white",
    image=white,
    command=lambda: clicked(4, 80, 220),
)
btn4.place(x=80, y=220)

btn5 = Button(
    mainFrame,
    width=110,
    height=110,
    bg="white",
    fg="white",
    image=white,
    command=lambda: clicked(5, 200, 220),
)
btn5.place(x=200, y=220)

btn6 = Button(
    mainFrame,
    width=110,
    height=110,
    bg="white",
    fg="white",
    image=white,
    command=lambda: clicked(6, 320, 220),
)
btn6.place(x=320, y=220)


############
btn7 = Button(
    mainFrame,
    width=110,
    height=110,
    bg="white",
    fg="white",
    image=white,
    command=lambda: clicked(7, 80, 340),
)
btn7.place(x=80, y=340)

btn8 = Button(
    mainFrame,
    width=110,
    height=110,
    bg="white",
    fg="white",
    image=white,
    command=lambda: clicked(8, 200, 340),
)
btn8.place(x=200, y=340)

btn9 = Button(
    mainFrame,
    width=110,
    height=110,
    bg="white",
    fg="white",
    image=white,
    command=lambda: clicked(9, 320, 340),
)
btn9.place(x=320, y=340)

root.mainloop()
