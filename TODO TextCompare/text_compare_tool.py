import tkinter as tk
from tkinter import scrolledtext, Text, simpledialog

def compare_texts():
    update_word_count()
    user_input = user_input_text.get("1.0", tk.END).strip()
    user_input_words = user_input.split()

    user_input_text.delete("1.0", tk.END)  # Clear current text

    idx = '1.0'
    for orig_word, input_word in zip(original_words, user_input_words):
        if orig_word == '[ ]':
            user_input_text.insert(tk.END, input_word + " ", 'fill')
        elif orig_word == input_word:
            user_input_text.insert(tk.END, input_word + " ")
        else:
            user_input_text.insert(tk.END, input_word + " ", 'highlight')

        idx = user_input_text.index(tk.END)

    if len(user_input_words) > len(original_words):
        extra_text = " ".join(user_input_words[len(original_words):])
        user_input_text.insert(tk.END, extra_text, 'highlight')

def update_original_text():
    global original_words
    new_text = simpledialog.askstring("Update Original Text", 
                                      "Enter the new text (use '[ ]' for free spaces):")
    if new_text:
        original_words = new_text.split()

def update_word_count():
    text = user_input_text.get("1.0", tk.END).strip()
    word_count.set(f"Word Count: {len(text.split())}")

# Original text stored in the program
original_text = "The quick [ ] fox jumps over the lazy dog"
original_words = original_text.split()

# Setting up the GUI window
root = tk.Tk()
root.title("Text Comparison Tool")
root.geometry("800x600")

# Description label
description_label = tk.Label(root, text="This tool can be used to compare text.", font=("Arial", 12))
description_label.pack(pady=5)

# Text input area
user_input_label = tk.Label(root, text="Enter your text:", font=("Arial", 14))
user_input_label.pack(pady=10)

user_input_text = scrolledtext.ScrolledText(root, height=15, width=70, font=("Arial", 12))
user_input_text.pack(padx=20, pady=20)
user_input_text.bind("<KeyRelease>", lambda event: update_word_count())

# Highlighting configuration
user_input_text.tag_configure('highlight', background='yellow', foreground='red')
user_input_text.tag_configure('fill', background='lightgrey', foreground='black')

# Word count
word_count = tk.StringVar()
word_count_label = tk.Label(root, textvariable=word_count, font=("Arial", 12))
word_count_label.pack(pady=5)

# Compare and Update buttons
compare_button = tk.Button(root, text="Compare Texts", command=compare_texts, font=("Arial", 14))
compare_button.pack(pady=10)

update_button = tk.Button(root, text="Update Original Text", command=update_original_text, font=("Arial", 14))
update_button.pack(pady=10)

# Start the GUI
root.mainloop()
