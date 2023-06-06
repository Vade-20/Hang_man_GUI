from tkinter import *
from PyDictionary import PyDictionary
from random import choice
import json
from hangman_visual import visuals
from tkinter import messagebox

dictionary = PyDictionary()
with open('words.json', 'r',encoding='utf-8') as f:
    data = json.load(f)

root = Tk()
root.config(bg='black')
chances = 7
rand = None
l3 = None

def check(keys):
    char = str(keys)
    if not char.isalpha():
        messagebox.showerror('Error', 'Please enter an alphabet only')
    else:
        answer(char.lower())
    value.set('Select an Alphabet')

def check_key(keys):
    char = keys.char
    if not char.isalpha():
        messagebox.showerror('Error', 'Please enter an alphabet only')
    else:
        answer(char.lower())
    e1.delete(0, END)

def right_word(n=None):
    global rand, l3
    rand = choice(list(data)).lower()
    meaning = dictionary.meaning(rand, disable_errors=True)
    while meaning is None:
        rand = choice(list(data)).lower()
        meaning = dictionary.meaning(rand, disable_errors=True)
    ans = '__  ' * len(rand)
    l3 = Label(root, fg='red', bg='black', font=('Times', '20'), justify='center', text=ans, border=3, relief='raised')
    l3.grid(row=5, column=0, columnspan=6, sticky=W+E)
    for i, j in enumerate(meaning, start=6):
        t = Text(root, fg='red', bg='black', font=('Times', '15'), height=2, wrap='word')
        t.grid(row=i, column=0, columnspan=6, sticky=W+E)
        t.insert(END, f'{j} : {",".join(meaning[j])}')
        break

def new_game(n=None):
    global chances, b1_f1, l, value, l1_f1, l2_f2, l3_f1, e1
    chances = 7
    b1_f1.destroy()
    l.destroy()
    right_word()

    l2 = Label(root, text='Enter the guess -->', fg='red', bg='black', font=('Times', '20'), bd=3, relief='sunken')
    l2.grid(row=4, column=0, sticky=W+E)

    e1 = Entry(root, fg='red', bg='black', font=('Times', '20'), highlightthickness=2, highlightcolor='red',
               highlightbackground='red', justify='center')
    e1.grid(row=4, column=1, sticky=W+E)

    b1_f1 = Button(f1, text='New Game', fg='red', bg='black', width=20, relief='raised', font=('Times', '16'),
                   command=new_game)
    b1_f1.grid(row=0, column=1, sticky=E, columnspan=2)
    
    l1_f1 = Label(f1, text=f'You have {chances} chances left ', fg='red',
                  bg='black', font=('Times', '15'),)
    l1_f1.grid(row=0, column=0, sticky=W)
    
    l2_f2 = Text(f1, fg='red', wrap='word', height=7, bg='black', font=('Times', '20'))
    l2_f2.insert(END, f'{visuals[chances]}')
    l2_f2.grid(row=1, column=0, sticky=W+E, columnspan=2)
    
    l3_f1 = Text(f1, fg='red', wrap='word', bg='black', font=('Times', '15'), width=15, height=10)
    l3_f1.insert(END, 'Character already used:')
    l3_f1.grid(row=1, column=2, sticky=W)
    
    value = StringVar()
    value.set('Select an Alphabet')
    s1 = OptionMenu(root, value, *list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), command=check)
    s1.config(fg='red', font=('Times', '20'), relief='solid', bg="black", highlightthickness=2, highlightcolor='red',
              highlightbackground='red')
    s1['menu'].config(bg='black', fg='red')
    s1.grid(row=4, column=2)

def answer(n):
    global chances
    if n in rand:
        d = str(l3.cget('text')).split()
        for i, j in enumerate(rand):
            if j == n:
                d[i] = j.upper()
        d = '   '.join(d)
        l3.config(text=d)
    else:
        chances -= 1
        l1_f1.config(text=f'You have {chances} chances left ')
        l2_f2.delete('1.0', END)
        try:
            l2_f2.insert(END, f'{visuals[chances]}')
        except:
            new_game()
        v = l3_f1.get('1.0', END)
        l3_f1.delete('1.0', END)
        l3_f1.insert(END, f'{v} {n.upper()}')

    if chances == 0:
        l3.config(text=f'You lose!! The answer is - {rand}')

    if '__' not in l3.cget('text') and chances != 0:
        l3.config(text=f'You Win!! The answer is - {rand}')

l1 = Label(root, text='Hang-Man Game', fg='red', bg='black', padx=250, font=('Times', '40'), bd=3, relief='sunken')
l1.grid(row=0, column=0, columnspan=6)

f1 = Frame(root, bg='black')
f1.grid(row=1, column=0, columnspan=6, rowspan=3)

b1_f1 = Button(f1, text='Start Game', fg='red', bg='black', relief='raised', font=('Times', '30'), command=new_game)
b1_f1.grid(row=1, column=0, sticky=W+E, columnspan=2)

l = Label(f1, text='Note: This may take a few seconds to load', fg='red', bg='black', font=('Times', '15'))
l.grid(row=2, column=0, columnspan=6, sticky=W+E)

root.bind('<Key>', check_key)
root.bind('<Return>', new_game)
root.bind('<Escape>', lambda x: root.quit())
mainloop()