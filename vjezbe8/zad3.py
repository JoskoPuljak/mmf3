import numpy as np
import matplotlib.pyplot as plt
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
plt.plot(x,početni,label="t=0")


#rjesavanje jednadzbe i plottanje
def diffusion(initial,constant,n):
    rjesenje=initial
    for j in range(1,n+1):
        rjesenje_j=[0 for i in range(0,len(initial))]
        for i in range(1,len(initial)-1):
            rjesenje_j[i]=constant*rjesenje[i+1]+(1-2*constant)*rjesenje[i]+constant*rjesenje[i-1]
        rjesenje=rjesenje_j
        if j in [100,200,300,400]:
            #print(rjesenje)
            plt.plot(x,rjesenje,label="t={}s".format(round(j*deltat)))
    plt.title("Eksplicitno rješenje")
    plt.legend()
    plt.show()
diffusion(početni,konstanta,400)

#implicitna forma
def thomasalgortihm(array):
    array1=np.array(array)
    size=array1.shape
    array2=np.zeros(size)
    rjesenje1=np.zeros((size[0],1))
    rjesenje=np.zeros((size[0],1))
    #prvi red
    c1=array1[0][1]/array1[0][0]
    d1=array1[0][size[1]-1]/array1[0][0]
    array2[0][0]=1
    array2[0][1]=c1
    rjesenje1[0][0]=d1
    #i-ti red
    for i in range(2,size[0]):
        array2[i-1][i-1]=1
        array2[i-1][i]=array1[i-1][i]/(array1[i-1][i-1]-array1[i-1][i-2]*array2[i-2][i-1])
        rjesenje1[i-1][0]=(array1[i-1][size[1]-1]-array1[i-1][i-2]*rjesenje1[i-2][0])/(array1[i-1][i-1]-array1[i-1][i-2]*array2[i-2][i-1])


    #n-ti red
    array2[size[0]-1][size[1]-1]=1
    rjesenje1[size[0]-1][0]=(array1[size[0]-1][size[1]-1]-array1[size[0]-1][size[1]-3]*rjesenje1[size[0]-2][0])/(array1[size[0]-1][size[1]-2]-array1[size[0]-1][size[1]-3]*array2[size[0]-2][size[1]-2])
    #rjesenja
    rjesenje[size[0]-1][0]=rjesenje1[size[0]-1][0]
    for i in range(size[0]-1,0,-1):
        rjesenje[i-1][0]=rjesenje1[i-1][0]-rjesenje[i][0]*array2[i-1][i]
    return rjesenje

def implicit_diffusion(initial,constant,n):
    prostornikoraci=len(initial)-2
    Matrix=np.zeros((prostornikoraci,prostornikoraci))
    #print(Matrix)
    Matrix[0,0]=1+2*constant
    Matrix[0,1]=-constant
    for i in range(1,prostornikoraci-1):
        Matrix[i,i-1]=-constant
        Matrix[i,i]=1+2*constant
        Matrix[i,i+1]=-constant
    Matrix[-1,-2]=-constant
    Matrix[-1,-1]=1+2*constant
    plt.plot(x,initial,label="t=0")
    initial.pop(-1)
    initial.pop(0)
    initial=np.transpose([initial])
    Matrix2=np.append(Matrix,initial,axis=1)
    x.pop(0)
    x.pop(-1)
    print(x)
    for j in range(1,n+1):
        rjesenje=thomasalgortihm(Matrix2)
        
        Matrix2=np.append(Matrix,rjesenje,axis=1)

        if j in [100,200,300,400]:
            plt.plot(x,rjesenje,label="t={}s".format(round(j*deltat)))
    plt.legend()
    plt.title("Implicitno rješenje")
    plt.show()
implicit_diffusion(početni,konstanta,400)