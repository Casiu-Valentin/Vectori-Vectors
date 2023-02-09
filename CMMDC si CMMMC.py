# Realizat de/Produced by Casiu George Valentin
"""
Se citeşte un vector cu n componente numere naturale.
Sǎ se afişeze cel mai mare divizor comun si cle mai mic multiplu comun al celor n numere.
"""
def cmmdc(a,b):
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    return(a)

def cmmmc(a,b):
    c=a
    d=b
    while c!=d:
        if c<d:
            c=c+a
        else:
            d=d+b
    return(c)

# Programul principal/The main program
import utile_vectori as uv
n, v = uv.citeste_f("date.in", "int")
uv.afisare(v)

x=v[0]
for i in range(1,n):
    x=cmmdc(x,v[i])
print("cmmdc=",x)

y=v[0]
for i in range(1,n):
    y=cmmmc(y,v[i])
print("cmmmc=",y)
