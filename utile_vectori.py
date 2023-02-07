# Realizat de/Produced by Casiu George Valentin
def citire(n,v,tip):
    for i in range (n):
        if tip=="int":
            v.append(int(input("V["+str(i)+"]=")))
        elif tip=="float":
            v.append(float(input("V["+str(i)+"]=")))
        else:
            v.append(input("V["+str(i)+"]="))

def citeste_f(fisier,tip):
    with open(fisier,"r") as f:
        n=int(f.readline())
        linie=f.readline() #sau se poate folosi/or you can use directli: linie=f.readline().replace("\n"," ").split()
        linie=linie.replace("\n"," ")
        linie=linie.split()
        if tip=="int":
            return [n,[int(el) for el in linie]]
        elif tip=="float":
            return [n,[float(el) for el in linie]]
        else:
            return[n,linie]

def afisare(v):
    for el in v:
        print(el,end=" ")
    print()

def scrie_f(fisier,v):
    with open (fisier, "w") as f:
        for el in v:
            f.write(str(el)+" ")
        f.write("\n")

