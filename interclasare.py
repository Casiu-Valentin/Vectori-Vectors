# Realizat de/Produced by Casiu George Valentin
"""
Se dau n numere raţionale distincte, reţinute în doi vectori a şi b şi m numere raţionale distincte reţinute în c şi d.
Atât cele n numere reţinute în vectorii a şi b, cât şi cele m numere reţinute în vectorii c şi d sunt sortate crescǎtor.
Se cere sǎ se interclaseze cele douǎ şiruri de numere.
We given n distinct rational number hold in two vectors a and b, and m distinct rational number hold in vectors c and d.
Both the n number stored in vectors a and b, as well m number stored in vectors c and d are sorted in ascending order.
it is request to interclasify the two strings of numbers.
"""

# Programul principal/The main program
import utile_vectori as uv
a = [1, 3, 5, 7]
b = [2, 4, 6, 8]
c = [11, 33, 55, 77, 99]
d = [21, 44, 69, 89, 100]
n = len(a)
m = len(c)
e = [0 for i in range(m+n)]
f = [0 for i in range(m+n)]
i = j = k = 0
while i < n and j < m:
    if (a[i]/b[i]) < (c[j]/d[j]):
        e[k] = a[i]; f[k] = b[i]
        i += 1
    else:
        e[k] = c[j]; f[k] = d[j]
        j += 1
    k += 1
if i < n:
    for t in range(i, n):
        e[k] = a[t]; f[k] = b[t]
        k += 1
else:
    for t in range(j, m):
        e[k] = c[t]; f[k] = d[t]
        k += 1
print("a=", end=" "); uv.afisare(a)
print("b=", end=" "); uv.afisare(b)
print("c=", end=" "); uv.afisare(c)
print("d=", end=" "); uv.afisare(d)
x = [round(e[i]/f[i],2) for i in range(m+n)]
print("Vectorul sortat/Sorted vector=", end=" "); uv.afisare(x)
print("e=", end=" "); uv.afisare(e)
print("f=", end=" "); uv.afisare(f)
