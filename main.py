# Import necessary libraries
import random                      # For computer's random move
from tkinter import *               # For GUI elements
from PIL import Image, ImageDraw, ImageTk  # For handling images in Tkinter
from tkinter import ttk
import subprocess                   # For restarting the game
import time

# -------------------------------
# Function to center the game window on screen
# -------------------------------
def center_window(w=300, h=200):
    ws = root.winfo_screenwidth()   # Get screen width
    hs = root.winfo_screenheight()  # Get screen height
    x = (ws / 2) - (w / 2)          # Calculate X position
    y = (hs / 3) - (h / 3)          # Calculate Y position
    root.geometry("%dx%d+%d+%d" % (w, h, x, y))  # Apply geometry to window


# -------------------------------
# Global variables and setup
# -------------------------------
user = 1        # Keeps track of which player's turn it is (1 or 2)
plyrs = 1       # 1 = User vs Computer, 2 = User vs User
LARGE_FONT = ("Verdana", 12)
NORM_FONT = ("Helvetica", 10)
SMALL_FONT = ("Helvetica", 8)

bord = [0, 0, 0, 0, 0, 0, 0, 0, 0]  # Represents the game board (3x3 grid)

# Positions of buttons on the board (used for placing Xs and Os)
positions = [
    [80, 100], [200, 100], [320, 100],
    [80, 220], [200, 220], [320, 220],
    [80, 340], [200, 340], [320, 340],
]

# Create root window
root = Tk()
center_window(500, 500)
root.title("Tic Tac Toe")
root.resizable(False, False)

# -------------------------------
# Function to check winning condition
# -------------------------------
def winning_condition(user):
    for i in range(0, len(bord)):
        if (
            (bord[0] == user and bord[1] == user and bord[2] == user) or
            (bord[0] == user and bord[3] == user and bord[6] == user) or
            (bord[2] == user and bord[5] == user and bord[8] == user) or
            (bord[6] == user and bord[7] == user and bord[8] == user) or
            (bord[3] == user and bord[4] == user and bord[5] == user) or
            (bord[1] == user and bord[4] == user and bord[7] == user) or
            (bord[0] == user and bord[4] == user and bord[8] == user) or
            (bord[2] == user and bord[4] == user and bord[6] == user)
        ):
            winner_msg(user)  # Announce winner
            # Show Exit and Rematch buttons after win
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


# -------------------------------
# Function to display the winner message
# -------------------------------
def winner_msg(i):
    Label(root, bg="brown", fg="#5feb38", text="Match Finished",
          width=20, font=("bold", 15)).place(x=150, y=60)
    msg = "!! Congrats User " + str(i) + " won the match !!"
    Label(root, bg="#b6ff69", fg="red", text=msg,
          width=44, font=("bold", 15)).place(x=5, y=460)
    
    # Disable all buttons after win
    for btn in [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]:
        btn["state"] = DISABLED


# -------------------------------
# Function to restart the game
# -------------------------------
def rematch():
    root.destroy()                         # Close current window
    subprocess.call(["python", "main.py"]) # Relaunch the game


# -------------------------------
# Function that triggers when a cell (button) is clicked
# -------------------------------
def clicked(pos, a, b):
    global user, bord, positions, plyrs
    if user == 1:
        # User 1's move (O)
        Label(root, bg="brown", fg="#5feb38", text="User 2's turn",
              width=10, font=("bold", 15)).place(x=200, y=60)
        Button(root, width=110, height=110, bg="white", fg="white", image=o).place(x=a, y=b)
        bord[pos - 1] = user
        
        # Check if User 1 wins
        if winning_condition(1):
            return
        user = 2
        
        # If playing against computer, let it make a random move
        if plyrs == 1:
            t = random.randint(1, 9)
            while bord[t - 1]:  # Find an empty cell
                t = random.randint(1, 9)
            clicked(t, positions[t - 1][0], positions[t - 1][1])

    else:
        # User 2's move (X)
        Label(root, bg="brown", fg="yellow", text="User 1's turn",
              width=10, font=("bold", 15)).place(x=200, y=60)
        Button(root, width=110, height=110, bg="white", fg="white", image=x).place(x=a, y=b)
        bord[pos - 1] = user
        
        # Check if User 2 wins
        if winning_condition(2):
            return
        user = 1


