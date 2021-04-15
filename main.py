'''

'''


### Imports ###
import tkinter as tk
import tkinter.font as font
import tkinter.messagebox
import os

lbl_history = tk.messagebox

### Values for all shapes###
#rectangle, square and paralellogram values


length = 0
width = 0

#circle values
radius = 0
pi = 3.14

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

def create_window():


  #Define font
  
  myFont = font.Font(size=10)
  lbl_title = tk.Label(text = "Area / Perimeter Calculator")
  lbl_title.grid(column=0, row=0, sticky="nsew")

  #Creates the frame for the Buttons.
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

def create_filebuttons():
  #Define Font
  myFont = font.Font(size=10)

  #Define Frame
  filebuttons = tk.Frame(master=window, width=200, height=100)

  #New Equation Resets the Frame.
  btn_newequation = tk.Button(text="New Equation", master=filebuttons, command=reset_window)
  btn_newequation['font'] = myFont
  btn_newequation.grid(column=0, row=0)


  btn_savedata = tk.Button(text="Save Data", master=filebuttons, command=save_data)
  btn_savedata['font'] = myFont
  btn_savedata.grid(column=1, row=0)

  btn_viewfile = tk.Button(text="View File", master=filebuttons, command=view_file)
  btn_viewfile['font'] = myFont
  btn_viewfile.grid(column=0, row=1)

  btn_deletehistory = tk.Button(text="Delete History", master=filebuttons, command=delete_history)
  btn_deletehistory['font'] = myFont
  btn_deletehistory.grid(column=1, row=1)

  filebuttons.grid(column=0, row=3)

def reset_window():
  #This function is to have the "New Equation" button reset the frame. This would allow the user to reset the equation, or make another equation.
  clear_frame()
  create_window()

  
def save_data():
  global lbl_result
  data = lbl_result['text']

  f = open("History.txt", "a")
  f.write(data + "\n")
  f.close()

def view_file():
  os.system('python viewfile.py')

def delete_history():
  f = open("History.txt", "r+")
  f.truncate(0)
  f.write("Equation History:\n")
  f.close()

### Shape Frame Functions###

def rectangle_update_frame():
  global myFont
  global ent_length_a
  global ent_length_b
  global lbl_result
  #Clears the window, and rebuilds the window. This solves our problem with inputting the new frames. This also fixes the problem of frames overlapping when replacing the frame.
  clear_frame()
  create_window()
  create_filebuttons()
  myFont = font.Font(size=10)
  #creates new frame
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

  #This label is used for displaying the value that is selected, either Perimeter or Area.
  lbl_result = tk.Label(text="", master=input_box)
  lbl_result['font'] = myFont
  lbl_result.grid(column=0, row=3, columnspan=2, sticky="EW")
  #places grid within the window
  input_box.grid(column=0, row=2)

  
def square_update_frame():
  global ent_length_a
  global lbl_result
  myFont = font.Font(size=10)

  clear_frame()
  create_window()
  create_filebuttons()
  
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
  lbl_result.grid(column=0, row=3, columnspan=2, sticky="EW")

  input_box.grid(column=0, row=2)

def para_update_frame():
  myFont = font.Font(size=10)
  global ent_length_a
  global ent_length_b
  global ent_height
  global lbl_result
  
  clear_frame()
  create_window()
  create_filebuttons()

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

  btn_calc_peri = tk.Button(text="Perimeter", master=input_box, command=para_perimeter)
  btn_calc_peri['font'] = myFont
  btn_calc_peri.grid(column=0, row=3)

  btn_calc_area = tk.Button(text="Area", master=input_box, command=para_area)
  btn_calc_area['font'] = myFont
  btn_calc_area.grid(column=1, row=3)

  lbl_result = tk.Label(text="", master=input_box)
  lbl_result['font'] = myFont
  lbl_result.grid(column=0, row=4, columnspan=2, sticky="EW")

  input_box.grid(column=0, row=2)
  
def circle_update_frame():
  myFont = font.Font(size=10)
  global ent_radius
  global lbl_result
  clear_frame()
  create_window()
  create_filebuttons()

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

  btn_calc_area = tk.Button(text="Area", master=input_box, command=circle_area)
  btn_calc_area['font'] = myFont
  btn_calc_area.grid(column=1, row=2)

  lbl_result = tk.Label(text="", master=input_box)
  lbl_result['font'] = myFont
  lbl_result.grid(column=0, row=3, columnspan=2, sticky="EW")

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
  create_filebuttons()

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
  lbl_result.grid(column=0, row=5, columnspan=2, sticky="EW")

  input_box.grid(column=0, row=2) 

