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
#varianta 2
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
