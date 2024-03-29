from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

time_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=("Ariel", 35))
time_label.grid(column=1, row=0)

start_btn = Button(text="Start", highlightthickness=0)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="Reset", highlightthickness=0)
reset_btn.grid(column=2, row=2)

checkmark_label = Label(text="✓", bg=YELLOW , font=(FONT_NAME, 20))
checkmark_label.grid(column=1, row=4)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 133, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)


window.mainloop()