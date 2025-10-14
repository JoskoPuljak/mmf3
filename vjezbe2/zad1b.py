import numpy as np
def drugaderivacija(f,x,h):
    return (f(x+h)-2*f(x)+f(x-h))/(h**2)
with open("drugaderivacija.txt","a") as f:
    f.write(f"{'x':2s} | {'h=0.1':24s} | {'h=0.001':24s} | {'h=0.0001':24s} | {'h=0.00001':24s} | {'h=0.000001':24s} | {'h=0.000001':24s}\n")
    f.write (f"{0:2d} | {drugaderivacija(np.exp,0,0.1):24.16f} | {drugaderivacija(np.exp,0,0.001):24.16f} | {drugaderivacija(np.exp,0,0.001):24.18f} | {drugaderivacija(np.exp,0,0.0001):24.18f} | {drugaderivacija(np.exp,0,0.00001):24.18f} | {drugaderivacija(np.exp,0,0.0000001):24.18f}\n")
    f.write(f"{1:2d} | {drugaderivacija(np.exp,1,0.1):24.18f} | {drugaderivacija(np.exp,1,0.001):24.18f} | {drugaderivacija(np.exp,1,0.001):24.18f} | {drugaderivacija(np.exp,1,0.0001):24.18f} | {drugaderivacija(np.exp,1,0.00001):24.18f} | {drugaderivacija(np.exp,1,0.0000001):24.18f}\n")
    f.write(f"{2:2d} | {drugaderivacija(np.exp,2,0.1):24.18f} | {drugaderivacija(np.exp,2,0.001):24.18f} | {drugaderivacija(np.exp,2,0.001):24.18f} | {drugaderivacija(np.exp,2,0.0001):24.18f} | {drugaderivacija(np.exp,2,0.00001):24.18f} | {drugaderivacija(np.exp,2,0.0000001):24.18f}\n")
    f.write(f"{3:2d} | {drugaderivacija(np.exp,3,0.1):24.18f} | {drugaderivacija(np.exp,3,0.001):24.18f} | {drugaderivacija(np.exp,3,0.001):24.18f} | {drugaderivacija(np.exp,3,0.0001):24.18f} | {drugaderivacija(np.exp,3,0.00001):24.18f} | {drugaderivacija(np.exp,3,0.0000001):24.18f}\n")
    f.write(f"{4:2d} | {drugaderivacija(np.exp,4,0.1):24.18f} | {drugaderivacija(np.exp,4,0.001):24.18f} | {drugaderivacija(np.exp,4,0.001):24.18f} | {drugaderivacija(np.exp,4,0.0001):24.18f} | {drugaderivacija(np.exp,4,0.00001):24.18f} | {drugaderivacija(np.exp,4,0.0000001):24.18f}\n")
    f.write(f"{5:2d} | {drugaderivacija(np.exp,5,0.1):24.18f} | {drugaderivacija(np.exp,5,0.001):24.18f} | {drugaderivacija(np.exp,5,0.001):24.18f} | {drugaderivacija(np.exp,5,0.0001):24.18f} | {drugaderivacija(np.exp,5,0.00001):24.18f} | {drugaderivacija(np.exp,5,0.0000001):24.18f}\n")
    f.write(f"{6:2d} | {drugaderivacija(np.exp,6,0.1):24.18f} | {drugaderivacija(np.exp,6,0.001):24.18f} | {drugaderivacija(np.exp,6,0.001):24.18f} | {drugaderivacija(np.exp,6,0.0001):24.18f} | {drugaderivacija(np.exp,6,0.00001):24.18f} | {drugaderivacija(np.exp,6,0.0000001):24.18f}\n")
    f.write(f"{7:2d} | {drugaderivacija(np.exp,7,0.1):24.18f} | {drugaderivacija(np.exp,7,0.001):24.18f} | {drugaderivacija(np.exp,7,0.001):24.18f} | {drugaderivacija(np.exp,7,0.0001):24.18f} | {drugaderivacija(np.exp,7,0.00001):24.18f} | {drugaderivacija(np.exp,7,0.0000001):24.18f}\n")
    f.write(f"{8:2d} | {drugaderivacija(np.exp,8,0.1):24.18f} | {drugaderivacija(np.exp,8,0.001):24.18f} | {drugaderivacija(np.exp,8,0.001):24.18f} | {drugaderivacija(np.exp,8,0.0001):24.18f} | {drugaderivacija(np.exp,8,0.00001):24.18f} | {drugaderivacija(np.exp,8,0.0000001):24.18f}\n")
    f.write(f"{9:2d} | {drugaderivacija(np.exp,9,0.1):24.18f} | {drugaderivacija(np.exp,9,0.001):24.18f} | {drugaderivacija(np.exp,9,0.001):24.18f} | {drugaderivacija(np.exp,9,0.0001):24.18f} | {drugaderivacija(np.exp,9,0.00001):24.18f} | {drugaderivacija(np.exp,9,0.0000001):24.18f}\n")
    f.write(f"{10:2d} | {drugaderivacija(np.exp,10,0.1):24.18f} | {drugaderivacija(np.exp,10,0.001):24.18f} | {drugaderivacija(np.exp,10,0.001):24.18f} | {drugaderivacija(np.exp,10,0.0001):24.18f} | {drugaderivacija(np.exp,10,0.00001):24.18f} | {drugaderivacija(np.exp,10,0.0000001):24.18f}\n\n")
    f.write(f"{'error':8s} | {'h=0.1':26s} | {'h=0.001':26s} | {'h=0.0001':26s} | {'h=0.00001':26s} | {'h=0.000001':26s}\n")
    f.write(f"{'error 0':8s} | {abs(drugaderivacija(np.exp,0,0.1)-np.exp(0)):26.20} | {abs(drugaderivacija(np.exp,0,0.001)-np.exp(0)):26.20} | {abs(drugaderivacija(np.exp,0,0.0001)-np.exp(0)):26.20} | {abs(drugaderivacija(np.exp,0,0.00001)-np.exp(0)):26.20} | {abs(drugaderivacija(np.exp,0,0.000001)-np.exp(0)):26.20}\n")
    f.write(f"{'error 1':8s} | {abs(drugaderivacija(np.exp,1,0.1)-np.exp(1)):26.20} | {abs(drugaderivacija(np.exp,1,0.001)-np.exp(1)):26.20} | {abs(drugaderivacija(np.exp,1,0.0001)-np.exp(1)):26.20} | {abs(drugaderivacija(np.exp,1,0.00001)-np.exp(1)):26.20} | {abs(drugaderivacija(np.exp,1,0.000001)-np.exp(1)):26.20}\n")
    f.write(f"{'error 2':8s} | {abs(drugaderivacija(np.exp,2,0.1)-np.exp(2)):26.20} | {abs(drugaderivacija(np.exp,2,0.001)-np.exp(2)):26.20} | {abs(drugaderivacija(np.exp,2,0.0001)-np.exp(2)):26.20} | {abs(drugaderivacija(np.exp,2,0.00001)-np.exp(2)):26.20} | {abs(drugaderivacija(np.exp,2,0.000001)-np.exp(2)):26.20}\n")
    f.write(f"{'error 3':8s} | {abs(drugaderivacija(np.exp,3,0.1)-np.exp(3)):26.20} | {abs(drugaderivacija(np.exp,3,0.001)-np.exp(3)):26.20} | {abs(drugaderivacija(np.exp,3,0.0001)-np.exp(3)):26.20} | {abs(drugaderivacija(np.exp,3,0.00001)-np.exp(3)):26.20} | {abs(drugaderivacija(np.exp,3,0.000001)-np.exp(3)):26.20}\n")   
    f.write(f"{'error 4':8s} | {abs(drugaderivacija(np.exp,4,0.1)-np.exp(4)):26.20} | {abs(drugaderivacija(np.exp,4,0.001)-np.exp(4)):26.20} | {abs(drugaderivacija(np.exp,4,0.0001)-np.exp(4)):26.20} | {abs(drugaderivacija(np.exp,4,0.00001)-np.exp(4)):26.20} | {abs(drugaderivacija(np.exp,4,0.000001)-np.exp(4)):26.20}\n")
    f.write(f"{'error 5':8s} | {abs(drugaderivacija(np.exp,5,0.1)-np.exp(5)):26.20} | {abs(drugaderivacija(np.exp,5,0.001)-np.exp(5)):26.20} | {abs(drugaderivacija(np.exp,5,0.0001)-np.exp(5)):26.20} | {abs(drugaderivacija(np.exp,5,0.00001)-np.exp(5)):26.20} | {abs(drugaderivacija(np.exp,5,0.000001)-np.exp(5)):26.20}\n")
    f.write(f"{'error 6':8s} | {abs(drugaderivacija(np.exp,6,0.1)-np.exp(6)):26.20} | {abs(drugaderivacija(np.exp,6,0.001)-np.exp(6)):26.20} | {abs(drugaderivacija(np.exp,6,0.0001)-np.exp(6)):26.20} | {abs(drugaderivacija(np.exp,6,0.00001)-np.exp(6)):26.20} | {abs(drugaderivacija(np.exp,6,0.000001)-np.exp(6)):26.20}\n")
    f.write(f"{'error 7':8s} | {abs(drugaderivacija(np.exp,7,0.1)-np.exp(7)):26.20} | {abs(drugaderivacija(np.exp,7,0.001)-np.exp(7)):26.20} | {abs(drugaderivacija(np.exp,7,0.0001)-np.exp(7)):26.20} | {abs(drugaderivacija(np.exp,7,0.00001)-np.exp(7)):26.20} | {abs(drugaderivacija(np.exp,7,0.000001)-np.exp(7)):26.20}\n")
    f.write(f"{'error 8':8s} | {abs(drugaderivacija(np.exp,8,0.1)-np.exp(8)):26.20} | {abs(drugaderivacija(np.exp,8,0.001)-np.exp(8)):26.20} | {abs(drugaderivacija(np.exp,8,0.0001)-np.exp(8)):26.20} | {abs(drugaderivacija(np.exp,8,0.00001)-np.exp(8)):26.20} | {abs(drugaderivacija(np.exp,8,0.000001)-np.exp(8)):26.20}\n")
    f.write(f"{'error 9':8s} | {abs(drugaderivacija(np.exp,9,0.1)-np.exp(9)):26.20} | {abs(drugaderivacija(np.exp,9,0.001)-np.exp(9)):26.20} | {abs(drugaderivacija(np.exp,9,0.0001)-np.exp(9)):26.20} | {abs(drugaderivacija(np.exp,9,0.00001)-np.exp(9)):26.20} | {abs(drugaderivacija(np.exp,9,0.000001)-np.exp(9)):26.20}\n")
    f.write(f"{'error 10':8s} | {abs(drugaderivacija(np.exp,10,0.1)-np.exp(10)):26.20} | {abs(drugaderivacija(np.exp,10,0.001)-np.exp(10)):26.20} | {abs(drugaderivacija(np.exp,10,0.0001)-np.exp(10)):26.20} | {abs(drugaderivacija(np.exp,10,0.00001)-np.exp(10)):26.20} | {abs(drugaderivacija(np.exp,10,0.0000001)-np.exp(10)):26.20}\n")
    f.write("Vidimo da bez obzira sto je h=0.000001 najmanji korak, greska ne pada ispod 10^-3. To je zbog greske u računanju sa vrlo malim brojevima i float reprezentacijom brojeva u pythonu.\n")
#plottanje grafa greške
import matplotlib.pyplot as plt
x=[0.1,0.01,0.001,0.0001,0.00001,0.000001]	
y=[abs(drugaderivacija(np.exp,1,h)-np.exp(1)) for h in x]
y2=[abs(drugaderivacija(np.exp,5,h)-np.exp(5)) for h in x]
y3=[abs(drugaderivacija(np.exp,10,h)-np.exp(10)) for h in x]
plt.loglog(x,y,label="x=1",color="blue")
plt.loglog(x,y2,label="x=5",color="orange")
plt.loglog(x,y3,label="x=10",color="green")
plt.legend(["x=1","x=5","x=10"])
plt.show()
plt.savefig("drugaderivacija.png")