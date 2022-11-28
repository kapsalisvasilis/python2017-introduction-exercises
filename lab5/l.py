x=float(input('please enter the amount of cash : '))
a=x // 500
if a > 0:
    print(a,'* 500$')
    x=x-a*500
    x=round(x,2)
b=x // 200
if b > 0:
    print(b,'* 200$')
    x=x-b*200
    x=round(x,2)
c=x // 100
if c > 0:
    print(c,'* 100$')
    x=x-c*100
    x=round(x,2)
d=x // 50
if d > 0:
    print(d,'* 50$')
    x=x-d*50
    x=round(x,2)
e=x // 20
if e > 0:
    print(e,'* 20$')
    x=x-e*20
    x=round(x,2)
f=x // 10
if f > 0:
    print(f,'* 10$')
    x=x-f*10
    x=round(x,2)
g=x // 5
if g > 0:
    print(g,'* 5$')
    x=x-g*5
    x=round(x,2)
h=x // 2
if h > 0:
    print(h,'* 2$')
    x=x-h*2
    x=round(x,2)
i=x // 1
if i > 0:
    print(i,'* 1$')
    x=x-i*1
    x=round(x,2)
j=x // 0.5
if j > 0:
    print(j,'* 0.5$')
    x=x-j*0.5
    x=round(x,2)
k=x // 0.2
if k > 0:
    print(k,'* 0.2$')
    x=x-k*0.2
    x=round(x,2)
l=x // 0.1
if l > 0:
    print(l,'* 0.1$')
    x=x-l*0.1
    x=round(x,2)
m=x // 0.05
if m > 0:
    print(m,'* 0.05$')
    x=x-m*0.05
    x=round(x,2)
n=x // 0.02
if n > 0:
    print(n,'* 0.02$')
    x=x-n*0.02
    x=round(x,2)
o= x // 0.01
if o > 0:
    print(o,'* 0.01$')
    x=x-o*0.01
    x=round(x,2)
