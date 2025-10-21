import numpy as np
def y1(t,y01=5,A=1,B=3):
    y1=y01+A*np.cos(B*t)
    return y1
def y2(t,y02=0.325,C=2,D=0.5):
    y2=y02+C*np.exp(D*t)
    return y2
def y3(t):
    return y1(t)-y2(t)
def y4(t):
    return 7*t**2+15*t-32
def method_bisection(f,min,max,epsilon):
    if f(min)*f(max)<0:
        a=min
        b=max
        while abs(a-b)>epsilon:
            bisect=(a+b)/2
            if f(a)*f(bisect)<0:
                a=a
                b=bisect
            else:
                a=bisect
                b=b
        return bisect, abs(f(bisect))
    else:
        return "Funkcija ima iste znakove na oba kraja intervala te je druga metoda potrebna."
def method_newtonraphson(f,x0,h,epsilon):
    xn=x0
    while abs(f(xn))>epsilon:
        derivacija=(f(xn+h)-f(xn-h))/(2*h)
        xn=xn-f(xn)/derivacija
    return xn, abs(f(xn))
   
print(method_bisection(y3,0,3,0.0000001))
print(method_bisection(y3,3,6,0.0000001))
print(method_bisection(y3,1,2.5,0.0000001))
print(method_bisection(y3,0,4,0.0000001))	
#ovisno o tome gdje stavimo interval, to će metoda bisekcije brže ili sporije konvergirati, ali će uvijek konvergirati ako su znakovi funkcije različiti na krajevima intervala
#što je aritmetička sredina krajeva intervala bliža pravom korijenu, to će metoda brže konvergirati
#smanjujući epsilon povećava se preciznost, ali povećava broj koraka
print(method_newtonraphson(y3,2,0.000001,0.0000001))
print(method_newtonraphson(y3,4,0.000001,0.0000001))
#ovisno o tome gdje stavimo početnu točku, to će metoda Newton-Raphson brže ili sporije konvergirati, ali neće uvijek konvergirati ako je početna točka daleko od pravog korijena
#što je početna točka bliža pravom korijenu, to će metoda brže konvergirati
#smanjujući epsilon povećava se preciznost, ali povećava broj koraka