#!/use/bin/env python3
import tkinter as tk
import random
root = tk.Tk()
root.geometry("600x280")
root.title("Guess the number!")
root.resizable(False, False)
root.configure(bg="#7FFFD4")


number = random.randint(1, 100)
attempts = 10
a = "The hidden number is greating!"
b = "The hidden number is less!"
c = "You guessed right!"
d = "You've lost!"
def checking_the_number(event):
    global attempts
    entryget = entry_1.get()
    if entryget == "":
        label_1["text"]="Enter a number from 1 to 100"
    else:
        entryget = int(entryget)
        if entryget < number:
            label_1["text"]=a
            button_2.configure(state=tk.DISABLED)
            attempts -= 1
        if entryget > number:
            label_1["text"]=b
            button_2.configure(state=tk.DISABLED)
            attempts -= 1
        if entryget == number:
            label_1["text"]=c
            button_2.configure(state=tk.NORMAL)
        if attempts == 0:
            label_1["text"]=d
            button_2.configure(state=tk.NORMAL)
    label_2["text"] = f"Number of attempts: {attempts}"
    entry_1.delete(0, tk.END)
def restart_game():
    global number ,attempts
    number = random.randint(1, 100)
    attempts = 10
    label_2["text"] = f"Number of attempts: {attempts}"
    button_2.configure(state=tk.DISABLED)




label_1 = tk.Label(root, text="Enter a number from 1 to 100", fg="black", bg="#7FFFD4", font=("Arial", 20))
label_1.place(x=30, y=20)
label_2 = tk.Label(root, text=f"Number of attempts: {attempts}", fg="black", bg="#7FFFD4", font=("Arial", 20))
label_2.place(x=30, y=100)
entry_1 = tk.Entry(root, fg="#66CDAA", bg="black", font=("Arial", 15))
entry_1.place(x=40, y=140)
button_1 = tk.Button(root, text="Check", bg="#458B74", fg="white", width=10, height=1, font=("Arial", 15), command= lambda event="<Return>": checking_the_number(event))
button_1.place(x=30, y=200)
button_2 = tk.Button(root, text="Play again", bg="#458B74", fg="white", width=10, height=1, font=("Arial", 15), command=lambda event="<Return>": restart_game())
button_2.place(x=180, y=200)
root.bind('<Return>', checking_the_number)
root.mainloop()
