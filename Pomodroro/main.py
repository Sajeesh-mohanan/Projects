import tkinter
from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.2
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 0.4
REPS = 0
MARKS = ""
TIMER = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global MARKS
    global REPS
    REPS = 0
    MARKS = ""
    window.after_cancel(TIMER)
    ui_setup()

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global REPS
    REPS += 1

    if REPS % 8 == 0:
        countdown(LONG_BREAK_MIN * 60)
        timer_label.config(text="Long Break", fg=RED)
    elif REPS % 2 == 0:
        countdown(SHORT_BREAK_MIN * 60)
        timer_label.config(text="Short Break", fg=PINK)
    else:
        countdown(WORK_MIN * 60)
        timer_label.config(text="Work Time", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global REPS
    global MARKS
    global TIMER
    count_min = math.floor(count / 60)
    count_sec = math.floor(count % 60)
    if count_min < 10:
        count_min = f"0{count_min}"

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        TIMER = window.after(1000, countdown, count - 1)
    else:
        if REPS % 2 != 0:
            MARKS += "✔"
            check_mark.config(text=MARKS)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
def ui_setup():
    timer_label.config(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
    canvas.itemconfig(timer_text, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
    check_mark.config(text=MARKS, fg=GREEN, bg=YELLOW)


# Window Setup
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


# timer Label
timer_label = Label()
timer_label.grid(column=1, row=0)


# canvas image
canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 111, image=tomato_img)
canvas.grid(column=1, row=1)

# canvas text
timer_text = canvas.create_text(100, 130)

# start button
start_button = Button(text="Start", borderwidth=1, highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

# reset button
reset_button = Button(text="Reset", borderwidth=1, highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# tick mark
check_mark = Label()
check_mark.grid(column=1, row=3)

ui_setup()
tkinter.mainloop()
