import random
from tkinter import *
from PIL import Image, ImageDraw, ImageTk
from tkinter import ttk
import subprocess
import time
_BASE_W = 500
_BASE_H = 500


_CURR_W = _BASE_W
_CURR_H = _BASE_H

_T_W = _BASE_W
_T_H = _BASE_H


user=1
plyrs = 1
LARGE_FONT= ("Verdana", 12)
NORM_FONT = ("Helvetica", 10)
SMALL_FONT = ("Helvetica", 8)
bord = [0,0,0,0,0,0,0,0,0]
positions = [[80,100],[200,100],[320,100],[80,220],[200,220],[320,220],[80,340],[200,340],[320,340]]
btns = []
def center_window(w, h):
    # get screen width and height
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    # calculate position x, y
    x = (ws/2) - (w/2)    
    y = (hs/3) - (h/3)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

def ResizeComps():
    global _CURR_H,_CURR_W
    print(_CURR_W,_CURR_H)
    mainFrame.configure(width=_CURR_W,height=_CURR_H)
    selectusr.configure(width=_CURR_W,height=_CURR_H)
    canvas.configure(width=_CURR_W,height=_CURR_H)
    canvas2.configure(width=_CURR_W,height=_CURR_H)
    #mainFrame.place(x = (_CURR_W/2)-(_BASE_W/2),y= (_CURR_H/2)-(_BASE_H/2))
    selectusr_label.place(x = (_CURR_W/2)-(_BASE_W/2) + 90,y= (_CURR_H/2)-(_BASE_H/2) + 10)
    UvUbtn.place(x = (_CURR_W/2)-(_BASE_W/2) + 90,y= (_CURR_H/2)-(_BASE_H/2) + 150)
    UvCbtn.place(x = (_CURR_W/2)-(_BASE_W/2) + 90,y= (_CURR_H/2)-(_BASE_H/2) + 330)
    label_0.place(x = (_CURR_W/2)-(_BASE_W/2) + 90,y= (_CURR_H/2)-(_BASE_H/2) + 10)
    label_2.place(x = (_CURR_W/2)-(_BASE_W/2) + 200,y= (_CURR_H/2)-(_BASE_H/2) + 60)
    btn1.place(x = (_CURR_W/2)-(_BASE_W/2) + 80,y= (_CURR_H/2)-(_BASE_H/2) + 100)
    btn2.place(x = (_CURR_W/2)-(_BASE_W/2) + 200,y= (_CURR_H/2)-(_BASE_H/2) + 100)
    btn3.place(x = (_CURR_W/2)-(_BASE_W/2) + 320,y= (_CURR_H/2)-(_BASE_H/2) + 100)
    btn4.place(x = (_CURR_W/2)-(_BASE_W/2) + 80,y= (_CURR_H/2)-(_BASE_H/2) + 220)
    btn5.place(x = (_CURR_W/2)-(_BASE_W/2) + 200,y= (_CURR_H/2)-(_BASE_H/2) + 220)
    btn6.place(x = (_CURR_W/2)-(_BASE_W/2) + 320,y= (_CURR_H/2)-(_BASE_H/2) + 220)
    btn7.place(x = (_CURR_W/2)-(_BASE_W/2) + 80,y= (_CURR_H/2)-(_BASE_H/2) + 340)
    btn8.place(x = (_CURR_W/2)-(_BASE_W/2) + 200,y= (_CURR_H/2)-(_BASE_H/2) + 340)
    btn9.place(x = (_CURR_W/2)-(_BASE_W/2) + 320,y= (_CURR_H/2)-(_BASE_H/2) + 340)





def ResizeWind(arg):
    global _CURR_H,_CURR_W,_T_H,_T_W
    _CURR_W = root.winfo_width()
    _CURR_H = root.winfo_height()
    center_window(_CURR_W,_CURR_H)
    if (abs(_T_H - _CURR_H) > 10 or abs(_T_W - _CURR_W) >10 ):
        _T_H = _CURR_H
        _T_W = _CURR_W
        ResizeComps()
    


root = Tk()
#center_window(_BASE_W,_BASE_H)
root.title("Tic Tac Toe")
#root.resizable(False, False)
root.bind('<Configure>',ResizeWind)
def winning_condition(user):
    for i in range(0,len(bord)):
        if((bord[0]==user and bord[1]==user and bord[2]==user) or (bord[0]==user and bord[3]==user and bord[6]==user) or (bord[2]==user and bord[5]==user and bord[8]==user)
            or (bord[6]==user and bord[7]==user and bord[8]==user) or (bord[3]==user and bord[4]==user and bord[5]==user) or (bord[1]==user and bord[4]==user and bord[7]==user)
            or (bord[0]==user and bord[4]==user and bord[8]==user) or (bord[2]==user and bord[4]==user and bord[6]==user)):
            winner_msg(user)
            Button(root,text="Exit",bg="#ff2e2e", width=8,font=("bold",20),fg="white",command="exit").place(x=(_CURR_W/2)-(_BASE_W/2) + 270,y=(_CURR_H/2)-(_BASE_H/2) + 240)
            Button(root,text="ReMatch",bg="#ff2e2e", width=8,font=("bold",20),fg="white",command=rematch).place(x=(_CURR_W/2)-(_BASE_W/2) + 100,y=(_CURR_H/2)-(_BASE_H/2) + 240)
            return 1
    return 0
    
    
