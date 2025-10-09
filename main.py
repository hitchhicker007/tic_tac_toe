# Import necessary libraries
import random
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import subprocess

# -------------------------------
# Constants - Avoid hard coding
# -------------------------------
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
BOARD_SIZE = 9
PLAYER_ONE = 1
PLAYER_TWO = 2
MODE_VS_COMPUTER = 1
MODE_VS_PLAYER = 2

# Font constants
LARGE_FONT = ("Verdana", 12)
NORM_FONT = ("Helvetica", 10)
SMALL_FONT = ("Helvetica", 8)
TITLE_FONT = ("bold", 20)
BUTTON_FONT = ("bold", 15)

# Color constants
COLOR_WINNER_BG = "#b6ff69"
COLOR_WINNER_FG = "red"
COLOR_LABEL_BG = "brown"
COLOR_LABEL_FG_GREEN = "#5feb38"
COLOR_LABEL_FG_YELLOW = "yellow"
COLOR_BUTTON_EXIT = "#ff2e2e"
COLOR_HIGHLIGHT = "red"

# Button positions on the board
POSITIONS = [
    [80, 100], [200, 100], [320, 100],
    [80, 220], [200, 220], [320, 220],
    [80, 340], [200, 340], [320, 340],
]

# Winning combinations
WINNING_COMBINATIONS = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
    [0, 4, 8], [2, 4, 6]              # Diagonals
]


# -------------------------------
# Global variables
# -------------------------------
current_user = PLAYER_ONE
game_mode = MODE_VS_COMPUTER
board = [0] * BOARD_SIZE


# -------------------------------
# Helper Functions
# -------------------------------
def center_window(window, width=WINDOW_WIDTH, height=WINDOW_HEIGHT):
    """Center the game window on screen"""
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_position = (screen_width / 2) - (width / 2)
    y_position = (screen_height / 3) - (height / 3)
    window.geometry("%dx%d+%d+%d" % (width, height, x_position, y_position))


def check_winning_condition(player):
    """Check if the given player has won using winning combinations"""
    for combo in WINNING_COMBINATIONS:
        if all(board[pos] == player for pos in combo):
            return True
    return False


def display_winner_message(player):
    """Display winner message and disable all buttons"""
    Label(root, bg=COLOR_LABEL_BG, fg=COLOR_LABEL_FG_GREEN, 
          text="Match Finished", width=20, font=BUTTON_FONT).place(x=150, y=60)
    
    message = f"!! Congrats User {player} won the match !!"
    Label(root, bg=COLOR_WINNER_BG, fg=COLOR_WINNER_FG, text=message,
          width=44, font=BUTTON_FONT).place(x=5, y=460)
    
    # Disable all buttons
    for button in game_buttons:
        button["state"] = DISABLED


def show_game_over_options():
    """Show Exit and Rematch buttons after game ends"""
    Button(root, text="Exit", bg=COLOR_BUTTON_EXIT, width=8, 
           font=TITLE_FONT, fg="white", command=exit).place(x=270, y=240)
    Button(root, text="ReMatch", bg=COLOR_BUTTON_EXIT, width=8, 
           font=TITLE_FONT, fg="white", command=rematch).place(x=100, y=240)


def rematch():
    """Restart the game"""
    root.destroy()
    subprocess.call(["python", "main.py"])


def get_random_empty_position():
    """Get a random empty position on the board for computer move"""
    empty_positions = [i for i in range(BOARD_SIZE) if board[i] == 0]
    if empty_positions:
        return random.choice(empty_positions) + 1
    return None


def update_turn_label(player):
    """Update the turn label to show current player"""
    if player == PLAYER_ONE:
        Label(mainFrame, bg=COLOR_LABEL_BG, fg=COLOR_LABEL_FG_YELLOW, 
              text="User 1's turn", width=10, font=BUTTON_FONT).place(x=200, y=60)
    else:
        Label(mainFrame, bg=COLOR_LABEL_BG, fg=COLOR_LABEL_FG_GREEN, 
              text="User 2's turn", width=10, font=BUTTON_FONT).place(x=200, y=60)


def handle_click(position, x_pos, y_pos):
    """Handle button click event"""
    global current_user, board
    
    # Guard clause - return if position already occupied
    if board[position - 1] != 0:
        return
    
    # Place marker and update board
    image_to_place = o if current_user == PLAYER_ONE else x
    Button(root, width=110, height=110, bg="white", fg="white", 
           image=image_to_place).place(x=x_pos, y=y_pos)
    board[position - 1] = current_user
    
    # Check for win
    if check_winning_condition(current_user):
        display_winner_message(current_user)
        show_game_over_options()
        return
    
    # Switch player
    current_user = PLAYER_TWO if current_user == PLAYER_ONE else PLAYER_ONE
    update_turn_label(current_user)
    
    # Computer move if in computer mode
    if game_mode == MODE_VS_COMPUTER and current_user == PLAYER_TWO:
        computer_position = get_random_empty_position()
        if computer_position:
            handle_click(computer_position, POSITIONS[computer_position - 1][0], 
                        POSITIONS[computer_position - 1][1])


def select_game_mode(mode):
    """Select game mode and show main game board"""
    global game_mode
    game_mode = mode
    selectusr.pack_forget()
    mainFrame.pack()


# -------------------------------
# UI Setup
# -------------------------------
root = Tk()
center_window(root, WINDOW_WIDTH, WINDOW_HEIGHT)
root.title("Tic Tac Toe")
root.resizable(False, False)

# Main game frame
mainFrame = Frame(root)
canvas = Canvas(mainFrame, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
background_image = ImageTk.PhotoImage(Image.open("imgs/wood.jpg"))
canvas.pack()
canvas.create_image(0, 0, anchor=NW, image=background_image)

# Mode selection frame
selectusr = Frame(root)
canvas2 = Canvas(selectusr, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
canvas2.create_image(0, 0, anchor=NW, image=background_image)
canvas2.pack()

Label(selectusr, fg=COLOR_WINNER_FG, text="Select The Mode",
      width=20, font=("bold", 18)).place(x=90, y=10)

Button(selectusr, text="User Vs User", bg="blue", fg=COLOR_LABEL_FG_YELLOW,
       width=20, font=TITLE_FONT, command=lambda: select_game_mode(MODE_VS_PLAYER)).place(x=50, y=150)

Button(selectusr, text="User Vs Computer", bg="blue", fg=COLOR_LABEL_FG_YELLOW,
       width=20, font=TITLE_FONT, command=lambda: select_game_mode(MODE_VS_COMPUTER)).place(x=50, y=330)

selectusr.pack()

# Load marker images
o = ImageTk.PhotoImage(Image.open("imgs/circle.jpg"))
x = ImageTk.PhotoImage(Image.open("imgs/cross.jpg"))
white = ImageTk.PhotoImage(Image.open("imgs/white.jpg"))

# Title and turn label
Label(mainFrame, text="Tic Tac Toe", width=20, font=TITLE_FONT).place(x=90, y=10)
update_turn_label(PLAYER_ONE)

# Create 9 game buttons
game_buttons = []
for i in range(BOARD_SIZE):
    btn = Button(mainFrame, width=110, height=110, bg="white", fg="white",
                 image=white, command=lambda pos=i+1, x=POSITIONS[i][0], 
                 y=POSITIONS[i][1]: handle_click(pos, x, y))
    btn.place(x=POSITIONS[i][0], y=POSITIONS[i][1])
    game_buttons.append(btn)

root.mainloop()
