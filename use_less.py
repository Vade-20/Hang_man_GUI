import PyDictionary,random
from tqdm import tqdm
f = open('words.txt','r')
data = f.read()
data = eval(data)
d = PyDictionary.PyDictionary()
with open('words_.txt','w') as g:
    for i in tqdm(data):
        if d.meaning(i) is not None:
            g.write(i)
            g.write('\n')
        
    