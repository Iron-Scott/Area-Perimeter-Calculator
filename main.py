''''
Current Update: Functions and Values added. Working on adding a frame including just the buttons, with the ability to click on it, and another frame opens up, allowing users to input new values.

Current options: 
'''


### Imports ###
import tkinter as tk
import tkinter.font as font
import tkinter.messagebox


### Values for all shapes###
#rectangle, square and paralellogram values
length = 0
width = 0

#circle values
radius = 0
pi = 3.14159

#triangle values
side1 = 0
side2 = 0
side3 = 0

base = 0
height = 0

#trapisium lengths

t_length1 = 0
t_length2 = 0
t_length3 = 0
t_length4 = 0
t_height = 0

#final values
perimeter = 0
area = 0
#myFont = font.Font(size=10)

### Functions ###
def clear_frame():
  for widget in window.winfo_children():
    widget.destroy()
### Shape Functions###

def rectangle_update_frame():
  global myFont
  global ent_length_a
  global ent_length_b
  global lbl_result
  clear_frame()
  create_window()
  myFont = font.Font(size=10)
  input_box = tk.Frame(master=window)
  

  lbl_length_a = tk.Label(text="Length A", master=input_box)
  lbl_length_a['font'] = myFont
  lbl_length_a.grid(column=0, row=0)

  ent_length_a = tk.Entry(master=input_box)
  ent_length_a['font'] = myFont
  ent_length_a.grid(column=1, row=0)

  lbl_length_b = tk.Label(text="Length B", master=input_box)
  lbl_length_b['font'] = myFont
  lbl_length_b.grid(column=0, row=1)

  ent_length_b = tk.Entry(master=input_box)
  ent_length_b['font'] = myFont
  ent_length_b.grid(column=1, row=1)

  btn_calc_peri = tk.Button(text="Perimeter", master=input_box, command=rectangle_perimeter)
  btn_calc_peri['font'] = myFont
  btn_calc_peri.grid(column=0, row=2)
  
  btn_calc_area = tk.Button(text="Area", master=input_box, command=rectangle_area)
  btn_calc_area['font'] = myFont
  btn_calc_area.grid(column=1, row=2)

  lbl_result = tk.Label(text="", master=input_box)
  lbl_result['font'] = myFont
  lbl_result.grid(column=0, row=3)

  input_box.grid(column=0, row=2)

  
def square_update_frame():
  global ent_length_a
  global lbl_result
  myFont = font.Font(size=10)

  clear_frame()
  create_window()
  
  input_box = tk.Frame(master=window)
  
  lbl_length_a = tk.Label(text="Length", master=input_box)
  lbl_length_a['font'] = myFont
  lbl_length_a.grid(column=0, row=0)

  ent_length_a = tk.Entry(master=input_box)
  ent_length_a['font'] = myFont
  ent_length_a.grid(column=1, row=0)

  btn_calc_peri = tk.Button(text="Perimeter", master=input_box, command=square_perimeter)
  btn_calc_peri['font'] = myFont
  btn_calc_peri.grid(column=0, row=2)

  btn_calc_area = tk.Button(text="Area", master=input_box, command=square_area)
  btn_calc_area['font'] = myFont
  btn_calc_area.grid(column=1, row=2)

  lbl_result = tk.Label(text="", master=input_box)
  lbl_result['font'] = myFont
  lbl_result.grid(column=0, row=3)

  input_box.grid(column=0, row=2)

def para_update_frame():
  myFont = font.Font(size=10)
  global ent_length_a
  global ent_length_b
  global ent_height
  global lbl_result
  clear_frame()
  create_window()

  input_box = tk.Frame(master=window)
  
  

  lbl_length_a = tk.Label(text="Base", master=input_box)
  lbl_length_a['font'] = myFont
  lbl_length_a.grid(column=0, row=0)

  ent_length_a = tk.Entry(master=input_box)
  ent_length_a['font'] = myFont
  ent_length_a.grid(column=1, row=0)

  lbl_length_b = tk.Label(text="Side", master=input_box)
  lbl_length_b['font'] = myFont
  lbl_length_b.grid(column=0, row=1)

  ent_length_b = tk.Entry(master=input_box)
  ent_length_b['font'] = myFont
  ent_length_b.grid(column=1, row=1)

  lbl_height = tk.Label(text="Height", master=input_box)
  lbl_height['font'] = myFont
  lbl_height.grid(column=0, row=2)

  ent_height = tk.Entry(master=input_box)
  ent_height['font'] = myFont
  ent_height.grid(column=1, row=2)

  btn_calc_peri = tk.Button(text="Perimeter", master=input_box, command=rectangle_perimeter)
  btn_calc_peri['font'] = myFont
  btn_calc_peri.grid(column=0, row=3)

  btn_calc_area = tk.Button(text="Area", master=input_box, command=para_area)
  btn_calc_area['font'] = myFont
  btn_calc_area.grid(column=1, row=3)

  lbl_result = tk.Label(text="", master=input_box)
  lbl_result['font'] = myFont
  lbl_result.grid(column=0, row=4)

  input_box.grid(column=0, row=2)
  
