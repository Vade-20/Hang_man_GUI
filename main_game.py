from random import choice
from tkinter import *
from PyDictionary import PyDictionary
from string import punctuation,ascii_uppercase
from hangman_visual import visuals

dictionary = PyDictionary()
with open('words.txt','r') as f:
    data = f.read()
    data = eval(data)
    

root = Tk()
root.config(bg='black')
chances = 7

def check(keys):
    char = str(keys)
    if char.isdigit() or char in punctuation:
        from tkinter import messagebox
        messagebox.showerror('Error','Please enter a alphabet only')
    else:
        answer(char)
    value.set('Select a Alphabet')
    
    
def check_key(keys):
    char = keys.char
    print(char)
    
def right_word(n=None):
    global rand,l3
    rand = choice(data).lower()
    meaning = dictionary.meaning(rand,disable_errors=True)
    if meaning is None:
        return right_word()
    else:
        ans = '__  '*len(rand)
        l3 = Label(root, fg='red',bg='black',font=('Times', '20'),justify='center',text=ans,border=3,relief='raised')
        l3.grid(row=5,column=0,columnspan=6,sticky=W+E)
        for i,j in enumerate(meaning,start=6):
            t = Text(root, fg='red',bg='black',font=('Times', '15'),height=2,wrap='word')
            t.grid(row=i,column=0,columnspan=6,sticky=W+E)
            t.insert(END,f'{j} : {",".join(meaning[j])}')
            break
            


def new_game():
    global chances,b1_f1,l,value,l1_f1,l2_f2,l3_f1
    chances = 7
    b1_f1.destroy()
    l.destroy()
    right_word()
    
    l2 = Label(root,text='Enter the guess -->',fg='red',bg='black', font=('Times', '20'),bd=3,relief='sunken')
    l2.grid(row=4,column=0,sticky=W+E)
    
    e1 = Entry(root, fg='red',bg='black',font=('Times', '20'),highlightthickness=2,highlightcolor='red',highlightbackground='red',justify='center')
    e1.grid(row=4,column=1,sticky=W+E)
    
    l1_f1 = Label(f1,text=f'You have {chances} chances left ',fg='red',
           bg='black',  font=('Times', '15'),)
    l1_f1.grid(row=0,column=0,sticky=W)
    l3_f1 = Text(f1,fg='red',wrap='word',bg='black',  font=('Times', '15'),width=10,height=10)
    l3_f1.insert(END,'Character already used:')
    l3_f1.grid(row=1,column=2,sticky=W)
    l2_f2 = Text(f1,fg='red',wrap='word',height=7,
           bg='black',  font=('Times', '20'),)
    l2_f2.insert(END,f'{visuals[chances]}')
    l2_f2.grid(row=1,column=0,sticky=W+E,columnspan=2)
    b1_f1 = Button(f1,text = 'New Game',fg='red',bg='black',width=20,relief='raised',font= ('Times', '16'),command=new_game)
    b1_f1.grid(row=0,column=1,sticky=E,columnspan=2)  

    value = StringVar()
    value.set('Select a Alphabet')
    s1 = OptionMenu(root,value,*[i for i in ascii_uppercase],command=check)
    s1.config(fg='red',  font=('Times', '20'),relief='solid',bg="black",highlightthickness=2,highlightcolor='red',highlightbackground='red',)
    s1['menu'].config(bg='black',fg='red')
    s1.grid(row=4,column=2)

def answer(n):
    global chances
    n = n.lower()
    if n in rand:
        d =str(l3.cget('text')).split()
        for i,j in enumerate(rand):
            if j==n:
                d[i]=j.upper()
        d = '   '.join(d)
        l3.config(text=d)
    else:
        chances = chances-1
        l1_f1.config(text=f'You have {chances} chances left ')
        l2_f2.delete('1.0','end')
        l2_f2.insert(END,f'{visuals[chances]}')
        v = l3_f1.get('1.0','end')
        l3_f1.delete('1.0','end')
        l3_f1.insert(END,f'{v} {n.upper()}')

    if chances==0:
        l3.config(text=f'You lose!! The aswer is {rand}')
        
    if '__' not  in l3.cget('text') and chances != 0:
        l3.config(text=f'You Win!! The answer is-{rand}')
    
l1 = Label(root,text='Hang-Man Game',fg='red',
           bg='black', padx=250, font=('Times', '40'),bd=3,relief='sunken')
l1.grid(row=0,column=0,columnspan=6)

f1 = Frame(root,bg='black')
f1.grid(row=1,column=0,columnspan=6,rowspan=3)
b1_f1 = Button(f1,text = 'Start Game',fg='red',bg='black',relief='raised',font= ('Times', '30'),command=new_game)
b1_f1.grid(row=1,column=0,sticky=W+E,columnspan=2)
l = Label(f1,text='Note this may take few second to load',fg='red',
           bg='black',font=('Times', '15'))
l.grid(row=2,column=0,columnspan=6,sticky=W+E)

mainloop()



