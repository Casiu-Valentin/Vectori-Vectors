# Realizat de/Produced by Casiu George Valentin
"""
Se citeşte un vector cu n componente numere naturale. Se cere sǎ se afiseze ca in exemplu.
Exemplu: dacǎ n=4, şi vectorul este 1 2 3 4 afiseaza:
1 2 3 4
2 3 4 1
3 4 1 2
4 1 2 3
"""

def succ(i):
    if i<n-1: i+=1
    else: i=0
    return i

#Program principal/The main program
import utile_vectori as uv

n,v=uv.citeste_f("date.in", "int")

for i in range(n):
    k=i
    for j in range (n):
        print(v[k],end=" ")
        k=succ(k)
    print()