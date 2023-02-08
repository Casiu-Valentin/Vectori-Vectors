# Realizat de/Produced by Casiu George Valentin
"""
Se citeşte un vector cu n componente numere naturale. Sǎ se aranjeze numerele în vector astfel încât cele pare sǎ ocupe primele poziţii.
A vector with n natural number as components is read. Arange the number in the vector so that the one who is even occupy the firs position.
Exemplu. Dacǎ/If n=4 şi se citeşte/read 1 2 7 8, o soluţie este/a solution is 2 8 1 7.
"""

# Programul principal/The main program
import utile_vectori as uv

n,v=uv.citeste_f("date.in", "int")
uv.afisare(v)

#varianta 1
k = 0 # indicele ultimului numar par adus/the index of the last even number
for i in range(n):#parcurge toata lista de la stanga la dreapta si ia fiecare numar par si il aduce la inceput dupa ultimul numar par adus
    if v[i] % 2 == 0:#/it goes through the whole list from left to right and take each even number and brings it to the begining after the last even number brought
        x = v[i]#retine numarul par sa nu se piarda la mutare/keep the even number so they don't get lost when moving
        for j in range(i, k, -1):# muta toate elementele spre dreapta de la elementul par gasit pana la ultimul par gasit
            v[j] = v[j-1]#/move all elements to the right from the next even element found to the last one found
        v[k] = x
        k += 1
print("V sortat: ")
uv.afisare(v)

"""
#varianta 2
k = n-1 # indicele ultimului numar impar adus/the index of the last odd number
for i in range(n-1,-1,-1):#parcurge toata lista de la dreapta la stanga si ia fiecare numar par si il aduce la inceput dupa ultimul numar par adus
    if v[i] % 2 == 1:#/it goes through the whole list from the right to left and take each even number and brings it to the begining after the last even number put
        x = v[i]#retine numarul impar sa nu se piarda la mutare/keep the odd number so they don't get lost when moving
        for j in range(i,k):# muta toate elementele spre stanga de la elementul impar gasit pana la ultimul impar gasit
            v[j] = v[j+1]#/move all elements to the left from the next odd element found to the last one found
        v[k] = x
        k -= 1
print("V sortat: ")
uv.afisare(v)
"""

"""
#varianta 3
t = 0
for el in v: #t calculeaza cate numere sunt pare/calculate how many numbers are even
    if el%2==0:
        t += 1
print(t)
for i in range(t):# pentru fiecare numar par luat de la sfarsit spre inceput il duce pe prima pozitie 
    for i in range (n-1,0,-1):#/for each even number taken from the end to begining, it brings to the first position
        if v[i]%2==0:
            v[i],v[i-1]=v[i-1],v[i]
print("V sortat: ")
uv.afisare(v)
"""

"""
#varianta 4
t = 0
for el in v: #t calculeaza cate numere sunt impare/calculate how many numbers a odd
    if el%2==1:
        t += 1
for i in range(t):# pentru fiecare numar impar luat de la inceput spre sfarsit il aduce pe ultima pozitie
    for i in range (n-1):#/for each odd number taken from the begining to end it bring it to the last position
        if v[i]%2==1:
            v[i],v[i+1]=v[i+1],v[i]
print("V sortat: ")
uv.afisare(v)
"""

"""
#varianta 5
vs=[]
for el in v:
    if el % 2==0:
        vs.append(el)
for el in v:
    if el % 2==1:
        vs.append(el)
print("V sortat: ")
uv.afisare(vs)
"""

"""
#varianta 6
vs = [0 for el in v ]
k = 0
for i in range(n) :
    if v[i] % 2 == 0:
        vs[k] = v[i]
        k += 1
for i in range(n) :
    if v[i] % 2 == 1:
        vs[k] = v[i]
        k += 1
print("V sortat: ")
uv.afisare(vs)
"""
