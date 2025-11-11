with open("V(H-H)_AK.txt", "w") as file1:
    file1.write("#  r/A°      V/K\n")
    file1.write("#  ------  -------------\n")
    with open("V(H-H).txt", "r") as file2:
        check=1
        for line in file2:
            if check>2:
                part=line.split("   ")
                r=float(part[0])*0.52917721092
                V=float(part[1])*315775.04
                file1.write(f" {r:8.4f}  {V:13.6f}\n")
            check+=1
with open("V(H-H)_Ak.txt", "r") as file3:
    x_lista=[]
    y_lista=[]
    check=0
    for line in file3:
        if check >1:
            x_lista.append(line.split("  ")[1])
            y_lista.append(line.split("  ")[2])
        check +=1
    print(x_lista)
    print(y_lista)