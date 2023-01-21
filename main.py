import pandas
import random
from tkinter import Tk, PhotoImage, Canvas, Button

BACKGROUND_COLOR = "#B1DDC6"

# ------------------------ READ CSV DATA ------------------------- #
try:
    words_to_learn = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    with open("data/words_to_learn.csv", "w"):
        # Creates a new csv file 'words_to_learn' if it doesn't exist
        pass
except pandas.errors.EmptyDataError:
    words_to_learn = pandas.read_csv("data/french_words.csv")

to_learn = words_to_learn.to_dict(orient="records")
print(f"Words to learn: {len(to_learn)}")
current_card = {}


# ---------------------------- CARDS ----------------------------- #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    try:
        current_card = random.choice(to_learn)
    except IndexError:
        canvas.itemconfig(card, image=card_front_img)
        canvas.itemconfig(card_title, text="Congrats", fill="black")
        canvas.itemconfig(card_word, text="No cards left!", fill="black")
    else:
        canvas.itemconfig(card, image=card_front_img)
        canvas.itemconfig(card_title, text="French", fill="black")
        canvas.itemconfig(card_word, text=current_card["French"], fill="black")
        flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


# ----------------- ANSWERS AND SAVING PROGRESS ------------------ #

def known_word():
    next_card()
    try:
        to_learn.remove(current_card)
    except ValueError:
        return
    else:
        df = pandas.DataFrame(to_learn)
        df.to_csv("data/words_to_learn.csv", index=False)


def unknown_word():
    next_card()


# --------------------------- UI SETUP --------------------------- #
# App window
window = Tk()
window.title("Flash Cards App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

# Images
card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

# Card Front
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=1, column=1, columnspan=2)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

# Buttons
wrong_btn = Button(image=wrong_img, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0, command=unknown_word)
wrong_btn.grid(row=2, column=1, pady=50)

right_btn = Button(image=right_img, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0, command=known_word)
right_btn.grid(row=2, column=2, pady=50)

# Show first card after running the app
next_card()

window.mainloop()
