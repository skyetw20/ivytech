#Divyanshu Gupta
#SDEV 220
#Create a game similar to hangman
#17th May 2022

import random #importing random library
from tkinter import * #importing tkinter library
from tkinter import messagebox #importing message box for showing messages 

class GUI: #class to create gui and handle the operations
    def __init__(self):
        try: #try and except block to handle the directory presence of the words.txt file
            with open('words.txt') as file: #opening the file and reading it's data to a tuple 
                lines = file.readlines()
                lines = [line.rstrip() for line in lines]
            self.WORDS=tuple(lines)
        except: #except block to manually assign the words tuple
            self.WORDS=('bottom','bought','branch','breath','bridge','bright','broken','budget','burden','bureau','button','camera','cancer','cannot','carbon','animal','little','market','silent','ticket','yellow','speech','salary','remote','patent','minute','member','leader','driver')

        self.missed_letters = []#list for keeping the record of missed letters
        self.word = self.WORDS[random.randint(0, len(self.WORDS) - 1)]
        self.str = list('*' * len(self.word))

        window = Tk()#initialising the window 
        self.cnvs = Canvas(window, width=600, height=500)#initialising the canvas with width and height
        self.cnvs.pack()
        self.create_scene()

        self.cnvs.bind('<Key>', self.handle_input)
        self.cnvs.bind('<Return>', self.replay)
        self.cnvs.focus_set()

        window.mainloop()# mainloop for running continuously the loop

    def handle_input(self, event):#function to handle the input form the user
        if event.char in self.word:#checking for the letter in word input by the user 
            self.cnvs.delete('txt')
            for i in range(len(self.word)):
                if self.word[i] == event.char:
                    self.str[i] = self.word[i]

                self.cnvs.delete('txt')
                txt = "Guess a word: " + "".join(self.str)
                self.cnvs.create_text(280, 380, text=txt, tag='txt')
        else:
            self.cnvs.delete('wrong')
            self.create_home(len(self.missed_letters))
            self.missed_letters.append(event.char)
            txt = "Missed letters: " + "".join(self.missed_letters)

        if "".join(self.str) == self.word or len(self.missed_letters)>6 :
            self.cnvs.delete('txt')
            self.cnvs.delete('wrong')
            txt = "The word is: " + "".join(self.word)
            self.cnvs.create_text(280, 380, text=txt, tag='txt')
            
            self.cnvs.create_text(280, 420, text='To continue the game press ENTER', tag='txt')

    def create_home(self, i):#fucntion to handle the creation of the home
        if i == 0:
            self.cnvs.create_line(114, 150, 114, 294, tag='home',width=5)#creating the lines usign the coordinates on the canvas  
            self.cnvs.create_line(114, 291, 487, 291, tag='home',width=5)#creating the lines usign the coordinates on the canvas
            self.cnvs.create_line(487, 294, 487, 150, tag='home',width=5)#creating the lines usign the coordinates on the canvas
        elif i == 1:
            self.cnvs.create_rectangle(276,80,325,100,tag='home',fill='red')
        elif i == 2:
            self.cnvs.create_rectangle(375,150,437,220,tag='home',fill='red')
        elif i == 3:
            self.cnvs.create_rectangle(164,150,226,220,tag='home',fill='red')
        elif i == 4:
            self.cnvs.create_line(293,10, 541,200, tag='home',width=15)
        elif i == 5:
            self.cnvs.create_line(300, 10, 60,200,width=15, tag='home')
            
        else:
            self.cnvs.create_rectangle(276,191,325,291,tag='home',fill='red')
            self.cnvs.create_oval(276,236,286,246,tag='home',fill='blue')

    def create_scene(self):#method to initialise the scene on the canvas
        
        txt = "Guess a word: " + ('*' * len(self.word))
        self.cnvs.create_text(280, 380, text=txt, tag='txt')

    def replay(self, event):#method for displaying the result
        
        self.cnvs.delete('home')
        self.cnvs.delete('txt')
        self.word = self.WORDS[random.randint(0, len(self.WORDS) - 1)]
        self.str = list('*' * len(self.word))
        txt = "Guess a word: " + ('*' * len(self.word))
        self.cnvs.create_text(280, 380, text=txt, tag='txt')
        self.missed_letters = []
GUI()#creating the instance of the class GUI