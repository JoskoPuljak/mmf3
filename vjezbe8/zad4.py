import numpy as np
import matplotlib.pyplot as plt
import thomas as th
#konstante
a=0.01
deltax=0.2
L=20
deltat=0.5
konstanta=(deltat/(deltax)**2)*a
end=int(round(L/deltax))
#početni uvjet
početni=[0 for i in range(0,end+1)]
for i in range(2*int(1//deltax),5*int(1//deltax)):
    početni[i]=5.5
x=[i*deltax for i in range (0,len(početni))]

#rjesavanje jednadzbe i plottanje
def CrankNicolson(initial,constant,n):
    plt.plot(x,initial,label="t=0s")
    #matrica koeficijenata
    size=len(initial)-2
    B=np.zeros((size,size))
    #prvi red
    B[0][0]=2
    B[0][1]=-1
    #i-ti red
    for i in range(1,size-1):
        B[i][i-1]=-1
        B[i][i]=2
        B[i][i+1]=-1
    #zadnji red
    B[-1][-2]=-1
    B[-1][-1]=2
   
    #eksplicitni dio
    B_2=(2*np.eye(size)-constant*B)
    for j in range(1,n+1):
        #desna strana
        initial_np=np.transpose([initial[1:-1]])
        desna_strana=np.dot(B_2,initial_np)
        #lijeva strana
        B_3=constant*B+(2*np.eye(size))
        #rjesavanje sustava
        rjesenje=np.linalg.solve(B_3,desna_strana)
        #priprema za sljedeći korak
        initial= [0]+[rjesenje[i][0] for i in range(len(rjesenje))]+[0]
        if j in [100,200,300,400]:
            plt.plot(x,initial,label="t={}s".format(round(j*deltat)))
    plt.title("Crank-Nicolson metoda")
    plt.legend()
    plt.show()
CrankNicolson(početni,konstanta,400)