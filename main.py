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
canvas = Canvas(width=200, height=224, bg=PINK, highlightthickness=0)
window.config(padx=100, pady=50, bg=YELLOW)
# tomato = PhotoImage(file="tomato.jpg")
#RETURNED: _tkinter.TclError: couldn't recognize data in image file "tomato.jpg
#Stackoverlow and other guides recommended trying .jpg or .gif - same issue, or installing PIL
#Installed PIL, verified install and current ver but this error occurred after it installed:
# ERROR: Could not find a version that satisfies the requirement pil (from versions: none)
# ERROR: No matching distribution found for pil (so still no dice). Will continue for no without an image.
canvas.create_image(100, 112)
canvas.create_text(103, 112, text="00:00", fill="black", font=("Courier", 35, "bold"))
canvas.grid(column=2, row=2)

label = Label(text="Timer", font=("Courier", 35, "bold"),  highlightthickness=0)
# label.config(text="This is new text")
label.grid(column=2, row=1)

start_button = Button(text="Start", highlightthickness=0)
start_button.grid(column=1, row=3)

reset_button = Button(text="Reset", highlightthickness=0)
reset_button.grid(column=3, row=3)



window.mainloop()
