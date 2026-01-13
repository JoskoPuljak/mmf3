import numpy as np
import matplotlib.pyplot as plt
a=0.01
deltax=0.2
L=20
deltat=0.5
konstanta=(deltat/(deltax)**2)*a

end=int(round(L/deltax))
print(end)
početni=[0 for i in range(0,end+1)]
for i in range(2*2,5*2):
    početni[i]=5.5
x=[0.2*i for i in range (0,len(početni))]
plt.plot(x,početni)
print(početni)
def diffusion(initial,constant,n):
    rjesenje=initial
    for j in range(1,n+1):
        rjesenje_j=[0 for i in range(0,len(initial))]
        for i in range(1,len(initial)-1):
            rjesenje_j[i]=constant*rjesenje[i+1]+(1-2*constant)*rjesenje[i]+constant*rjesenje[i-1]
        rjesenje=rjesenje_j
        if j in [100,200,300,400]:
            print(rjesenje)
            plt.plot(x,rjesenje)
    plt.show()
diffusion(početni,konstanta,400)