def circle_update_frame():
  myFont = font.Font(size=10)
  global ent_radius
  global lbl_result
  clear_frame()
  create_window()

  input_box = tk.Frame(master=window)


  lbl_length_a = tk.Label(text="Radius", master=input_box)
  lbl_length_a['font'] = myFont
  lbl_length_a.grid(column=0, row=0)

  ent_radius = tk.Entry(master=input_box)
  ent_radius['font'] = myFont
  ent_radius.grid(column=1, row=0)

  btn_calc_peri = tk.Button(text="Circumference", master=input_box, command=circle_perimeter)
  btn_calc_peri['font'] = myFont
  btn_calc_peri.grid(column=0, row=2)

  btn_calc_area = tk.Button(text="Area", master=input_box, command=circle_perimeter)
  btn_calc_area['font'] = myFont
  btn_calc_area.grid(column=1, row=2)

  fr_result = tk.Frame(master=input_box)
  lbl_result = tk.Label(text="", master=fr_result)
  lbl_result['font'] = myFont
  lbl_result.grid(column=0, row=0)
  fr_result.grid(column=1, row=3)


  input_box.grid(column=0, row=2)
  
def triangle_update_frame():
  myFont = font.Font(size=10)

  global ent_base
  global ent_height
  global ent_length_a
  global ent_length_b
  global lbl_result
  clear_frame()
  create_window()

  input_box = tk.Frame(master=window)
  


  lbl_base = tk.Label(text="Base", master=input_box)
  lbl_base['font'] = myFont
  lbl_base.grid(column=0, row=0)

  ent_base = tk.Entry(master=input_box)
  ent_base['font'] = myFont
  ent_base.grid(column=1, row=0)

  lbl_length_a = tk.Label(text="Side A", master=input_box)
  lbl_length_a['font'] = myFont
  lbl_length_a.grid(column=0, row=1)

  ent_length_a = tk.Entry(master=input_box)
  ent_length_a['font'] = myFont
  ent_length_a.grid(column=1, row=1)
  
  lbl_length_b = tk.Label(text="Side B", master=input_box)
  lbl_length_b['font'] = myFont
  lbl_length_b.grid(column=0, row=2)

  ent_length_b = tk.Entry(master=input_box)
  ent_length_b['font'] = myFont
  ent_length_b.grid(column=1, row=2)
  
  lbl_height = tk.Label(text="Height", master=input_box)
  lbl_height['font'] = myFont
  lbl_height.grid(column=0, row=3)

  ent_height = tk.Entry(master=input_box)
  ent_height['font'] = myFont
  ent_height.grid(column=1, row=3)
  
  btn_calc_peri = tk.Button(text="Perimeter", master=input_box, command=triangle_perimeter)
  btn_calc_peri['font'] = myFont
  btn_calc_peri.grid(column=0, row=4)

  btn_calc_area = tk.Button(text="Area", master=input_box, command=triangle_area)
  btn_calc_area['font'] = myFont
  btn_calc_area.grid(column=1, row=4)

  lbl_result = tk.Label(text="", master=input_box)
  lbl_result['font'] = myFont
  lbl_result.grid(column=0, row=5)

  input_box.grid(column=0, row=2)
  

def trapisium_update_frame():
  myFont = font.Font(size=10)
  clear_frame()
  create_window()
  
  input_box = tk.Frame(master=window)
  
  
  lbl_length_a = tk.Label(text="Length A", master=input_box)
  lbl_length_a['font'] = myFont
  lbl_length_a.grid(column=0, row=0)

  ent_radius = tk.Entry(master=input_box)
  ent_radius['font'] = myFont
  ent_radius.grid(column=1, row=0)

  lbl_length_b = tk.Label(text="Length B", master=input_box)
  lbl_length_b['font'] = myFont
  lbl_length_b.grid(column=0, row=1)

  ent_length_b = tk.Entry(master=input_box)
  ent_length_b['font'] = myFont
  ent_length_b.grid(column=1, row=1)
  
  lbl_length_c = tk.Label(text="Length C", master=input_box)
  lbl_length_c['font'] = myFont
  lbl_length_c.grid(column=0, row=2)

  ent_length_c = tk.Entry(master=input_box)
  ent_length_c['font'] = myFont
  ent_length_c.grid(column=1, row=2)
  
  lbl_length_c = tk.Label(text="Length D", master=input_box)
  lbl_length_c['font'] = myFont
  lbl_length_c.grid(column=0, row=3)

  ent_length_c = tk.Entry(master=input_box)
  ent_length_c['font'] = myFont
  ent_length_c.grid(column=1, row=3)

  lbl_height = tk.Label(text="Height", master=input_box)
  lbl_height['font'] = myFont
  lbl_height.grid(column=0, row=4)

  ent_length_c = tk.Entry(master=input_box)
  ent_length_c['font'] = myFont
  ent_length_c.grid(column=1, row=4)

  btn_calc_peri = tk.Button(text="Perimeter", master=input_box)
  btn_calc_peri['font'] = myFont
  btn_calc_peri.grid(column=0, row=5)

  btn_calc_area = tk.Button(text="Area", master=input_box)
  btn_calc_area['font'] = myFont
  btn_calc_area.grid(column=1, row=5)

  lbl_result = tk.Label(text="", master=input_box)
  lbl_result['font'] = myFont
  lbl_result.grid(column=0, row=6)

  input_box.grid(column=0, row=2)


