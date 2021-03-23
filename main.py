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

### Functions ###

### Shape Functions###

def rectangle_update_frame():
  global area
  
def paralellogram_update_frame():
  global area

def circle_update_frame():
  global area

def triangle_update_frame():
  global area
  

def trapisium_update_frame():
  global area


### Calculation Functions
def rectangle_perimeter():
  global length_a
  global length_b
  global perimeter

  perimeter = ((2 * length_a) + (2 * length_b))

def rectangle_area():
  global length_a
  global length_b
  global area

  area = (length_a * length_b)

def square_perimeter():
  global length_a
  global perimeter

  perimeter = (length_a * 4)

def square_area():
  global length_a
  global area

  area = (length_a * length_a)

def circle_perimeter():
  global radius
  global pi
  global perimeter

  perimeter = ((2 * radius) * pi)

def circle_area():
  global pi
  global radius
  global area

  area = ((radius * radius) * pi)

def triangle_perimeter():
  global side1
  global side2
  global side3
  global perimeter


#Main Code


window = tk.Tk(className="Movie Fundraising Program")
window.geometry("500x300")

#Define font
myFont = font.Font(size=10)

fr_buttons = tk.Frame(master = window)
#Create buttons for the shapes...

fr_buttons.grid(column=0, row=1)


window.mainloop()