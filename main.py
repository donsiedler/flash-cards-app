from tkinter import Tk, PhotoImage, Canvas, Button

BACKGROUND_COLOR = "#B1DDC6"

# --------------------------- UI SETUP --------------------------- #
# App window
window = Tk()
window.title("Flash Cards App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Images
card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

# Card Front
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=1, column=1, columnspan=2)
canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))

# Buttons
wrong_btn = Button(image=wrong_img, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0)
wrong_btn.grid(row=2, column=1, pady=50)

right_btn = Button(image=right_img, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0)
right_btn.grid(row=2, column=2, pady=50)

window.mainloop()
