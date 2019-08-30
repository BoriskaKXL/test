import random
#минус кода - любая модель океана генерируется 5 раз, тк я не смог ршеить проблему сравнения текущей модели с предыдущей

L = ['fish', 'shmp', 'rock', 'none']

Ocean = []
Ocean1 = []
Ocean2 = []
# raw = random.randint(3, 20)
# col = random.randint(3, 20)


raw = 30
col = 30


def show(H):
    print('Океан')
    for i in range(len(H)):
        for j in range(len(H[i])):
            print(H[i][j], end=' ')
        print()


for i in range(raw):
    Ocean.append([])
    for j in range(col):
        Ocean[i].append(L[random.randint(0, 3)])

for i in range(raw):
    Ocean1.append([])
    for j in range(col):
        Ocean1[i].append([])

def lifeCheck(i, j, ob):
    if Ocean[i][j] == ob:
        n = 0
        if i + 1 != raw:
            if Ocean[i + 1][j] == ob:
                n += 1
                # print('Есть сосед на нижней строке')
        if i != 0:
            if Ocean[i - 1][j] == ob:
                n += 1
                # print('Есть сосед на верхней строке')
        if j + 1 != col:
            if Ocean[i][j + 1] == ob:
                n += 1
                # print('Есть сосед справа')
        if j != 0:
            if Ocean[i][j - 1] == ob:
                n += 1
                # print('Есть сосед слева')
        if (n == 4) or (n <= 1):
            Ocean1[i][j] = 'none'
        else:
            Ocean1[i][j] = ob


def rockCheck(i, j):
    if Ocean[i][j] == 'rock':
        Ocean1[i][j] = 'rock'


def noneCheck(i, j):
    if Ocean[i][j] == 'none':
        s = 0
        f = 0
        if i + 1 != raw:
            if Ocean[i + 1][j] == 'shmp':
                s += 1
        if i != 0:
            if Ocean[i - 1][j] == 'shmp':
                s += 1
        if j + 1 != col:
            if Ocean[i][j + 1] == 'shmp':
                s += 1
        if j != 0:
            if Ocean[i][j - 1] == 'shmp':
                s += 1
        if i + 1 != raw:
            if Ocean[i + 1][j] == 'fish':
                f += 1
        if i != 0:
            if Ocean[i - 1][j] == 'fish':
                f += 1
        if j + 1 != col:
            if Ocean[i][j + 1] == 'fish':
                f += 1
        if j != 0:
            if Ocean[i][j - 1] == 'fish':
                f += 1
        if s == 3:
            Ocean1[i][j] = 'shmp'
        if f == 3:
            Ocean1[i][j] = 'fish'
        else:
            Ocean1[i][j] = 'none'


def fullCheck():
    for i in range(raw):
        for j in range(col):
            lifeCheck(i, j, 'fish')
            lifeCheck(i, j, 'shmp')
            rockCheck(i, j)
            noneCheck(i, j)
    global Ocean
    global Ocean1
    global Ocean2
    Ocean2 = Ocean
    Ocean = Ocean1
    show(Ocean1)





show(Ocean)
for i in range(5):
    fullCheck()


