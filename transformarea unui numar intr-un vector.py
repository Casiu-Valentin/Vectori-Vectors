# Realizat de/Produced by Casiu George Valentin
"""
Se citeşte un numǎr natural n (citirea se va face într-o variabilǎ de tip int). Sǎ se scrie acest numǎr într-un vector.
Exemplu. Dacǎ citim 1231, vom avea V[1]=1, V[2]=2, V[3]=3, V[4]=1.
Transform a natural number in a vector. Example: For 1234 we have V[1]=1, V[2]=2, V[3]=3, V[4]=1.
"""

def citire():# citire numar natural /natural number reading
    n=''
    while not(n.isdecimal()): # daca n nu e zecimal /if n is not decimal
        n = input("Introduceti un numar natural /Enter a natural number:")
        n = n.strip(' +')# elimina spatiile libere si '+' de la inceputul si sfarsitul numarului /remove spaces and '+' from the beginning and end of number
    return int(n)

# Programul principal/The main program
#varianta 1
n=citire()
v=[0 for el in range(len(str(n)))]
for i in range(len(str(n))):
    v[i]=int(str(n)[i])
print(v)

"""
#varianta 2
n=m=citire()
nr = 0
while m != 0:# calculam cate caractere are numarul. Se poate inlocuii cu nr=len(str(m))
    m = m // 10
    nr += 1
v=[0 for el in range(nr)]
for i in range(nr-1,-1,-1):
    v[i] = n % 10
    n = n // 10
print(v)
"""

"""
#varianta 3
n=citire()
print(len(str(n)))
v=[]
while n != 0:
    v.append(n%10)
    n=n//10
v=v[::-1]
print(v)
"""
