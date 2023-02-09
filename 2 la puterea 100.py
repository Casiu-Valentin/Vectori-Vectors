# Realizat de/Produced by Casiu George Valentin
"""
Sǎ se calculeze 2 la puterea n, unde n>100
Indicaţie. Dacǎ am calcula produsul pe cǎi clasice, numǎrul obţinut este atât de mare încât nu se poate reprezenta în memorie.
Pentru aceasta,suntem nevoiţi sǎ simulǎm înmulţirea cu 2, reţinând cifrele numǎrului într-un vector.
Astfel, se porneşte de la un vector ale cǎrui componente au valorile:
0 0 0 0 0...0 0 0 1 (numǎrul 1);
 se înmulţeşte fiecare componentǎ a vectorului cu 2:
0 0 0 0 0...0 0 0 2
0 0 0 0 0...0 0 0 4
0 0 0 0 0...0 0 0 8
0 0 0 0 0...0 0 0 16
 dupǎ fiecare înmulţire cu 2 se parcurge vectorul în sens invers şi pentru fiecare componentǎ (n) cu un conţinut mai mare decât 9 se scade 10 şi se adunǎ 1 la componenta n-1:
0 0 0 0 0...0 0 1 6
 se va obţine în continuare:
0 0 0 0 0...0 0 2 12
0 0 0 0 0...0 0 3 2
0 0 0 0 0...0 0 6 4
Estimaţi numǎrul de cifre pe care îl va avea numǎrul 2 la puterea 100 astfel încât sǎ reţinem tipul vector cu atâtea componente câte sunt necesare.
"""

def citire():# citire numar natural /natural number reading
    n=''
    while not(n.isdecimal()): # daca n nu e zecimal /if n is not decimal
        n = input("Introduceti un numar natural /Enter a natural number:")
        n = n.strip(' +')# elimina spatiile libere si '+' de la inceputul si sfarsitul numarului /remove spaces and '+' from the beginning and end of number
    return int(n)

# Programul principal/The main program
x=100# 31 de cifre are 2 la puterea 100. Daca marim puterea trebuie marit si numarul de cifre.
v=[0 for i in range(x)]
v[x-1]=1
print(v)
n=citire()
for i in range(n):
    v=[v[j]*2 for j in range(x)]
    for t in range(x-1, -1, -1):
        if v[t]>9:
            v[t]-=10
            v[t-1]+=1

for i in range (x):#afisarea componentelor vectorului fara 0 la inceput
    if v[i]!=0:
        break
print("Numarul are ",x-i, "cifre")
print("2 ^",n,"= ",end="")
for j in range (i,x):
        print(v[j],end="")