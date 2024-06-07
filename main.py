import tkinter as tk
from PIL import ImageTk, Image
import random


def start_game():
    global im, b4, b3, restart_btn
    global b1, b2

    # Buttons for Players
    # Player -1
    b1.place(x=1200, y=400)

    # Player -2
    b2.place(x=1200, y=550)

    # Exit button
    b3 = tk.Button(root, text="Click Here to End Game", height=3, width=20, fg="red", bg="yellow",
                   font=('Cursive', 14, 'bold'), activebackground="white", command=root.destroy)
    b3.place(x=1200, y=20)

    # Dice button with image
    im = Image.open("dice.png")
    im = im.resize((65, 65))
    im = ImageTk.PhotoImage(im)
    b4 = tk.Button(root, image=im, height=80, width=80, command=roll_dice)
    b4.place(x=1250, y=200)

    # Restart button
    restart_btn = tk.Button(root, text="Restart Game", height=3, width=20, fg="blue", bg="lightgreen",
                            font=('Cursive', 14, 'bold'), activebackground="white", command=restart_game)
    restart_btn.place(x=1200, y=300)


def reset_coins():
    global player_1, player_2
    global pos1, pos2

    player_1.place(x=0, y=750)
    player_2.place(x=50, y=750)

    pos1 = 0
    pos2 = 0


def restart_game():
    global turn

    # Reset player positions
    reset_coins()

    # Reset turn to player 1
    turn = 1

    # Enable player 1 button and disable player 2 button
    b1.configure(state='normal')
    b2.configure(state='disabled')

    # Reset dice button image
    b4.config(image=im)


def load_dice_images():
    global Dice
    names = ["dice 1.png", "dice 2.png", "dice 3.png", "dice 4.png", "dice 5.png", "dice 6.png"]
    for nam in names:
        im = Image.open(nam)
        im = im.resize((65, 65))
        im = ImageTk.PhotoImage(im)
        Dice.append(im)


def check_ladder(Turn):
    global pos1, pos2
    global Ladder

    if Turn == 1:
        if pos1 in Ladder:
            pos1 = Ladder[pos1]
            return 1
    else:
        if pos2 in Ladder:
            pos2 = Ladder[pos2]
            return 1
    return 0


def check_snake(Turn):
    global pos1, pos2

    if Turn == 1:
        if pos1 in Snake:
            pos1 = Snake[pos1]  # changing position to tail
    else:
        if pos2 in Snake:
            pos2 = Snake[pos2]


def roll_dice():
    global Dice
    global turn
    global pos1, pos2
    global b1, b2, b4

    r = random.randint(1, 6)
    b4.config(image=Dice[r - 1])

    Lad = 0  # no ladder
    if turn == 1:
        if (pos1 + r) <= 100:
            pos1 += r
        Lad = check_ladder(turn)
        check_snake(turn)
        move_coin(turn, pos1)
        if r != 6 and Lad != 1:
            turn = 2
            b1.configure(state='disabled')
            b2.configure(state='normal')
    else:
        if (pos2 + r) <= 100:
            pos2 += r
        Lad = check_ladder(turn)
        check_snake(turn)
        move_coin(turn, pos2)
        if r != 6 and Lad != 1:
            turn = 1
            b1.configure(state='normal')
            b2.configure(state='disabled')
    is_winner()


def is_winner():
    global pos1, pos2

    if pos1 == 100:
        msg = "Player 1 is the Winner"
        Lab = tk.Label(root, text=msg, height=2, width=20, bg='red', font=('Cursive', 30, 'bold'))
        Lab.place(x=300, y=300)
        reset_coins()
    elif pos2 == 100:
        msg = "Player 2 is the Winner"
        Lab = tk.Label(root, text=msg, height=2, width=20, bg='red', font=('Cursive', 30, 'bold'))
        Lab.place(x=300, y=300)
        reset_coins()


def move_coin(Turn, pos):
    global player_1, player_2
    global Index

    if Turn == 1:
        player_1.place(x=Index[pos][0], y=Index[pos][1])
    else:
        player_2.place(x=Index[pos][0], y=Index[pos][1])


def get_index():
    global Index
    Num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
           20, 19, 18, 17, 16, 15, 14, 13, 12, 11,
           21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
           40, 39, 38, 37, 36, 35, 34, 33, 32, 31,
           41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
           60, 59, 58, 57, 56, 55, 54, 53, 52, 51,
           61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
           80, 79, 78, 77, 76, 75, 74, 73, 72, 71,
           81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
           100, 99, 98, 97, 96, 95, 94, 93, 92, 91]
    row = 700
    i = 0
    for x in range(10):
        col = 0
        for y in range(10):
            Index[Num[i]] = (col, row)
            col += 113
            i += 1
        row -= 75


# Initialize global variables
Dice = []
Index = {}
pos1 = None
pos2 = None

# Ladder positions
Ladder = {1: 38, 4: 14, 9: 31, 28: 42, 21: 84, 51: 67, 72: 91, 80: 99}

# Snake positions
Snake = {98: 79, 95: 75, 93: 73, 87: 36, 62: 18, 64: 60, 54: 34, 17: 7}

# Setup the main window
root = tk.Tk()
root.geometry("1400x800")
root.title("Snake & Ladder Game")

# Setup the game board frame
F1 = tk.Frame(root, width=1100, height=800, relief='raised')
F1.place(x=0, y=0)

# Set the game board image
img1 = ImageTk.PhotoImage(Image.open("board (5).jpg"))
Lab = tk.Label(F1, image=img1)
Lab.place(x=0, y=0)

# Player 1 button
b1 = tk.Button(root, text="Player 1", height=3, width=20, fg="red", bg="cyan", font=('Cursive', 14, 'bold'),
               activebackground="white", command=roll_dice)

# Player 2 button
b2 = tk.Button(root, text="Player 2", height=3, width=20, fg="red", bg="orange", font=('Cursive', 14, 'bold'),
               activebackground="light green", command=roll_dice)

# Player 1 coin
player_1 = tk.Canvas(root, width=40, height=40)
player_1.create_oval(10, 10, 40, 40, fill='blue')

# Player 2 coin
player_2 = tk.Canvas(root, width=40, height=40)
player_2.create_oval(10, 10, 40, 40, fill='red')

# Initialize turn
turn = 1


load_dice_images()
get_index()

reset_coins()
start_game()
root.mainloop()