### Calculation Functions
def rectangle_perimeter():
  global length_a
  global length_b
  global ent_length_a
  global ent_length_b
  global lbl_result
  global perimeter

  length_a = float(ent_length_a.get())
  length_b = float(ent_length_b.get())
  
  perimeter = ((2 * length_a) + (2 * length_b))

  lbl_result['text'] = (f"Perimeter: {perimeter}")

def rectangle_area():
  global length_a
  global length_b
  global area

  
  length_a = float(ent_length_a.get())
  length_b = float(ent_length_b.get())
  
  area = (length_a * length_b)

  lbl_result['text'] = (f"Area: {area}")

def square_perimeter():
  global length_a
  global ent_length_a
  global perimeter

  length_a = float(ent_length_a.get())

  perimeter = (length_a * 4)

  lbl_result['text'] = (f"Perimeter: {perimeter}")

def square_area():
  global length_a
  global area

  length_a = float(ent_length_a.get())

  area = (length_a * length_a)
  lbl_result['text'] = (f"Area: {area}")

def para_area():
  global length_a
  global length_b
  global height
  global area

  length_a = float(ent_length_a.get())
  height = float(ent_height.get())

  area = (length_a * height)
  lbl_result['text'] = (f"Area: {area}")

def circle_perimeter():
  global radius
  global pi
  global perimeter

  radius = float(ent_radius.get())

  perimeter = ((2 * radius) * pi)
  lbl_result['text'] = (f"Circumference: {perimeter}")

def circle_area():
  global pi
  global radius
  global area

  radius = float(ent_radius.get())


  area = ((radius * radius) * pi)

def triangle_perimeter():
  global side1
  global side2
  global side3
  global perimeter

  side1 = float(ent_base.get())
  side2 = float(ent_length_a.get())
  side3 = float(ent_length_b.get())

  perimeter = (side1 + side2 + side3)
  lbl_result['text'] = (f"Perimeter: {perimeter}")

def triangle_area():
  global ent_base
  global ent_height
  global base
  global height
  global area

  base = float(ent_base.get())
  height = float(ent_height.get())

  area = (0.5 * base * height)
  lbl_result['text'] = (f"Area: {area}")

def create_window():


  #Define font
  
  myFont = font.Font(size=10)
  lbl_title = tk.Label(text = "Area / Perimeter Calculator")
  lbl_title.grid(column=0, row=0, sticky="nsew")


  fr_buttons = tk.Frame(master = window)
  #Create buttons for the shapes...
  rectangle = tk.Button(text="Rectangle", master=fr_buttons, command=rectangle_update_frame)
  rectangle['font'] = myFont
  rectangle.grid(column=0, row=0, sticky="nsew")

  square = tk.Button(text="Square", master=fr_buttons, command=square_update_frame)
  square['font'] = myFont
  square.grid(column=1, row=0, sticky="nsew")

  para = tk.Button(text="Paralellogram", master=fr_buttons, command=para_update_frame)
  para['font'] = myFont
  para.grid(column=2, row=0, sticky="nsew")

  circle = tk.Button(text="Circle", master=fr_buttons, command=circle_update_frame)
  circle['font'] = myFont
  circle.grid(column=0, row=1, sticky="nsew")

  triangle = tk.Button(text="Triangle", master=fr_buttons, command=triangle_update_frame)
  triangle['font'] = myFont
  triangle.grid(column=1, row=1, sticky="nsew")

  trapisium = tk.Button(text="Trapisium", master=fr_buttons, command=trapisium_update_frame)
  trapisium['font'] = myFont
  trapisium.grid(column=2, row=1, sticky="nsew")

  fr_buttons.grid(column=0, row=1)

#Main Code
  
window = tk.Tk(className=" Area Perimeter Calculator")
window.geometry("500x300")
create_window()


window.mainloop()