# Realizat de /Produced by Casiu George Valentin
"""
Variante de afisare al indicelui unui element in lista/How return index of element from list
Pentru/For lista = ["Python","JavaScript","Python","C Sharp","Java","Python","C++","Python"] si/and item="Python"
Afiseaza: /Display:
1.  [0, 2, 5, 7]
2.  [0, 2, 5, 7]
..............
26.  [0, 2, 5, 7]
27.  [0 2 5 7]
"""

lista=["Python","JavaScript","Python","C Sharp","Java","Python","C++","Python"]

#varianta/version 1
a=[i for i in range(len(lista)) if lista[i]=="Python"]
print('1. ', a)

#varianta/version 2
a=[]
t = (i for i in range(len(lista)) if lista[i]=="Python")
while True:
    try:
        a.append(next(t))
    except StopIteration:
        break
print('2. ',a)

#varianta/version 3
a=[]
for i in range(len(lista)):
    if lista[i]=='Python':
        a.append(i)
print('3. ', a)

#varianta/version 4
a = [i for i,j in enumerate(lista) if j == "Python"]
print('4. ', a)

#varianta/version 5
a=[]
t = (i for i,j in enumerate(lista) if j == "Python")
while True:
    try:
        a.append(next(t))
    except StopIteration:
        break
print('5. ',a)

#varianta/version 6
a=[]
for i,j in enumerate(lista):
    if j == "Python":
        a.append(i)
print('6. ', a)

#varianta/version 7
import itertools
a=[i for i,j in zip(itertools.count(), lista) if j == 'Python']
print('7. ', a)

#varianta/version 8
import itertools
a=[]
t=(i for i,j in zip(itertools.count(), lista) if j == 'Python')
while True:
    try:
        a.append(next(t))
    except StopIteration:
        break
print('8. ',a)

#varianta/version 9
import itertools
a=[]
for i,j in zip(itertools.count(), lista):
    if j == 'Python':
        a.append(i)
print('9. ', a)

#varianta/version 10
a=[]
i=0
while i<len(lista):
    if lista[i]=='Python':
        a.append(i)
    i+=1
print('10. ', a)

#varianta/version 11
a=[]
s=0
for i in lista:
    if i=='Python':
        a.append(lista.index(i,s))
    s += 1
print('11. ', a)

#varianta/version 12
a = []# pentru mine aceasta este cea mai optima si simpla versiune/for me this is the most optimum and simplest version
s=0
for i in range(lista.count("Python")):
    a.append(lista.index("Python",s))
    s = a[-1]+1
print("12. ",a)

#varianta/version 13
a=[]# si aceasta este foarte frumoasa si optima/and this is very beautiful and optimum
s=0
while "Python" in lista[s:]:
            i=lista[s:].index("Python")
            a.append(s+i)
            s+=i+1
print("13. ",a)

#varianta/version 14
a = []
i=0
s=0
while i < lista.count("Python"):
        a.append(lista.index("Python",s))
        i+=1
        s = a[-1]+1
print("14. ",a)

#varianta/version 15
a = []
s=0
try:
    while s < len(lista):
        a.append(lista.index("Python",s))
        s = a[-1]+1
except ValueError:
    print(end="")
print("15. ",a)

#varianta/version 16
a=[]
s=-1
for i in lista:
    if i=='Python':
        s=lista.index(i,s+1)
        a.append(s)
print('16. ', a)

#varianta/version 17
a=[]
i=-1
while True:
    try:
        i=lista.index('Python',i+1)#functia index resturneaza ValueError daca itemul nu se afla in lista/function index return ValueError if item is not in list
        a.append(i)
    except ValueError:
        break
print('17. ', a)

#varianta/version 18
def indice(value, lista):# aceasta varianta e la fel ca 17 doar cu functii. Este facuta doar pentru a exemplifica folosirea functiilor/This version is just like 17 but with functions. Is made only for exemplify the use of function
    a = []
    i = -1
    while True:
        try:
            i = lista.index(value, i+1)#functia index resturneaza ValueError daca itemul nu se afla in lista/function index return ValueError if item is not in list
            a.append(i)
        except ValueError:
            break
    return a
print("18. ", indice("Python", lista))

#varianta/version 19
import collections
a = collections.defaultdict(list)
for i,e in enumerate(lista):
    a[e].append(i)
print("19. ",a["Python"])

#varianta/version 20
import collections
a=collections.defaultdict(list)
for i in range(len(lista)) :
    a[lista[i]].append(i)
print("20. ",a["Python"])

#varianta/version 21
import collections
a=collections.defaultdict(list)
i=0
while i<len(lista) :
    a[lista[i]].append(i)
    i+=1
print("21. ",a["Python"])

#varianta/version 22
import collections
a=collections.defaultdict(list)
s=-1
for i in lista:
    s=lista.index(i,s+1)
    a[i].append(s)
print('22. ', a["Python"])

#varianta/version 23
a= lambda x : [i for i,y in zip(range(len(lista)),lista) if x == y]
print('23. ',a("Python"))

#varianta/version 24
try:
    a = dict(zip(set(lista), map(lambda y: [i for i,z in enumerate(lista) if z is y ], set(lista))))
    print("24. ", a["Python"])
except KeyError:
    print(end="")

#varianta/version 25
print("25. ",list(map(lambda x: x[0],(filter(lambda x: x[1]=="Python", enumerate(lista))))))

#varianta/version 26
import more_itertools
print("26. ",list(more_itertools.locate(lista, lambda x: x == "Python")))

#varianta/version 27
import pandas
a = pandas.Series(lista)
print('27. ',list(a[a == 'Python'].index))

#varianta/version 28
import numpy
i= numpy.where(numpy.array(lista)=="Python")[0]
print ('28. ',i)
