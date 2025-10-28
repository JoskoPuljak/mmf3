import thomas as tom
import numpy as np
matrica1=[[4,-2,0,0,5],[-2,6,-2,0,0],[0,-2,6,-2,0],[0,0,-2,8,0]]
a=tom.thomasalgortihm(matrica1)
print(94*a)
with open("rjesenje.txt", "w") as f:
    for i in range (0,a.shape[0]):
        f.write("Struja {} ima vrijednost {} \n".format(i+1,a[i][0]))