def winner_msg(i):
    label_3 = Label(root,bg="brown",fg="#5feb38",text="Match Finished", width=20,font=("bold",15))
    label_3.place(x=(_CURR_W/2)-(_BASE_W/2) + 150,y=(_CURR_H/2)-(_BASE_H/2) + 60)
    msg = "!! Congrats User "+str(i)+" won the match !!"
    Label(root,bg="#b6ff69",fg="red",text=msg, width=44,font=("bold",15)).place(x=(_CURR_W/2)-(_BASE_W/2) + 5,y=(_CURR_H/2)-(_BASE_H/2) + 460)
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

def clicked(pos):
    global user,zeros,crosses,bord,positions,plyrs
    if(user==1):
        label_3 = Label(root,bg="brown",fg="#5feb38",text="User 2's turn", width=10,font=("bold",15))
        label_3.place(x=(_CURR_W/2)-(_BASE_W/2) + 200,y=(_CURR_H/2)-(_BASE_H/2) + 60)
        #Button(root,width=110,height=110,bg='white',fg='white',image=o).place(x=(_CURR_W/2)-(_BASE_W/2) + a,y=(_CURR_H/2)-(_BASE_H/2) + b)
        btns[pos-1]["image"] = o
        btns[pos-1]["state"] = DISABLED
        bord[pos-1]=user
        if winning_condition(1):
            return
        user=2
        if(plyrs == 1):
            t = random.randint(1,9)
            while(bord[t-1]):
                t = random.randint(1,9)
            clicked(t)

    else:
        label_2 = Label(root,bg="brown",fg="yellow",text="User 1's turn", width=10,font=("bold",15))
        label_2.place(x=(_CURR_W/2)-(_BASE_W/2) + 200,y=(_CURR_H/2)-(_BASE_H/2) + 60)
        #Button(root,width=110,height=110,bg='white',fg='white',image=x).place(x=a,y=b)
        btns[pos-1]["image"] = x
        btns[pos-1]["state"] = DISABLED
        bord[pos-1]=user
        if winning_condition(2):
            return
        user=1

def SelectUser(u):
    global plyrs
    plyrs=u
    selectusr.grid_forget()
    mainFrame.place(x=0,y=0)


mainFrame = Frame(root)

canvas = Canvas(mainFrame,width=_BASE_W,height=_BASE_H)
image = ImageTk.PhotoImage(Image.open("imgs/wood.jpg"))

canvas.create_image(0,0,anchor=NW,image=image)
selectusr = Frame(root)
canvas2 = Canvas(selectusr,width=_BASE_W,height=_BASE_H)
canvas2.create_image(0,0,anchor=NW,image=image)

selectusrInnerFrame = Frame(selectusr)


selectusr_label = Label(selectusr,fg="red",text="Select The Mode", width=20,font=("bold",18))


UvUbtn = Button(selectusr,text="User Vs User",bg='blue',fg='yellow',width=20,font=("bold", 20),command=lambda: SelectUser(2))

UvCbtn = Button(selectusr,text="User Vs Computer",bg='blue',fg='yellow',width=20,font=("bold", 20),command=lambda: SelectUser(1))



o = ImageTk.PhotoImage(Image.open("imgs/circle.jpg"))
x = ImageTk.PhotoImage(Image.open("imgs/cross.jpg"))
white = ImageTk.PhotoImage(Image.open("imgs/white.jpg"))

label_0 = Label(mainFrame, text="Tic Tac Toe",width=20,font=("bold", 20))


label_2 = Label(mainFrame,bg="brown",fg="yellow",text="User 1's turn", width=10,font=("bold",15))

label_3 = Label(root,bg="brown",fg="#5feb38",text="Match Finished", width=20,font=("bold",15))

############
btn1 = Button(mainFrame,width=110,height=110,bg='white',fg='white',image=white,command=lambda : clicked(1))


btn2 = Button(mainFrame,width=110,height=110,bg='white',fg='white',image=white,command=lambda :clicked(2))


btn3 = Button(mainFrame,width=110,height=110,bg='white',fg='white', image=white,command=lambda :clicked(3))


###########
btn4 = Button(mainFrame,width=110,height=110,bg='white',fg='white', image=white,command=lambda :clicked(4))


btn5 = Button(mainFrame,width=110,height=110,bg='white',fg='white',image=white,command=lambda :clicked(5))


btn6 = Button(mainFrame,width=110,height=110,bg='white',fg='white', image=white,command=lambda :clicked(6))



############
btn7 = Button(mainFrame,width=110,height=110,bg='white',fg='white', image=white,command=lambda :clicked(7))


btn8 = Button(mainFrame,width=110,height=110,bg='white',fg='white',image=white,command=lambda :clicked(8))


btn9 = Button(mainFrame,width=110,height=110,bg='white',fg='white', image=white,command=lambda :clicked(9))

btns = [btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9]


canvas.grid(row=0,column=0)
canvas2.grid(row=0,column=0)
#selectusr_label.grid(row=0,column=0)
selectusr_label.place(x=90,y=10)
#UvUbtn.grid(row=1,column=0)
UvUbtn.place(x=90+_CURR_W-_BASE_W,y=150+_CURR_H-_BASE_H)
#UvCbtn.grid(row=2,column=0)
UvCbtn.place(x=90,y=330)
selectusr.grid(row=0,column=0)
label_0.place(x=90,y=10)
label_2.place(x=200,y=60)

btn1.place(x=80,y=100)
btn2.place(x=200,y=100)
btn3.place(x=320,y=100)
btn4.place(x=80,y=220)
btn5.place(x=200,y=220)
btn6.place(x=320,y=220)
btn7.place(x=80,y=340)
btn8.place(x=200,y=340)
btn9.place(x=320,y=340)

root.mainloop()
