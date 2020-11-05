from tkinter import *
from PIL import Image, ImageTk
import random

# top-level widget which represents the main window of an application
root = Tk()
root.geometry('400x400')
root.title('Roll the Dice')

# Adding label into the frame
BlankLine = Label(root, text="")
BlankLine.pack()
# adding label with different font and formatting
HeadingLabel = Label(root, text="Welcome to Roll the dice!",fg = "light green",bg = "dark green",   font = "Helvetica 16 bold italic")
HeadingLabel.pack()
# images

die1 = open("F:/code/Roll_dice/die1.jpg", 'rb')
die2 = open("F:/code/Roll_dice/die2.jpg", 'rb')
die3 = open("F:/code/Roll_dice/die3.png", 'rb')
die4 = open("F:/code/Roll_dice/die4.png", 'rb')
die5 = open("F:/code/Roll_dice/die5.png", 'rb')
die6 = open("F:/code/Roll_dice/die6.png", 'rb')

dice = [die1, die2, die3,die4, die5, die6]
# simulating the dice with random numbers between
# 0 to 6 and generating image
DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))


# construct a label widget for image
ImageLabel = Label(root, image=DiceImage)

# packing a widget in the parent widget
ImageLabel.pack( expand=True)
# function activated by button
def rolling_dice():
    DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    # update image
    ImageLabel.configure(image=DiceImage)
    # keep a reference
    ImageLabel.image = DiceImage
# adding button, and command will use rolling_dice function
button = Button(root, text='Roll the Dice', fg='blue', command=rolling_dice)
# pack a widget in the parent widget
button.pack( expand=True)



root.mainloop()