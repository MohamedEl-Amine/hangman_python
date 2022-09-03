from tkinter import *
from tkinter import ttk
from all_words import words
from info import info
import random
import string
from PIL import Image, ImageTk
from googletrans import Translator 


def hangman():
    global word, word_letter, alphabet, used_letters, entry, check, user_letter, ok, used_letters, lives
    lives = 7
    word = get_valid_word(words)
    word_letter = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    
    translater = Translator()
    out = translater.translater(word,dest='ar')
    y = f"Guess a character then press OK {out}"
    Scomment["text"] = y
    word_list = [letter if letter in used_letters else '-' for letter in word]
    x = ["Current word: ", word_list]
    com = str(x).replace('}', '').replace('}', '').replace('[', '').replace(']', '').replace('\'', '').replace(',', '')
    comment["text"] = com
    xx = ["you still have", lives, "lives"]
    l = str(xx).replace('}', '').replace('}', '').replace('[', '').replace(']', '').replace('\'', '').replace(',', '')
    lives_label["text"] = l

    entry = Entry(welcome_window)
    entry.place(x=395, y=200)
    ok = ttk.Button(welcome_window, text="OK", command=check_letter)
    ok.place(x=420, y=250)
    check_lives()


def check_lives():
    global lives, name_player, try_again, win
    lives -= 1
    xx = ["you still have", lives, "lives"]
    l = str(xx).replace('}', '').replace('}', '').replace('[', '').replace(']', '').replace('\'', '').replace(',', '')
    lives_label["text"] = l
    print(lives)
    comment["text"] = ""

    if lives == 0:
        ok.destroy()
        entry.config(state=DISABLED)
        lives_label['text'] = "your guy is dead :')"
        unfor = ["Unfortunately", name_player, " you lose", word]
        Unfortunately = str(unfor).replace('}', '').replace('}', '').replace('[', '').replace(']', '').replace('\'',
                                                                                                               '').replace(
            ',', '')
        Scomment["text"] = Unfortunately
        ok.destroy()
        try_again = Button(welcome_window, text="Try Again", command=reset)
        try_again.place(x=420, y=250)
        win = False


def check_if_win():
    global count_word, win, try_again
    user_letter = entry.get().upper()
    y = "Guess the next character"
    Scomment["text"] = y
    if len(word_letter) > 0:
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)

            if user_letter in word_letter:
                word_letter.remove(user_letter)
                happy_hangman()
            else:
                angry_hangman()
                check_lives()
            x1 = ['You have print these letter ', ' '.join(used_letters)]
            com1 = str(x1).replace('}', '').replace('}', '').replace('[', '').replace(']', '').replace('\'',
                                                                                                       '').replace(
                ',', '')
            alert_label["text"] = com1
        elif user_letter in used_letters:
            x3 = ["you already used this letter, Please choose another"]
            com3 = str(x3).replace('}', '').replace('}', '').replace('[', '').replace(']', '').replace('\'', '')
            alert_label["text"] = com3


        else:
            x4 = ['you type a invalid character']
            com4 = str(x4).replace('}', '').replace('}', '').replace('[', '').replace(']', '').replace('\'',
                                                                                                       '').replace(
                ',', '')
            alert_label["text"] = com4

    word_list = [letter if letter in used_letters else '*' for letter in word]
    print(word_list)
    x2 = ["Current word: ", word_list]
    com2 = str(x2).replace('}', '').replace('}', '').replace('[', '').replace(']', '').replace('\'', '').replace(
        ',', '')
    comment["text"] = com2
    entry.delete(0, END)

    if len(word_letter) <= 0:
        x5 = ["you did it you print the correct word: ", word]
        com5 = str(x5).replace('}', '').replace('}', '').replace('[', '').replace(']', '').replace('\'', '').replace(
            ',', '')
        comment["text"] = com5
        entry.config(state=DISABLED)
        ok.destroy()
        try_again = Button(welcome_window, text="Try Again", command=reset)
        try_again.place(x=420, y=250)
        count_word += 1
        you_got = ["you got ", count_word, " words correct"]
        Scomment["text"] = str(you_got).replace('}', '').replace('}', '').replace('[', '').replace(']', '').replace(
            '\'', '').replace(
            ',', '')
        lives_label['text'] = "your gay alive:)"
        win = True


