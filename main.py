from tkinter import *
from random import *
root = Tk()

root.title("PASS CREATOR")
root.geometry('250x200')

top_lbl = Label(root,text = "PASSWORD GENERATOR" )
top_lbl.place(x = 60)

def hello():
    PASS = "C=Dbc^*NOPQa9:0AB&de+f@g-hiq_HIw)xyz1(2opR*ST3&4M!#$XY&JKL^r56EFG$jk#lm@n7U!V8WstZ"    
    i=0
    password = []
    while i<8:
    	password.append( PASS[ randint(0,55) ] )
    	i += 1
        
    pass_lbl = Label(root, text=password )
    pass_lbl.place(x = 80,y = 150)    

button = Button(root, text = "Create", width = 10, height = 5, bg="yellow", command=hello)
button.place(x = 80,y = 40)

root.mainloop()
