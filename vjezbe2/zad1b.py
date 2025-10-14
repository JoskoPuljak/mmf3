import numpy as np
def drugaderivacija(f,x,h):
    return (f(x+h)-2*f(x)+f(x-h))/(h**2)
with open("drugaderivacija.txt","a") as f:
    f.write (f"{drugaderivacija(np.exp,0,0.1):2.16f} | {drugaderivacija(np.exp,0,0.001):2.16f} | {drugaderivacija(np.exp,0,0.001):2.16f} | {drugaderivacija(np.exp,0,0.0001):2.16f} | {drugaderivacija(np.exp,0,0.00001):2.16f} | {drugaderivacija(np.exp,0,0.0000001):2.16f}\n")

