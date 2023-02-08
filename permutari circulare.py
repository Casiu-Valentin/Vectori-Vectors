# Realizat de/Produced by Casiu George Valentin
"""
Se citeşte un vector cu n componente numere naturale. Se cere sǎ se obţinǎ toate permutǎrile circulare la dreapta.
A vector with n natural number is read. It is requaired to obtain all circular permutation to the right
Exemplu: dacǎ/if n=4, şi vectorul este/and vector is 1 2 3 4, permutǎrile circulare sunt/circular permutation are:
1 2 3 4
4 1 2 3
3 4 1 2
2 3 4 1
Observaţi faptul cǎ, de fiecare datǎ, ultimul element trece pe prima poziţie, iar restul elementelor sunt deplasate la dreapta cu o poziţie.
Notice, each time, the last element move to the first position, and the rest of elements shifted to the right with one position.
"""

#Program principal/The main program
import utile_vectori as uv

n,v=uv.citeste_f("date.in", "int")
uv.afisare(v)
for i in range(n-1):
    k=v[n-1]
    for j in range (n-1,0,-1):
        v[j]=v[j-1]
    v[0]=k
    uv.afisare(v)
