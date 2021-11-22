from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_sec)
        label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        label.config(text="Break", fg=PINK)
    else:
        countdown(work_sec)
        label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
        #should keep single digit numbers to display as 01/02/03 etc
    canvas.itemconfig(label, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = " "
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        #will keeping adding marks after every 25 min of work
        check_marks.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
canvas = Canvas(width=200, height=224, bg=PINK, highlightthickness=0)
window.config(padx=100, pady=50, bg=YELLOW)
# tomato = PhotoImage(file="tomato.jpg")
#RETURNED: _tkinter.TclError: couldn't recognize data in image file "tomato.jpg
#Stackoverlow and other guides recommended trying .jpg or .gif - same issue, or installing PIL
#Installed PIL, verified install and current ver but this error occurred after it installed:
# ERROR: Could not find a version that satisfies the requirement pil (from versions: none)
# ERROR: No matching distribution found for pil (so still no dice). Will continue for no without an image.
# canvas.create_image(100, 112)
timer_text = canvas.create_text(103, 112, text="00:00", fill="black", font=("Courier", 35, "bold"))
canvas.grid(column=2, row=2)

label = Label(text="Timer", font=("Courier", 35, "bold"),  highlightthickness=0)
label.grid(column=2, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=1, row=3)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=3, row=3)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=2, row=3)

window.mainloop()
