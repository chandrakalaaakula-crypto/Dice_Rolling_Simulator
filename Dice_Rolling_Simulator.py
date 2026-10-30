
import tkinter as tk
import random

def roll_dice():
    dice_faces = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]

    result = random.randint(1, 6)

    dice_label.config(text=dice_faces[result - 1])
    result_label.config(text=f"You rolled: {result}")

# Create main window
root = tk.Tk()
root.title("Dice Rolling Simulator")
root.geometry("400x450")
root.configure(bg="#eaf2f8")

# Heading
heading = tk.Label(
    root,
    text="DICE ROLLING SIMULATOR",
    font=("Arial", 18, "bold"),
    bg="#eaf2f8",
    fg="#154360"
)
heading.pack(pady=25)

# Dice display
dice_label = tk.Label(
    root,
    text="🎲",
    font=("Arial", 100),
    bg="#eaf2f8"
)
dice_label.pack(pady=20)

# Result display
result_label = tk.Label(
    root,
    text="Click the button to roll!",
    font=("Arial", 16, "bold"),
    bg="#eaf2f8",
    fg="#239b56"
)
result_label.pack(pady=15)

# Roll button
roll_button = tk.Button(
    root,
    text="ROLL DICE",
    command=roll_dice,
    font=("Arial", 15, "bold"),
    bg="#2874a6",
    fg="white",
    width=15,
    height=2
)
roll_button.pack(pady=25)

# Exit button
exit_button = tk.Button(
    root,
    text="EXIT",
    command=root.destroy,
    font=("Arial", 11),
    bg="#c0392b",
    fg="white",
    width=10
)
exit_button.pack(pady=5)

# Run application
root.mainloop()
