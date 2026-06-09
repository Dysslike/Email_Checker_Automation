from tkinter import *
import tkinter as tk


root = tk.Tk()
root.geometry("300x200")
root.title("Did you get hired?")

tk.Label(root, text="Email:").grid(row=0, column=0)
tk.Label(root, text="Password:").grid(row=1, column=0)

entry_email = tk.Entry(root)
entry_password = tk.Entry(root, show="*")

entry_email.grid(row=0, column=1)
entry_password.grid(row=1, column=1)

root.mainloop()