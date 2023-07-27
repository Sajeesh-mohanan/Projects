import random
from tkinter import *
import pandas as pd

# ---------------------------Initializing constant Values----------------------------------------------
GREEN = "#b1ddc6"
FONT_1 = ('Adobe Heiti Std R', 35, 'bold italic')
FONT_2 = ('Action Man', 25, 'bold')

window = Tk()
window.title("Flash card")
window.config(padx=40, pady=50, bg=GREEN)
DATA = pd.read_csv("spanish to english.csv")
INDEX_VALUE = None


# -----------------------------Three-second timer------------------------------------------------------
def countdown(count):
    if count > 0:
        timer = window.after(1000, countdown, count-1)

    # ----------------flipping back side of the card after 3 second.-----------------------
    else:
        back_card()


# -------------loading the correct answer to crt_answer.csv and dropping it from default csv file-------
def correct_ans():
    # ----------------------loading values from correct_answers.csv-------------------------------------
    try:
        crt_data = pd.read_csv("correct_answers.csv")
        spanish_list = crt_data["Spanish"].to_list()
        english_list = crt_data["English"].to_list()

    # ------------------create a new file if no file found in the folder.-------------------------------
    except (FileNotFoundError, pd.errors.EmptyDataError):
        DATA[DATA["Spanish"] == DATA.Spanish[INDEX_VALUE]].to_csv("correct_answers.csv", index=False)

    # -----------------updating new correct answer value to correct_answers.csv------------------------
    else:
        if DATA.Spanish[INDEX_VALUE] in spanish_list:
            pass
        else:
            spanish_list.append(DATA.Spanish[INDEX_VALUE])
            english_list.append(DATA.English[INDEX_VALUE])
            dict = {"Spanish": spanish_list,
                    "English": english_list}
            pd.DataFrame(dict).to_csv("correct_answers.csv", index=False)

    # ----------------dropping the correct answer from default csv-----------------------------
    finally:
        DATA.drop(INDEX_VALUE).to_csv("spanish to english.csv", index=False)
        front_card()


# -------------------Back side of the card english translated---------------------------------
def back_card():
    # changing canvas items to back side of the card
    canvas.itemconfig(flashcard, image=flashcard_img_back)
    canvas.itemconfig(label, text="English")
    canvas.itemconfig(word, text=DATA.English[INDEX_VALUE])

    # -----------changing command functions so that it will only function while card is on the back side.-------------
    crt_button.config(command=correct_ans)
    wrg_button.config(command=front_card)


# ---------------------------front card display----------------------------------------------------
def front_card():
    global INDEX_VALUE
    global DATA
    # -------------------Loading updated csv file to data-----------------------------------------
    DATA = pd.read_csv("spanish to english.csv")

    # ---------------random index value to get random row from csv file---------------------------
    INDEX_VALUE = random.randint(0, len(DATA))

    # -------------------------Canvas item of front card------------------------------------------
    canvas.itemconfig(flashcard, image=flashcard_img_front)
    canvas.itemconfig(label, text="Spanish")
    canvas.itemconfig(word, text=DATA.Spanish[INDEX_VALUE])

    # ------setting correct button command to ull so that it won't function in front card---------
    crt_button.config(command="")
    wrg_button.config(command="")
    # ----------------------to flip the card after 3 seconds--------------------------------------
    countdown(3)


# --------------------------------creating canvas-------------------------------------------------
canvas = Canvas(height=600, width=900, bg=GREEN, highlightthickness=0)

# -----------------------------Canvas flash card image-------------------------------------------
flashcard_img_back = PhotoImage(file="../images/card_back.png")
flashcard_img_front = PhotoImage(file="../images/card_front.png")
crt_img = PhotoImage(file="../images/right.png")
wrg_img = PhotoImage(file="../images/wrong.png")
flashcard = canvas.create_image(450, 320, image=flashcard_img_front)

# ---------------------------language label in flash card---------------------------------------
label = canvas.create_text(450, 200, text="Spanish", font=FONT_1, fill="black")

# ----------------------------------word label--------------------------------------------------

word = canvas.create_text(450, 300, font=FONT_2, fill="black")
canvas.grid(row=0, column=0, columnspan=2)

# --------------------------------correct button-----------------------------------------------
crt_button = Button(image=crt_img, borderwidth=0, highlightthickness=0)
crt_button.grid(row=2, column=1)

# --------------------------------wrong button-------------------------------------------------
wrg_button = Button(image=wrg_img, borderwidth=0, highlightthickness=0)
wrg_button.grid(row=2, column=0)

front_card()

Tk.mainloop(window)