# -------------------------------
# Function to select game mode (User vs User or User vs Computer)
# -------------------------------
def SelectUser(u):
    global plyrs
    plyrs = u               # Set mode based on selection
    selectusr.pack_forget() # Hide selection screen
    mainFrame.pack()        # Show main game board


# -------------------------------
# UI SETUP
# -------------------------------

mainFrame = Frame(root)

# Background image for board
canvas = Canvas(mainFrame, width=500, height=500)
image = ImageTk.PhotoImage(Image.open("imgs/wood.jpg"))
canvas.pack()
canvas.create_image(0, 0, anchor=NW, image=image)

# Frame for selecting game mode
selectusr = Frame(root)
canvas2 = Canvas(selectusr, width=500, height=500)
canvas2.create_image(0, 0, anchor=NW, image=image)
canvas2.pack()

# Labels and buttons for mode selection
Label(selectusr, fg="red", text="Select The Mode",
      width=20, font=("bold", 18)).place(x=90, y=10)

UvUbtn = Button(selectusr, text="User Vs User", bg="blue", fg="yellow",
                width=20, font=("bold", 20), command=lambda: SelectUser(2))
UvUbtn.place(x=50, y=150)

UvCbtn = Button(selectusr, text="User Vs Computer", bg="blue", fg="yellow",
                width=20, font=("bold", 20), command=lambda: SelectUser(1))
UvCbtn.place(x=50, y=330)

selectusr.pack()

# Load X, O, and white placeholder images
o = ImageTk.PhotoImage(Image.open("imgs/circle.jpg"))
x = ImageTk.PhotoImage(Image.open("imgs/cross.jpg"))
white = ImageTk.PhotoImage(Image.open("imgs/white.jpg"))

# Title and turn label
Label(mainFrame, text="Tic Tac Toe", width=20, font=("bold", 20)).place(x=90, y=10)
label_2 = Label(mainFrame, bg="brown", fg="yellow", text="User 1's turn",
                width=10, font=("bold", 15))
label_2.place(x=200, y=60)

# -------------------------------
# Create 9 buttons (game cells)
# -------------------------------
btn1 = Button(mainFrame, width=110, height=110, bg="white", fg="white",
              image=white, command=lambda: clicked(1, 80, 100))
btn1.place(x=80, y=100)

btn2 = Button(mainFrame, width=110, height=110, bg="white", fg="white",
              image=white, command=lambda: clicked(2, 200, 100))
btn2.place(x=200, y=100)

btn3 = Button(mainFrame, width=110, height=110, bg="white", fg="white",
              image=white, command=lambda: clicked(3, 320, 100))
btn3.place(x=320, y=100)

btn4 = Button(mainFrame, width=110, height=110, bg="white", fg="white",
              image=white, command=lambda: clicked(4, 80, 220))
btn4.place(x=80, y=220)

btn5 = Button(mainFrame, width=110, height=110, bg="white", fg="white",
              image=white, command=lambda: clicked(5, 200, 220))
btn5.place(x=200, y=220)

btn6 = Button(mainFrame, width=110, height=110, bg="white", fg="white",
              image=white, command=lambda: clicked(6, 320, 220))
btn6.place(x=320, y=220)

btn7 = Button(mainFrame, width=110, height=110, bg="white", fg="white",
              image=white, command=lambda: clicked(7, 80, 340))
btn7.place(x=80, y=340)

btn8 = Button(mainFrame, width=110, height=110, bg="white", fg="white",
              image=white, command=lambda: clicked(8, 200, 340))
btn8.place(x=200, y=340)

btn9 = Button(mainFrame, width=110, height=110, bg="white", fg="white",
              image=white, command=lambda: clicked(9, 320, 340))
btn9.place(x=320, y=340)

# -------------------------------
# Start the Tkinter main loop
# -------------------------------
root.mainloop()
