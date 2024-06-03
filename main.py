from tkinter import *
import tkinter as tk
import random

# ------ Text Prompts ---- #
random_prompts = {
    1: "There were thousands of the strange things crawling around.",
    2: "Rain was the only comfort on a night like this.",
    3: "BOOM! BANG! More noise came from nearby.",
    4: "Sunlight all but disappeared under the canopy.",
    5: "He had seen her face. A mistake she couldn't let go.",
    6: "No one suspected that he was the one behind it all.",
    7: "Curious little spirits rose up around her feet. They seemed harmless."
}


# ------ Functions ----- #
def on_text_change(event):
    # Update the height of the text widget as user types to fit content and starts timer
    text_entry.config(height=(text_entry.get("1.0", "end-1c").count("\n") + 1))
    start_timer()  # Start timer whenever there is a text change


def start_timer():
    global timer_id
    if timer_id:
        window.after_cancel(timer_id)  # Cancel the previous timer
    timer_id = window.after(5000, clear_text)  # Set the timer for 5 seconds (5000 milliseconds)


def clear_text():
    text_entry.delete("1.0", "end")  # Delete all text in the text field


def on_timer_reset(event):
    start_timer()  # Reset the timer on key release


def select_prompt():
    get_prompt = random_prompts[random.randint(1, 7)]
    prompt_text.config(text=f"{get_prompt}")
    text_entry.focus()


# ----- UI SETUP ----- #
window = Tk()
window.title("Type or Lose it!")
window.config(background="teal", padx=10, pady=10)
logo_frame = tk.Frame(window)
logo_frame.pack()
logo_frame.pack_configure(side="left")
timer_id = None  # Initialize the timer ID
logo = PhotoImage(file='logo.png')

# ----- Buttons ----- #
prompt = tk.Button(window, text="Get Prompt", command=select_prompt)

# ------ Labels ------ #
instructions = tk.Label(window, text="Get a random prompt and then start typing. If you stop, it's all gone!",
                        background="teal", font=("Arial", 12), foreground="white")
instructions.pack()
instructions.pack_configure(pady=10, padx=10)

prompt.pack()

prompt_text = tk.Label(window, text="", font=("Helvetica", 20), background="teal", wraplength=700)
prompt_text.pack()

logo_label = tk.Label(logo_frame, image=logo, background="teal")
logo_label.pack()

# ----- Text ------ #

text_entry = tk.Text(window, wrap="word", height=10, background="light grey")
text_entry.pack()
text_entry.pack_configure(side="bottom", padx=10, pady=10)
text_entry.bind("<Key>", on_text_change)  # Start the timer on text change
text_entry.bind("<KeyRelease>", on_timer_reset)  # Reset the timer on key release

# ------- mainloop ---- #
window.mainloop()
