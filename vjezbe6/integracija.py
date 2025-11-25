def trapez(a,b,m,f):
    h=(b-a)/m
    integral=0.5*(f(a)+f(b))
    for i in range(1,m):
        integral += f(a+i*h)
    integral *= h
    return integral
def simpson(a,b,m,f):
    if m%2==1:
        m+=1
    h=(b-a)/m
    integral=f(a)+f(b)
    for i in range(1,m,2):
        integral += 4*f(a+i*h)
    for i in range(2,m-1,2):
        integral += 2*f(a+i*h)
    integral *= h/3
    return integral