def trapisium_update_frame():
  myFont = font.Font(size=10)
  
  global lbl_length_a
  global ent_topside
  global ent_bottomside
  global ent_leftside
  global ent_rightside
  global ent_height
  global lbl_result

  clear_frame()
  create_window()
  create_filebuttons()
  
  input_box = tk.Frame(master=window)
  
  
  lbl_topside = tk.Label(text="Top", master=input_box)
  lbl_topside['font'] = myFont
  lbl_topside.grid(column=0, row=0)

  ent_topside = tk.Entry(master=input_box)
  ent_topside['font'] = myFont
  ent_topside.grid(column=1, row=0)

  lbl_bottomside = tk.Label(text="Bottom", master=input_box)
  lbl_bottomside['font'] = myFont
  lbl_bottomside.grid(column=0, row=1)

  ent_bottomside = tk.Entry(master=input_box)
  ent_bottomside['font'] = myFont
  ent_bottomside.grid(column=1, row=1)
  
  lbl_leftside = tk.Label(text="Left Side", master=input_box)
  lbl_leftside['font'] = myFont
  lbl_leftside.grid(column=0, row=2)

  ent_leftside = tk.Entry(master=input_box)
  ent_leftside['font'] = myFont
  ent_leftside.grid(column=1, row=2)
  
  lbl_rightside = tk.Label(text="Right Side", master=input_box)
  lbl_rightside['font'] = myFont
  lbl_rightside.grid(column=0, row=3)

  ent_rightside = tk.Entry(master=input_box)
  ent_rightside['font'] = myFont
  ent_rightside.grid(column=1, row=3)

  lbl_height = tk.Label(text="Height", master=input_box)
  lbl_height['font'] = myFont
  lbl_height.grid(column=0, row=4)

  ent_height = tk.Entry(master=input_box)
  ent_height['font'] = myFont
  ent_height.grid(column=1, row=4)

  btn_calc_peri = tk.Button(text="Perimeter", master=input_box, command=trap_perimeter)
  btn_calc_peri['font'] = myFont
  btn_calc_peri.grid(column=0, row=5)

  btn_calc_area = tk.Button(text="Area", master=input_box, command=trap_area)
  btn_calc_area['font'] = myFont
  btn_calc_area.grid(column=1, row=5)

  lbl_result = tk.Label(text="", master=input_box)
  lbl_result['font'] = myFont
  lbl_result.grid(column=0, row=6, columnspan=2, sticky="EW")

  input_box.grid(column=0, row=2)


### Shape Calculation Functions ###
def rectangle_perimeter():
  global length_a
  global length_b
  global ent_length_a
  global ent_length_b
  global lbl_result
  global perimeter

  #Get Values from Input Boxes 
  length_a = float(ent_length_a.get())
  length_b = float(ent_length_b.get())
  
  perimeter = ((2 * length_a) + (2 * length_b))

  lbl_result['text'] = (f"Rectangle Perimeter = (2 x {length_a}) + (2 x {length_b}) = {perimeter}")

def rectangle_area():
  global length_a
  global length_b
  global area

  
  length_a = float(ent_length_a.get())
  length_b = float(ent_length_b.get())
  
  area = (length_a * length_b)

  lbl_result['text'] = (f"Rectangle Area = {length_a} x {length_b} = {area}")

def square_perimeter():
  global length_a
  global ent_length_a
  global perimeter

  length_a = float(ent_length_a.get())

  perimeter = (length_a * 4)

  lbl_result['text'] = (f"Square Perimeter = (4 x {length_a}) = {perimeter}")

def square_area():
  global length_a
  global area

  length_a = float(ent_length_a.get())

  area = (length_a * length_a)
  lbl_result['text'] = (f"Square Area = {length_a} x {length_a} = {area}")

def para_area():
  global length_a
  global length_b
  global height
  global area

  length_a = float(ent_length_a.get())
  height = float(ent_height.get())

  area = (length_a * height)
  lbl_result['text'] = (f"Paralellogram Area = {length_a} x {height} = {area}")

def para_perimeter():
  global length_a
  global length_b
  global ent_length_a
  global ent_length_b
  global lbl_result
  global perimeter

  #Get Values from Input Boxes 
  length_a = float(ent_length_a.get())
  length_b = float(ent_length_b.get())
  
  perimeter = ((2 * length_a) + (2 * length_b))

  lbl_result['text'] = (f"Paralellogram Perimeter = (2 x {length_a}) + (2 x {length_b}) = {perimeter}")
def circle_perimeter():
  global radius
  global pi
  global perimeter

  radius = float(ent_radius.get())

  perimeter = ((2 * radius) * pi)
  lbl_result['text'] = (f"Circle Circumference = 2 x 3.14 x {radius} = {round(perimeter, 2)}")

def circle_area():
  global pi
  global radius
  global area

  radius = float(ent_radius.get())


  area = ((radius * radius) * pi)
  lbl_result['text'] = (f"Circle Area:  3.14 x ({radius} x {radius}) = {round(area, 2)}")

def triangle_perimeter():
  global side1
  global side2
  global side3
  global perimeter

  side1 = float(ent_base.get())
  side2 = float(ent_length_a.get())
  side3 = float(ent_length_b.get())

  perimeter = (side1 + side2 + side3)
  lbl_result['text'] = (f"Triangle Perimeter: {side1} + {side2} + {side3} = {perimeter}")

def triangle_area():
  global ent_base
  global ent_height
  global base
  global height
  global area

  base = float(ent_base.get())
  height = float(ent_height.get())

  area = (0.5 * base * height)
  lbl_result['text'] = (f"Triangle Area = 0.5 x {base} x {height} = {area}")

def trap_area():
  global ent_topside
  global ent_bottomside
  global ent_height
  global t_length1
  global t_length2
  global height
  global area

  t_length1 = float(ent_topside.get())
  t_length2 = float(ent_bottomside.get())
  height = float(ent_height.get())

  area = (((t_length1 * t_length2) / 2) * height)
  lbl_result['text'] = (f"Trapisium Area = 0.5 x ({t_length1} + {t_length2}) x {height} = {area}")

def trap_perimeter():
  global ent_topside
  global ent_bottomside
  global ent_height
  global t_length1
  global t_length2
  global t_length3
  global t_length4
  global perimeter

  t_length1 = float(ent_topside.get())
  t_length2 = float(ent_bottomside.get())
  t_length3 = float(ent_leftside.get())
  t_length4 = float(ent_rightside.get())

  perimeter = (t_length1 + t_length2 + t_length3 + t_length4)
  lbl_result['text'] = (f"Trapisium Perimeter = {t_length1} + {t_length2} + {t_length3} + {t_length4} = {perimeter}")




#Main Code
  
window = tk.Tk(className=" Area Perimeter Calculator")
window.geometry("500x300")
create_window()


window.mainloop()