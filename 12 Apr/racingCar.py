#Divyanshu Gupta
#SDEV 220
#Car racing game
#12th April 2022

from importlib import abc
from tkinter import *
from tkinter.ttk import *

from matplotlib.pyplot import fill
 
class window:
    def __init__(self, master = None):
        self.master = master
        self.master.title("Car Racing")
        
        self.temp=0
         
        # to take care movement in x direction
        self.x = 1
        # to take care movement in y direction
        self.y = 0
 
        # canvas object to create shape
        self.canvas = Canvas(master, width=600, height=100, bg="white")
        # creating rectangle
        self.trapezium = self.canvas.create_polygon(35,35,45,25,55,25,65,35, fill = "grey",tags=('move'))
        self.rectangle = self.canvas.create_rectangle(25,35,75,45, fill = "grey",tags=('move'))
        self.circle=self.canvas.create_oval(35,45,45,55,fill = "black",tags=('move'))
        self.circle1=self.canvas.create_oval(55,45,65,55,fill = "black",tags=('move'))
        self.canvas.pack()
 
        # calling class's movement method to
        # move the rectangle
        self.movement()
     
    def movement(self):
 
        # This is where the move() method is called
        # This moves the rectangle to x, y coordinates
        self.temp+=self.x
        
        if self.temp>600:
            self.canvas.move(('move'), -600, self.y)
            self.temp=0
        self.canvas.move(('move'), self.x, self.y)

        self.canvas.after(100, self.movement)
     
    # for motion in positive x direction
    def right(self, event):
        
        self.x += 5
        self.y = 0
    def left(self, event):
        
        self.x -= 2
        self.y = 0
 
if __name__ == "__main__":
 
    # object of class Tk, responsible for creating
    # a tkinter toplevel window
    master = Tk()
    w = window(master)
 
    # This will bind arrow keys to the tkinter
    # toplevel which will navigate the image or drawing
    master.bind("<KeyPress-Left>", lambda e: w.left(e))
    master.bind("<KeyPress-Right>", lambda e: w.right(e))
    
     
    # Infinite loop breaks only by interrupt
    mainloop()