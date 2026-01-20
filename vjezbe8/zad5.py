import numpy as np
import matplotlib.pyplot as plt
#konstante
L=1
a=0.005
deltat=0.01
deltax=0.01
konstanta=(deltat/(deltax)**2)*a

#početni uvjet
def f(x):
    return np.exp(-400*((x-0.3)**2))
početni=[0 for i in np.arange(0,L+deltax,deltax)]
for i in range(1,len(početni)):
    početni[i]=f(i*0.01)
početni[-1]=0
x=[i*deltax for i in range (0,len(početni))]
plt.plot(x,početni,label="t=0s")
def wave(initial,constant,n):
    rjesenje_prijasnje=initial
    rjesenje=initial
    for j in range(1,n+1):
        rjesenje_j=[0 for i in range(0,len(initial))]
        for i in range(1,len(initial)-1):
            rjesenje_j[i]=constant*rjesenje[i+1]+2*(1-constant)*rjesenje[i]+constant*rjesenje[i-1]-rjesenje_prijasnje[i]
        rjesenje_prijasnje=rjesenje
        rjesenje=rjesenje_j
        if j in [5,10,20]:
            print(rjesenje)
            plt.plot(x,rjesenje,label="t={}s".format(round(j*deltat)))
    plt.legend()
    plt.show()
wave(početni,konstanta,20)