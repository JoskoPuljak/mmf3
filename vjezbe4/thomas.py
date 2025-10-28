import numpy as np
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

