# Produced by/Realizat de Casiu George Valentin
"""
Se citeşte un numǎr natural n (citirea se va face într-o variabilǎ de tip int). 
Sǎ se scrie acest numǎr într-un vector. Exemplu: Pentru 1231, vom avea V[1]=1, V[2]=2, V[3]=3, V[4]=1.
Transform a natural number read in a vector. Example: For 1234 we have V[1]=1, V[2]=2, V[3]=3, V[4]=1.
"""

def citire():# citire numar natural /natural number reading
    n=''
    while not(n.isdecimal()): # daca n nu e zecimal /if n is not decimal
        n = input("Introduceti un numar natural /Enter a natural number:")
        n = n.strip(' +')# elimina spatiile libere si '+' de la inceputul si sfarsitul numarului /remove spaces and '+' from the beginning and end of number
    return int(n)

# Programul principal/The main program
#version 1/varianta 1
n=citire()
v=[0 for el in range(len(str(n)))]
for i in range(len(str(n))):
    v[i]=int(str(n)[i])
print(v)

"""
#version 2/varianta 2
n=m=citire()
nr = 0
while m != 0:#calculate how may characters have number. We can change with n=len(str(m))/calculam cate caractere are numarul. Se poate inlocuii cu nr=len(str(m))
    m = m // 10
    nr += 1
v=[0 for el in range(nr)]#we create a vector of lenght of number with all characters 0/cream un vector de lungimea numarului cu toatre componentele 0
for i in range(nr-1,-1,-1):
    v[i] = n % 10
    n = n // 10
print(v)
"""

"""
#version 3/varianta 3
n=citire()
print(len(str(n)))
v=[]
while n != 0:#we add the last digit one by one to a vector/adaugam ultima cifra pe rand la vector
    v.append(n%10)
    n=n//10
v=v[::-1]#we reverse the vector/rasturnam vectorul
print(v)
"""
