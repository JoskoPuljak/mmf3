import matplotlib.pyplot as plt
import numpy as np
def linterpol(x_list,y_list,x):
    p_list=[]
    p=0.
    L=1.
    for i in range (0,len(x_list)):
        for j in range (0,len(x_list)):
            if j!=i:
                L*=(x-x_list[j])/(x_list[i]-x_list[j])
        padd=y_list[i]*L
        p_list.append(padd)
        p+=padd
        L=1.
    p_list.append(p)
    return p_list
