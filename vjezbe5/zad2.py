with open("V(H-H)_AK.txt", "w") as file1:
    file1.write("#  r/A°      V/K\n")
    file1.write("# ------ -------------\n")
    with open("V(H-H).txt", "r") as file2:
        check=1
        for line in file2:
            if check>2:
                part=line.split("   ")
                r=float(part[0])*0.52917721092
                V=float(part[1])*315775.04
                file1.write(f"{r:8.4f} {V:13.6f}\n")
            check+=1