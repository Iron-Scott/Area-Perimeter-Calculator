import tkinter as tk

window = tk.Tk()

def read_data():
  f = open("History.txt", "r")
  data = f.read()
  lbl_history['text'] = data


lbl_history = tk.Label(master=window)
lbl_history.grid(column=0, row=0)

read_data()
window.mainloop()