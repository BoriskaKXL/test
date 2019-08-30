#я не обернул модель в класс, это главный минус 
import re
#здесь данные считываются из одного файла, но не думаю, что это страшно
f = open('title.txt', 'r')
f = f.read()
f = f.replace('...', '.')
f = f.replace('.', ' .')
reg = re.compile('[^a-zA-Zа-яА-Я. \n]')
l = reg.sub('', f)
l = l.split()
for i in range(len(l)):
    l[i] = l[i].lower()

Dict = {}

for i in range(len(l) - 1):
    if l[i] not in Dict:
        Dict[l[i]] = list()
        Dict[l[i]].append(l[i + 1])
    else:
        if l[i + 1] not in Dict[l[i]]:
            Dict[l[i]].append(l[i + 1])

import random

firstWord = ''


def findFirst():
    global firstWord
    firstWord = l[(random.randint(0, len(l)))]
    if firstWord == '.':
        findFirst()


def nextWord(x):
    a = random.choice(Dict.get(x))
    global firstWord
    firstWord = a

findFirst()
D = ''
D += firstWord.capitalize() + ' '
u = open('new.txt', 'w')
b = 0
nextWord(firstWord)
c = 0
r = 0
p = random.randint(2000,4000)
for i in range(1, p):
    if b == 1:
        D += (' ' + firstWord.capitalize() + '')
        b = 0
    else:
        D += (firstWord + '')
    if firstWord == '.':
        b = 1
        firstWord = l[round(random.uniform(0, len(l)))]
        c+=1
        if c > 10:
            r = random.randint(0,1)
            if r == 1:
                D += '\n'
                c = 0
                r = 0
    else:
        D += (' ')
        nextWord(firstWord)


D += '.'
D = D.replace(' \n', '\n')
D = D.replace('\n.', '\n')
D = D.replace('\n. ', '\n')
D = D.replace('\n. ', '\n')
D = D.replace('\n ', '\n')
D = D.replace('..', '.')
D = D.replace('. .', '.')
D = D.replace(' . ', '. ')
D = D.replace(' .', '.')
u = open('new.txt', 'w')
u.write(D)
