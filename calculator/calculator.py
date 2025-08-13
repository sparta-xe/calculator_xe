#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk


# In[3]:


def click(event):
    current = str(entry.get())
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)


root = tk.Tk()
root.geometry("300x400")
root.title("Simple Calculator")


entry = tk.Entry(root, font="Arial 20")
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)


button_frame = tk.Frame(root)
button_frame.pack()


buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]


for row in buttons:
    frame = tk.Frame(button_frame)
    frame.pack(expand=True, fill="both")
    for btn_text in row:
        btn = tk.Button(frame, text=btn_text, font="Arial 18", relief="ridge", border=1)
        btn.pack(side="left", expand=True, fill="both", padx=2, pady=2)
        btn.bind("<Button-1>", click)


root.mainloop()



