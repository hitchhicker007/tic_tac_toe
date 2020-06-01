from tkinter import *
from PIL import Image, ImageDraw, ImageTk
from tkinter import ttk
import subprocess

def center_window(w=300, h=200):
    # get screen width and height
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    # calculate position x, y
    x = (ws/2) - (w/2)    
    y = (hs/3) - (h/3)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

user=1
LARGE_FONT= ("Verdana", 12)
NORM_FONT = ("Helvetica", 10)
SMALL_FONT = ("Helvetica", 8)
bord = [0,0,0,0,0,0,0,0,0]

root = Tk()
center_window(500,500)
root.title("Tic Tac Toe")

def winning_condition(user):
    for i in range(0,len(bord)):
        if((bord[0]==user and bord[1]==user and bord[2]==user) or (bord[0]==user and bord[3]==user and bord[6]==user) or (bord[2]==user and bord[5]==user and bord[8]==user)
            or (bord[6]==user and bord[7]==user and bord[8]==user) or (bord[3]==user and bord[4]==user and bord[5]==user) or (bord[1]==user and bord[4]==user and bord[7]==user)
            or (bord[0]==user and bord[4]==user and bord[8]==user) or (bord[2]==user and bord[4]==user and bord[6]==user)):
            winner_msg(user)
            Button(root,text="Exit",bg="#ff2e2e", width=8,font=("bold",20),fg="white",command="exit").place(x=270,y=240)
            Button(root,text="ReMatch",bg="#ff2e2e", width=8,font=("bold",20),fg="white",command=rematch).place(x=100,y=240)
    
    
def winner_msg(i):
    label_3 = Label(root,bg="brown",fg="#5feb38",text="Match Finished", width=20,font=("bold",15))
    label_3.place(x=150,y=60)
    msg = "!! Congrats User "+str(i)+" won the match !!"
    Label(root,bg="#b6ff69",fg="red",text=msg, width=44,font=("bold",15)).place(x=5,y=460)
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
    subprocess.call(["python","main.py"])

def clicked(pos,a,b):
    global user,zeros,crosses,bord
    if(user==1):
        label_3 = Label(root,bg="brown",fg="#5feb38",text="User 2's turn", width=10,font=("bold",15))
        label_3.place(x=200,y=60)
        Button(root,width=110,height=110,bg='white',fg='white',image=o).place(x=a,y=b)
        bord[pos-1]=user
        winning_condition(1)
        user=2
    else:
        label_2 = Label(root,bg="brown",fg="yellow",text="User 1's turn", width=10,font=("bold",15))
        label_2.place(x=200,y=60)
        Button(root,width=110,height=110,bg='white',fg='white',image=x).place(x=a,y=b)
        bord[pos-1]=user
        winning_condition(2)
        user=1



canvas = Canvas(root,width=500,height=500)
image = ImageTk.PhotoImage(Image.open("imgs/wood.jpg"))

canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()

o = ImageTk.PhotoImage(Image.open("imgs/circle.jpg"))
x = ImageTk.PhotoImage(Image.open("imgs/cross.jpg"))
white = ImageTk.PhotoImage(Image.open("imgs/white.jpg"))

label_0 = Label(root, text="Tic Tac Toe",width=20,font=("bold", 20))
label_0.place(x=90,y=10)

label_2 = Label(root,bg="brown",fg="yellow",text="User 1's turn", width=10,font=("bold",15))
label_2.place(x=200,y=60)

############
btn1 = Button(root,width=110,height=110,bg='white',fg='white',image=white,command=lambda : clicked(1,80,100))
btn1.place(x=80,y=100)

btn2 = Button(root,width=110,height=110,bg='white',fg='white',image=white,command=lambda :clicked(2,200,100))
btn2.place(x=200,y=100)

btn3 = Button(root,width=110,height=110,bg='white',fg='white', image=white,command=lambda :clicked(3,320,100))
btn3.place(x=320,y=100)

###########
btn4 = Button(root,width=110,height=110,bg='white',fg='white', image=white,command=lambda :clicked(4,80,220))
btn4.place(x=80,y=220)

btn5 = Button(root,width=110,height=110,bg='white',fg='white',image=white,command=lambda :clicked(5,200,220))
btn5.place(x=200,y=220)

btn6 = Button(root,width=110,height=110,bg='white',fg='white', image=white,command=lambda :clicked(6,320,220))
btn6.place(x=320,y=220)


############
btn7 = Button(root,width=110,height=110,bg='white',fg='white', image=white,command=lambda :clicked(7,80,340))
btn7.place(x=80,y=340)

btn8 = Button(root,width=110,height=110,bg='white',fg='white',image=white,command=lambda :clicked(8,200,340))
btn8.place(x=200,y=340)

btn9 = Button(root,width=110,height=110,bg='white',fg='white', image=white,command=lambda :clicked(9,320,340))
btn9.place(x=320,y=340)

root.mainloop()