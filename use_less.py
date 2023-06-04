f = open('words.txt','r')
data = f.read()
data = eval(data)
import string 
data = {i:len(i) for i in data}

for i in data:
    for j in i:
     if j.isdigit() or j in string.punctuation:
        print(i) 


