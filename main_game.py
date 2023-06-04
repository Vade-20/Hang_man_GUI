from random import choice
from tkinter import *
from PyDictionary import PyDictionary
from string import punctuation,ascii_uppercase

dictionary = PyDictionary()
with open('words.txt','r') as f:
    data = f.read()
    data = eval(data)
    

root = Tk()
root.config(bg='black')


def check(keys):
    char = str(keys.char)
    if char.isdigit() or char in punctuation:
        from tkinter import messagebox
        messagebox.showerror('Error','Please enter a alphabet only')
    else:
        pass

def right_word(n):
    pass

    
l1 = Label(root,text='Hang-Man Game',fg='red',
           bg='black', padx=250, font=('Comic Sans MS', '40'),bd=3,relief='sunken')
l1.grid(row=0,column=0,columnspan=6)
l2 = Label(root,text='Enter the guess-',fg='red',bg='black', font=('Comic Sans MS', '20'),
               )
l2.grid(row=4,column=0)

e1 = Entry(root, fg='gold',bg='light sky blue',font=('Comic Sans MS', '20'), width=5, borderwidth=2)
e1.grid(row=4,column=1)

value = StringVar()
value.set('Select a Alphabet')
s1 = OptionMenu(root,value,*[i for i in ascii_uppercase])
f1 = Frame(root,bg='light grey')
f1.grid(row=1,column=0,columnspan=6,rowspan=3)
l1_f1 = Label(f1,text='Game',fg='red',
           bg='black',  font=('Comic Sans MS', '40'),)
l1_f1.pack()



mainloop()



