#SUNARTHSH ELEGXWN TWN KWDIKWN TOU SINGLE PLAYER KAI PARALLHLA ELEGXOS TOU KOUDIKOU TOU PLAYER 2 STO MULTIPLAYER
def elexos(g):
    while not g.isdigit():
        print('ENTER DIGIT ONLY')
        print('ATTEMPT',o,)
        return False
    while len(g) !=4:
        print('PLEASE ENTER ONLY FOUR DIGITS  ')
        print('ATTEMPT' , o , )
        return False
    while  int(g[0]) > 6 or int(g[1])> 6 or int(g[2])>6 or int(g[3])>6 or int(g[0]) <1 or int(g[1])<1 or int(g[2])<1 or int(g[3])< 1:
        print('ENTER DIGITS RAGNING FROM (1-6)')
        print('ATTEMPT', o ,)
        return False
    else:
        return True
def kappa(c):
    cod=code
    eg=egw
    apotel=[]
    for i in range(len(eg)):
        if eg[i]==cod[i]:
            apotel.append('o')
            print(apotel,end='')
def lamda(u):
    cod=code
    eg=egw
    apotel2=[]
    for i in range(len(eg)):
        if eg[i]==cod[i]:
            code[i]='12'
    g=list(set(eg))
    for j in range(len(g)):
        if g[j] in cod:
            apotel2.append('x')
            print(apotel2,end='')
        
        
o=1
from random import randint
print('star')
x = int(input(''))
if x == 1:
    code = [str(randint(1,6)) for i in range(1,5)]
    code = "".join(code)
    while o<=8:
        print('ATTEMPT' , o , )
        egw = str(input(''))
        while True:
            if elexos(egw)==True:
                break
            else:
                egw=input('ENTER NEW CODE:')
        apotelesma=list()
        egw=list(egw)
        code=list(code)
        if egw == code:
            print('SUCCESS with ', o , 'attempts. PLAYER 1 WINS')
            break
        else:
            kappa(o)
            o+=1
    if o>8:
        print('YOU RUN OUT OF ATTEMPTS.CPU WINS')
    else:
        print('YOU RUN OUT OF ATTEMPTS.CPU WINS')
elif x == 2:
    code = str(input ('INPUT THE 4 DIGIT CODE(NOTE! PLAYER 2 SHALL NOT INTEND TO SEE THE CODE ):'))
    code=''.join(code)
    print('\n'*100)
    print(code)
    while o<=8:
        code=list(code)
        print('ATTEMPT' , o , )
        egw = str(input(''))
        while True:
            if elexos(egw)==True:
                break
            else:
                egw=input('ENTER NEW CODE:')
        apotelesma=list()
        egw=list(egw)
        if egw == code:
            print('SUCCESS with ', o , 'attempts . PLAYER 2 WINS')
            break
        else:
            kappa(o)
            lamda(o)
            o+=1
    if o>8:
        print('player 2 : YOU RUN OUT OF ATTEMPTS! PLAYER 1 IS THE WINNER !')
    else:
        print('player 2 : YOU RUN OUT OF ATTEMPTS! PLAYER 1 IS THE WINNER !')
else:
    print('try again')

