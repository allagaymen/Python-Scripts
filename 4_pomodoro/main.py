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

reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    if timer is not None:
        window.after_cancel(timer)
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    time_label.config(text="Timer", fg=GREEN)
    checkmark_label.config(text="")
    start_btn.config(state=NORMAL)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    start_btn.config(state=DISABLED)

    # Work on odd reps, a long break every 8th rep, a short break otherwise
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        time_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        time_label.config(text="Break", fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        time_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    minutes, seconds = divmod(count, 60)
    canvas.itemconfig(timer_text, text=f"{minutes:02d}:{seconds:02d}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        # One tick for each finished work session
        checkmark_label.config(text="✓" * ((reps + 1) // 2))
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

time_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35))
time_label.grid(column=1, row=0)

start_btn = Button(text="Start", highlightthickness=0, command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_btn.grid(column=2, row=2)

checkmark_label = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
checkmark_label.grid(column=1, row=4)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 133, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)


window.mainloop()