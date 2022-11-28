#VASILEIOS KAPSALHS, A.M. 4080
#SUNARTHSH ELEXOU KWDIKOU STO MULTIPLAYER GIA TON PLAYER 1(secret code) XWRIS attempts- USED 1 TIME 
def elexosS(g):#xwris attempts
    while not g.isdigit():#pairnei alfarithmitiko
        print('You can only use 1, 2, 3, 4, 5, 6 as colors. Try again!')
        return False
    while len(list(g)) != 4:#error gia ta len,me listoula
        print('The secret code has exactly four colors. Try again! ')
        return False#akolouthei error me arithmous afou ginoun int kai dinei paromoio error me to prwto
    while  int(g[0]) > 6 or  int(g[1])> 6 or int(g[2])>6 or int(g[3])>6 or int(g[0]) <1 or int(g[1])<1 or int(g[2])<1 or int(g[3])< 1:
        print('You can only use 1, 2, 3, 4, 5, 6 as colors. Try again!')
        return False
    else:#an ola kala dinei true kai spaei thn while sto telos
        return True
#ELEGXOS GIA TH PROSPATHEIA TOU PLAYER 1 STO MULTIPLAYER KAI THN PROSPATHEIA PLAYER 2 STO SINGLEPLAYER - USED 2 TIMES
def elexos(g):#idia me thn panw mono p exei kai ta attempts wste na ta ypenthmizei ston xrhsth
    while not g.isdigit():
        print('You can only use 1, 2, 3, 4, 5, 6 as colors. Try again!')
        print('ATTEMPT', o ,)
        return False
    g=str(g)
    while len(list(g)) != 4: #elegxos me attempts na epanalamvaontai kai na upenthimizontai
        print('The secret code has exactly four colors. Try again! ')
        print('ATTEMPT' , o , )
        return False #gia thn loop while akolouthei elegxos aritmwn
    while  int(g[0]) > 6 or int(g[1])> 6 or int(g[2])>6 or int(g[3])>6 or int(g[0]) <1 or int(g[1])<1 or int(g[2])<1 or int(g[3])< 1:
        print('You can only use 1, 2, 3, 4, 5, 6 as colors. Try again!')
        print('ATTEMPT', o ,)
        return False
    else:
        return True
#SUNARTHSH GIA NA VRW TA IDIA KAI OMOIA DHLAD TA 'O' USED 1-8 TIMES
def kappa(eg,cod,l3):#elegxos kwdikwn - idia stoixeia pairnoun 0
            if eg[0]==cod[0]:
                l3.append('o')#aplo append den m noiazei pou tha bei sto telos 
            if eg[1]==cod[1]:
                l3.append('o')
            if eg[2]==cod[2]:
                l3.append('o')
            if eg[3]==cod[3]:
                l3.append('o')
            else:
                return
#SUNARTHSH GIA NA VALW TA X - USED 1-8 TIMES
def keppo(eg,cod,l2):#afou teleiwsoun ta idia me 'o' 3ekiname na diwxnoumw ta anstistoixa idia
    codee=list(cod)#dinoume allh lista gia n mhn alla3ei ton krufo e3w apo thn snarthsh
    if eg[1]==codee[1]:#kai pop kai insert wste na mhn alla3ei to len an kai den to 
            codee.pop(1)#xreiazomai telika to insert giati na to riskarw afou doulevei
            codee.insert(1,11)
            eg.pop(1)
            eg.insert(1,12)
    if eg[0]==codee[0]:
            codee.pop(0)
            codee.insert(0,11)
            eg.pop(0)
            eg.insert(0,12)
    if eg[2]==codee[2]:
            codee.pop(2)
            codee.insert(2,11)
            eg.pop(2)
            eg.insert(2,12) 
    if eg[3]==codee[3]:
            codee.pop(3)
            codee.insert(3,11)
            eg.pop(3)
            eg.insert(3,12) 
    codee=list(set(codee))#twra menoun ta dipla pou borei na mhn eixan tuxei na pesoun idia stous dio kwdikus
    eg=list(set(eg))#boroun na boun mia fora opote ta kanoume set alliws tha eixame provlhma me ta x
    if len(code)>=len(eg):#duo periptwseis gia ta len twn kwdikwn meta to set giati allazoun ta len tous
        for i in range(len(codee)):#se kathe len VAZW KAI TO ANTISTOIXO CODE h diko m kwdiko gia na mhn vgei
            if codee[i] in eg:#se sfalma to in range 
                l2.append('x')
    if len(code)<len(eg):
        for i in range(len(eg)):
            if eg[i] in codee:
                l2.append('x')
    else:
        return
