#VASILEIOS KAPSALIS, AM 4080
#SUNARTHSH ELEXOU KWDIKOU STO MULTIPLAYER GIA TON PLAYER 1(secret code) xwris attempts
def elexosS(g):
    while len(g) !=4:
        print('The secret code has exactly four colors. Try again! ')
        return False
    while  int(g[0]) > 6 or not g.isdigit() or  int(g[1])> 6 or int(g[2])>6 or int(g[3])>6 or int(g[0]) <1 or int(g[1])<1 or int(g[2])<1 or int(g[3])< 1:

        print('You can only use 1, 2, 3, 4, 5, 6 as colors. Try again!')
        return False
    else:

        return True
def elexos(g):#ELEGXOS GIA TH PROSPATHEIA TOU PLAYER 1 STO MULTIPLAYER KAI THN PROSPATHEIA PLAYER 2 STO SINGLEPLAYER
    while len(g) !=4:
        print('The secret code has exactly four colors. Try again! ')
        print('ATTEMPT' , o , )
        return False
    while  int(g[0]) > 6 or not g.isdigit() or int(g[1])> 6 or int(g[2])>6 or int(g[3])>6 or int(g[0]) <1 or int(g[1])<1 or int(g[2])<1 or int(g[3])< 1:
        print('You can only use 1, 2, 3, 4, 5, 6 as colors. Try again!')
        print('ATTEMPT', o ,)
        return False
    else:
        return True
def kappa(eg,cod,l3):#elegxos kwdikwn - idia stoixeia pairnoun 0
            if eg[0]==cod[0]:
                l3.append('o')
            if eg[1]==cod[1]:
                l3.append('o')
            if eg[2]==cod[2]:
                l3.append('o')
            if eg[3]==cod[3]:
                l3.append('o')
            else:
                return
def keppo(eg,cod,l2):#apofugh idiwn stoixiwn an perasei o elegxos gia ta x 
    codee=list(cod)#nea lista gia n mhn peria3ei ton krufo
    if eg[1]==codee[1]:
            codee.pop(1)
            codee.insert(1,11)
    if eg[0]==codee[0]:
            codee.pop(0)
            codee.insert(0,11)
    if eg[2]==codee[2]:
            codee.pop(2)
            codee.insert(2,11)
    if eg[3]==codee[3]:
            codee.pop(3)
            codee.insert(3,11) 
    eg=list(set(eg))#diwxnei ta dipla apo to dwthenta kwdiko
    for i in range(len(codee)):
        if codee[i] in eg:
            l2.append('x')
    else:
        return
o=1#global
apotelesma=list()
from random import randint
print('CODECRACKER GAME! The objective is to guess the secret code in as few attempts as possible.Input 1 for 1player game or 2 for 2player game:')
x = int(input(''))
if x == 1:
    code = [str(randint(1,6)) for i in range(1,5)]
    code = "".join(code)
    apotelesma=list()
    li=list()
    le=list()
    code=list(code)
    print(code)
    while o<=8:
        print('ATTEMPT' , o , )
        egw = str(input(''))
        li=list()
        le=list()
        code=list(code)
        while True:
            if elexos(egw)==True:
                break
            else:
               egw=input('ENTER NEW CODE:')
        egw=list(egw)
        if egw == code:
            print('SUCCESS with ', o , 'attempts. PLAYER 1 WINS')
            break
        else:
            kappa(egw,code,li)
            keppo(egw,code,le)
            apotelesma=le+li
            apotelesma=''.join(apotelesma)
            print(apotelesma)
            del[apotelesma]
            del[le]
            del[li]
            o+=1
    else:
        print('YOU RUN OUT OF ATTEMPTS.CPU WINS')
elif x == 2:
    code = str(input (' PLAYER1-INPUT THE 4 DIGIT CODE(NOTE! PLAYER 2 SHALL NOT INTEND TO SEE THE CODE ):'))
    while True:
            if elexosS(code)==True:
                break
            else:
               code=input('ENTER NEW CODE:')
    code=''.join(code)
    print('\n'*100)
    while o<=8:
        print('ATTEMPT' , o , )
        egw = str(input(''))
        while True:
            if elexos(egw)==True:
                break
            else:
                egw=input('ENTER NEW CODE:')
        egw=list(egw)
        code=list(code)
        apotelesma=list() 
        li=list()
        le=list()
        if egw == code:
            print('SUCCESS with ', o , 'attempts . PLAYER 2 WINS')
            break
        else:
            kappa(egw,code,le)
            keppo(egw,code,li)
            apotelesma=li+le
            apotelesma=''.join(apotelesma)
            print(apotelesma)
            del[apotelesma]
            del[li]
            del[le]
            o+=1
    else:
        print('player 2 : YOU RUN OUT OF ATTEMPTS! PLAYER 1 IS THE WINNER !')
else:
    print('try again')