def get_valid_word(w):
    word = random.choice(w)
    while '-' in word or ' ' in word:
        words.remove(word)
        word = random.choice(w)
    return word.upper()


def check_letter():
    letter = entry.get()
    if len(letter) > 1 or len(letter) < 1:
        alert_label['text'] = "Please enter one character"
        alert_label.place(x=380, y=280)
    else:
        check_if_win()


def lets_gofunction():
    global welcome_window, hi_text, enter_yourname, lets_go, alert_label, name_player
    name_player = enter_yourname.get()

    if name_player == '':
        alert_label["text"] = "Please write a name"
    else:
        text = "Welcome ", name_player, " in the game i wish you a good luck"
        strippedText = str(text).replace('(', '').replace(')', '').replace('\'', '').replace(',', '')
        alert_label["text"] = strippedText
        alert_label.place(x=320, y=280)
        hi_text.after(50, hi_text.destroy())
        lets_go.after(50, lets_go.destroy())
        enter_yourname.after(50, enter_yourname.destroy())
        hangman()


def wel_window():
    global enter_yourname, welcome_window, hi_text, enter_yourname, lets_go, canvas1
    hi_text = Label(welcome_window, text="""Hello player do you want to play Hangman ah..
    Just type your name and let's get start""", font=('Berlin Sans FB', 20))
    hi_text.place(x=200, y=120)
    enter_yourname = ttk.Entry(welcome_window)
    enter_yourname.place(x=395, y=200)
    lets_go = ttk.Button(welcome_window, text="Let's GO..", command=lets_gofunction)
    lets_go.place(x=420, y=250)


welcome_window = Tk()
welcome_window.title("Hangman Game")
welcome_window.maxsize(800, 400)
welcome_window.minsize(800, 400)
welcome_window.iconbitmap("icons\hangman.ico")


def happy_hangman():
    canvas.itemconfig(image_container, image=img3)


def angry_hangman():
    canvas.itemconfig(image_container, image=img2)


def normal_hangman():
    canvas.itemconfig(image_container, image=img1)


canvas = Canvas(welcome_window, width=650, height=350)
canvas.place(x=50, y=50)

img1 = PhotoImage(file="icons/hangman.png")
img2 = PhotoImage(file="icons/angryhangman.png")
img3 = PhotoImage(file="icons/happyhangman.png")

image_container = canvas.create_image(0, 0, anchor="nw", image=img1)

alert_label = Label(welcome_window, text="")
alert_label.place(x=400, y=280)
comment = Label(welcome_window, text="", font=('Berlin Sans FB', 20))
comment.place(x=220, y=80)
Scomment = Label(welcome_window, text="", font=('Berlin Sans FB', 20))
Scomment.place(x=220, y=120)
lives_label = Label(welcome_window, text="", font=('Berlin Sans FB', 15))
lives_label.place(x=50, y=260)
by_me = Label(welcome_window, text="By Med Amine", font=('Berlin Sans FB', 9))
by_me.place(x=10, y=370)
Quit = ttk.Button(welcome_window, text="Quit", command=welcome_window.destroy)
Quit.place(x=700, y=360)
info = ttk.Button(welcome_window, text="Info", command=info)
info.place(x=620, y=360)


def reset():
    global count_word, lives
    lives = 6
    normal_hangman()
    try:
        ok.destroy()
        try_again.destroy()
    except:
        pass
    alert_label["text"] = ""
    comment["text"] = ""
    Scomment["text"] = ""
    lives_label["text"] = ""
    if win == False:
        count_word = 0
        hangman()
    elif win == True:
        hangman()
    else:
        wel_window()


def reset_all_game():
    global count_word, lives, win
    win = None
    lives = 6
    normal_hangman()
    try:
        ok.destroy()
        try_again.destroy()
    except:
        pass
    alert_label["text"] = ""
    comment["text"] = ""
    Scomment["text"] = ""
    lives_label["text"] = ""
    wel_window()


count_word = 0
menu_barre = Menu(welcome_window)
reset_menu = Menu(menu_barre, tearoff=0)
reset_menu.add_command(label="Reset the game", command=reset_all_game)
menu_barre.add_cascade(label="Menu", menu=reset_menu)
welcome_window.config(menu=menu_barre)
reset_all_game()

welcome_window.mainloop()