#ARXH PROGRAMMATOS - TELOS SYNARTHSEWN
o=1#global
apotelesma=list()#lista apotelesmatwn pou tha prosthethon oi alles 2 listes
from random import randint#gia ton player 1 apo odhgies
print('CODECRACKER GAME! The objective is to guess the secret code in as few attempts as possible.Input 1 for 1player game or 2 for 2player game:')
x = int(input(''))#input gia to programma
if x == 1:#player1
    code = [str(randint(1,6)) for i in range(1,5)]#ftiaxnei 4 4hfio me arithmous apo 1-6
    code = "".join(code)#axrhsto nmz
    while o<=8:#WHILE GIA TA ATTEMPTS ME THN 0=1
        print('ATTEMPT' , o , )#attempts mesa sthn while me to o san metavlhth p allazei 
        egw = input('')#O DIKOS M KWDIKOS STHN SUNARTHSH EINAI EG,EGWW
        while True:#ELEXGOS ME ATTEMPTS EISAGWGHS KWDIKOU
            if elexos(egw)==True:#an dwsei truw san timh me to return proxwrame 
                break
            else:
               egw=input('ENTER NEW CODE:')
        egw=list(egw)
        if egw == code:
            print('SUCCESS with ', o , 'attempts. PLAYER 1 WINS')
            break
        else:
            apotelesma=list()#APOTELSMA TWN  O,X MESA STHN LOOPA GIA NA MHN THN ORIZEI PANTA
            li=list()#LISTA ME  X MESA STHN LOOPA GIA NA MHN THN ORIZEI PANTA
            le=list()#LISTA ME o MESA STHN LOOPA GIA NA MHN THN ORIZEI PANTA
            code=list(code)#LISTA GIA N BEI SE SUNARTHSH ME LEN
            kappa(egw,code,li)#sunarthsh twn o
            keppo(egw,code,le)#sunarthsh twn x 
            apotelesma=li+le#me opoia prosthesw tis listes etsi the vgoun kai me seira ta oox h alliws xoo
            apotelesma=''.join(apotelesma)
            print(apotelesma)
            del[apotelesma]#katharizei lista
            del[le]#katharizei lista
            del[li]#katharizei lista
            o+=1#kinei ta attampts
    else:#an teleiwsei to while erxomaste edw
        print('YOU RUN OUT OF ATTEMPTS.CPU WINS.SECRET CODE WAS',code)
elif x == 2:
    print('PLAYER1-INPUT THE 4 DIGIT CODE(NOTE! PLAYER 2 SHALL NOT INTEND TO SEE THE CODE')
    code = input('')
    while True:#elegxei to input tou player1
            if elexosS(code)==True:#an i synarthsh dwsei true sunexizei
                break
            else:#an i synarthsh dwsei  dwsei kati allo 3anazhtaei kwdiko
                code=input('ENTER NEW CODE:')
    code=list(code)
    code=''.join(code)
    print('\n'*100)
    while o<=8:
        print('ATTEMPT' , o , )
        egw = input('')
        while True:#ELEGXOS ME ATTEMPTS PRIN TO PROGRAMMA
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
            kappa(egw,code,le)#sunarthsh o
            keppo(egw,code,li)#sunarthsh x
            apotelesma=le+li#duo sunarthseis kai 2 listes dinoun mia gia na exw o,x me seira xwrismena meta3u toys
            apotelesma=''.join(apotelesma)#apo list srt
            print(apotelesma)
            del[apotelesma]#katharizei lista gia na 3anaxrhsimopoithei
            del[li]#katharizei lista    gia na 3anaxrhsimopoithei
            del[le]#katharizei lista    gia na 3anaxrhsimopoithei
            o+=1#kinei ta attampts
    else:#an teleisei to while erxomaste edw
        print('player 2 : YOU RUN OUT OF ATTEMPTS! PLAYER 1 IS THE WINNER !')#an teleisei ta attempts
else:
    print('try again')#este oti bei kati katalathos na mhn peta3ei error apo to pouthena
