#A CODE IS A UNIQUE 4 DIGIT 1 TO 6 COLOURS CODE
#1-BLUE 2-GREEN 3-YELLOW 4-WHITE 5-PINK 6-BLACK 
def elim(lst):
	return(list(set(list)))
print('WELCOME TO CODECRACKER GAME')
print('THE OBJECTIVE IS SIMPLE, FIND THE SECRET CODE IN UNDER 8 ATTEMPTS.')
print('INPUT 1 FOR SINGLER PLAYER OR 2 FOR MULTIPLAYER, ANYTHING ELSE QUITS THE GAME : ')
from random import randint
import sys
x = int(input(''))
if x == 1:
    print('YOU SELECTED TO PLAY VERSUS THE CPU,A RANDOM CODE HAS BEEN ADDED PLEASE MAKE YOUR FIRST ATTEMPT' )
    print('NOTE! 1 BLUE , 2  GREEN , 3  YELLOW , 4  WHITE , 5 PINK ,6 BLACK')
    codelist = [str(randint(1,6)) for i in range(1,5)]
    cod = "".join(codelist)
    print('\n'*100)
    for o in range (1,9):
        print('ATTEMPT' , o , )
        egw = str(input(''))
        while len(egw) != 4:
            print('ENTER ONLY 4 DIGITS ')
            print('ATTEMPT' , o , )
            egw = str(input(''))
            continue
        while  int(egw[0]) > 6 or int(egw[1])> 6 or int(egw[2])>6 or int(egw[3])>6:
            print('PLEASE ENTER DIGITS RAGNING FROM 1-6')
            print('ATTEMPT', o ,)
            egw=str(input(''))
            continue
        apotelesma = list()
        if egw == cod:
            print('SUCCESS WITH ', o , ' ATTEMPTS ')
            break
        for co in cod:
            for eg in egw:
                if cod[0] in egw:
                        if cod[0] == egw[0]:
                            apotelesma.append('o')
                        else:
                            apotelesma.append('x')
                if cod[1] in egw:
                        if cod[1] == egw[1]:
                            apotelesma.append('o')
                        else:
                            apotelesma.append('x')
                if cod[2] in egw:
                        if cod[2] == egw[2]:
                            apotelesma.append('o')
                        else:
                            apotelesma.append('x')
                if cod[3] in egw:
                        if cod[3] == egw[3]:
                            apotelesma.append('o')
                        else:
                            apotelesma.append('x')           
                if True :
                    result = "".join(apotelesma)
                    print(result)
                break
            break
elif x == 2:
    print('PLAYER 2 ENTER THE SECRET 4-DIGIT CODE.')
    print('YOU CAN USE ANY COMBINATION 4 NUMBERS IN [ 1, 2, 3, 4 ,5, 6] AS COLOURS.')
    print('NOTE! 1 BLUE , 2  GREEN , 3  YELLOW , 4  WHITE , 5 PINK ,6 BLACK') 
    code = str(input ('INPUT THE 4 DIGIT CODE(NOTE! PLAYER 2 SHALL NOT INTEND TO SEE THE CODE ):'))
    while len(code) != 4 :
        code =str(input('ENTER ONLY 4 DIGITS:'))
        continue
    while  int(code[0]) > 6 or int(code[1])> 6 or int(code[2])>6 or int(code[3])>6:
            print('PLEASE ENTER 4 DIGITS RAGNING FROM 1-6')
            code=str(input(''))
            continue
    cod = "".join(code)
    print('\n'*100)
    for o in range (1,9):
        print('ATTEMPT' , o , )
        egw = str(input(''))
        while len(egw) != 4 :
            print('ENTER ONLY 4 DIGITS ')
            print('ATTEMPT' , o , )
            egw=str(input(''))
            continue
        while  int(egw[0]) > 6 or int(egw[1])> 6 or int(egw[2])>6 or int(egw[3])>6:
            print('PLEASE ENTER DIGITS RAGNING FROM 1-6')
            print('ATTEMPT', o ,)
            egw=str(input(''))
            continue
        apotelesma=list()
        if egw == code:
            print('SUCCESS WITH ', o , ' ATTEMPTS')
            break
        if cod[0] in egw:
                if cod[0] == egw[0]:
                        apotelesma.append('o')
                        elim(egw)
                else:
                        apotelesma.append('x')
                        elim(egw)
        if cod[1] in egw:
                if cod[1] == egw[1]:
                        apotelesma.append('o')
                        elim(egw)
                else:
                        apotelesma.append('x')
                        elim(egw)
        if cod[2] in egw:
                if cod[2] == egw[2]:
                        apotelesma.append('o')
                        elim(egw)
                else:
                        apotelesma.append('x')
                        elim(egw)
        if cod[3] in egw:
                if cod[3] == egw[3]:
                        apotelesma.append('o')
                        elim(egw)
                else:
                        apotelesma.append('x')
                        elim(egw)
        if True :
                result = "".join(apotelesma)
                print(result)
else:
    sys.exit()
