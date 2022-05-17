#Divyanshu Gupta
#SDEV 220
#Geometric figures outlined and filled
#12th April 2022

from tkinter import *  #importing library


#creating a class for the canvas
class Canvas1(Frame):

    def __init__(self):
        
        Frame.__init__(self)
        self.master.title("Radiobuttons and Checkbuttons") #initialising the title for the window
        self.grid()

        
        self.canvas = Canvas(self, width=600, height=500, bg="white") #setting dimensions of the window
        self.canvas.grid(row=0, column=0)

        
        frame = Frame(self)    #creating frame
        frame.grid(row=1, column=0)
       #intialising buttons and taking input from buttons
        self.radioChoice = IntVar()
        self.radioChoice.set(0) 
        rectangle = Radiobutton(frame, text="Triangle",variable=self.radioChoice,value=1, command=self.displayTriangle)
        oval = Radiobutton(frame, text="Diamond",variable=self.radioChoice,value=2, command=self.displayDiamond)
        self.filledVar=IntVar()
        self.filledVar.set(0)
        filled = Checkbutton(frame, text="Filled", command=self.displayFilled, variable=self.filledVar)
        clear = Button(frame, text="Clear", command=self.clearCanvas)
        #placing buttons on the frame
        rectangle.grid(row=0, column=0)
        oval.grid(row=0, column=1)
        filled.grid(row=0, column=2)
        clear.grid(row=0, column=3)

    def displayTriangle(self):
        self.canvas.delete('all')
        self.canvas.create_polygon(50,50,530,50,280,450,fill='white',outline='black')
        self.displayFilled()

    def displayDiamond(self):
        self.canvas.delete('all')
        self.canvas.create_polygon(80,120,160,40,480,40,560,120,320,440,fill='white',outline='black')
        self.displayFilled()

    def displayFilled(self):
        
        if self.filledVar.get()==1:
            
            if self.radioChoice.get()==1:
                self.canvas.create_polygon(50,50,530,50,280,450,fill='red',outline='black')
            
            if self.radioChoice.get()==2:
                self.canvas.create_polygon(80,120,160,40,480,40,560,120,320,440,fill='red',outline='black')
        else:
            self.canvas.delete("filled")

    def clearCanvas(self):
        self.canvas.delete('all')
        self.radioChoice.set(0)
        self.filledVar.set(0)


def main():
    Canvas1().mainloop()


main()