from tkinter import *


def info():
    info = Tk()
    info.title("Info")
    info.geometry("1000x500")
    info.minsize(645, 400)
    info.maxsize(645, 400)
    info.config(bg='white')
    titre = Label(info, text="""Hangman Game """, font=('arial', 25), bg='white', fg='black')
    titre.place(x=190, y=10)

    titre = Label(info, text="""This game is in my favorites games that i make and i'm so happy for finished it.
    Because i learn a new codes and new methods for used in future it was so hard and also so funny for me 
    if you read this it's mean that you get the game you're so lucky
    Special Edition for ABRAR 
    if you want to reset the game press menu then reset the game
    and Thank you very much

<3""", font=('arial', 9), bg='white', fg='black')
    titre.place(x=20, y=100)
    QUIT = Button(info, text="Quit", command=info.destroy)
    QUIT.place(x=300, y=300)
