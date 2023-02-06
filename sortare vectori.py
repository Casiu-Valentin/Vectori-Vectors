# Realizat de /Produced by Casiu George Valentin
"""
Diverse tipuri de sortare a vectorilor/Varios type of vector sorting
In utile_vectori.py avem proceduri de citirea si afisarea vectorilor de la consola cat si din fisier/
In utile_vectori we have procedures to read and display vectors from the console and the file.
"""

import utile_vectori as uv

n,v=uv.citeste_f("date.in","it")
print("V initial: ")
print(v)
uv.afisare(v)

"""
#sortare prin minim/sort by minimum
for i in range (n-1):
    min=v[i]
    k=i
    for j in range(i+1,n):
        if v[j]<min:
            k,min=j,v[j]
    v[i],v[k]=v[k],v[i]
print("V sortat: ")
uv.afisare(v)
"""

"""
#sortarea prin interschimbare(Bubble Sort)/sorting by swap(Bubble Sort)
rez=True
while rez:
    rez=False
    for i in range (n-1):
        if v[i]>v[i+1]:
            v[i],v[i+1]=v[i+1],v[i]
            rez=True
print("V sortat: ")
uv.afisare(v)
"""

"""
#sortarea prin insertie/insertion sort
a=[0 for i in range(n)]
a[0]=v[0]
for i in range (1,n):
    j=i-1
    while v[i]<a[j] and j>=0:
        a[j+1]=a[j]
        j-=1
    a[j+1]=v[i]
print("V sortat: ")
uv.afisare(a)
"""

"""
#sortare cu sort/sort by "sort"
v.sort(reverse=False)
print("V sortat: ")
uv.afisare(v)
"""

"""
#sortare cu sorted/sort by "sorted"
a=sorted(v, reverse=False)
print("V initial dupa sortare: ") #v ramane neschimbat
uv.afisare(v)
print("V sortat: ")
uv.afisare(a)
uv.scrie_f("date.out",v)
"""
