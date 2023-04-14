#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

"""
l = ["hej", 5.0, (3,2), 10, 24, "Nima", [3,2,1], 40]

def my_div_calc(data, p):
    new_data = []
    for x in data:
        if type(x) == int or type(x) == float:
            new_data.append(x)
    new_set = []
    for i in new_data:
        if i % p == 0:
            new_set.append(i)
    return len(new_set)

print(my_div_calc(l, 2))
"""

"""

def hej(z1,z2):
    return sum(map(lambda x,y: x*x + y, z1,z2))

print(hej([3,0,1,2,7,11],[2,0,1,2]))

def f(data, second_data):
    if len(data) > len(second_data):
        for q in range(len(data)-len(second_data)):
            data.pop()
    
    t = [x**2 for x in data]
    z = [y for y in second_data]
    nyy = []
    for x in range(len(data)):
        nyy.append(t[x]+z[x])

    return sum(nyy)

print(f([3,0,1,2,7,11],[2,0,1,2]))
"""

    
"""
def getname():
    UI = input(str("Name:"))  
    nynamn = UI.split()
    if len(nynamn) == 1:
        return getname()  
    elif len(nynamn) == 0:
        return getname()
    elif len(nynamn) > 1:
        print(nynamn[0], nynamn[-1])

getname()

#Sammanfattning:
#Vi tar in en input av användaren.
#Delar upp inputet till enskilda strängar mha av split()
#Sätter premisserna: om längden av samtliga strängar är en: börja om funktionen:
#Om noll: börja om.
#Om större än ett: behåll första och sista strängen. 
    
"""

"""
hej = []
x=0
for y in range(5):
    for z in range(3):
        x = (z+y)
print(x)
"""

"""
  
alf = ["aeiou"]
sträng = "" 
for x in "Du är en riktig horunge!":
    for y in alf:
        if x in y:
            sträng += x

print(sträng)


#Definera vokalerna
#Definiera en tom sträng
#Iterera över strängen 
#Iterera över vokalerna
#Om strängen som itererar finns med i vokalerna som itererar
#Lägg till sträng

"""


def kvadrater(n):
    squares = []
    for x in range(n):
        if x**2 < n:
            squares.append(x**2)
    return squares

print(kvadrater(20))

y = [x**2 for x in range(10) if x**2 < 10]

print(y)

"""
tuples = [(0,0), (0,2), (2,3), (3,5), (7,8)] 

onetuple = (2,4)
x,y = tuples[1]
print((x))

def interval_merge(l):
    x_axis = []
    y_axis = []
    for i in range(len(l)):
        x,y = l[i]
        x_axis.append(x)
        y_axis.append(y)
    
        
    return min(x_axis), max(y_axis)

print(interval_merge(tuples))

#Den var inte så svår. Sorterar alla x och y för sig själv. 
"""

barr_fakta = {'gran' : 'korta barr', 'tall' : 'långa barr'}

hej = []
for x,v in barr_fakta.items():
    print(x,len(v))


"""
def ff(d):
    for k, v in d.items():
        print(k, len(v))
        
print(ff(barr_fakta))
"""      
        
a = [1,2,3,4]
b = [17,12,11,10]

y = map(lambda x,y:x**2+y, a,b) 

print(y)
print(list(y))


fib = [0,1,1,2,3,5,8,13,21,34,55]
result = filter(lambda x: x % 3, fib)
print(list(result))

p = filter(lambda x: len(x)==3, ['one', 'two', 'three', 'four', 'five'])
print(list(p))    

  

d = {"a":1, "b":2}
c = {"c":1, "e":2}

for x, y in (c.items()):
    d[x] = y

print(d)

#Med två listor skapa en dictionary där första listan är nycklar
#och andra listan värden. 

strängar = ["a","b","c","d"]
siffror = [1,2,3,4]

y = zip(strängar, siffror)
print(list(y))

nydict = {}

for x, v in zip(strängar, siffror):
    nydict[x] = v
    
print(nydict)

#Extrahera alla nycklar till en nu lista.

värden = []
for x,y in nydict.items():
    värden.append(y)
print(värden)


#Find keys by value

a_dict = {"a":3, "Nima":32, "Li":33}

def dict_by_value(your_dict, value):
    key = []
    for x, y in your_dict.items():
        if y == value:
            key.append(x)
    return key 
print(dict_by_value(a_dict, 32))


#Skriv en funktion diff som räknar och returnerar antalet skillnader
#, positionsvis, för två strängar, listor, eller liknande datastruktur. 
#Du kan anta att de två parametrarna har samma längd.
#Exempelanvändning:

#diff(’Hubba’, ’bubba’)
#1
#diff(’DA2004’, ’DA2004’)
#0
#diff([1,2,3], [3,2,1])
#2
"""
def diff(wordcheck, change):
    tom = ""
    for x in wordcheck:
        if x in change:
            tom += x
    return len(wordcheck)- len(tom)

print(diff("hEj","hej"))
"""

"""
tom = []
for x in [1,2,3]:
    for y in [0,7,3,5]:
        if x == y:
            tom.append(x)
print(tom)
            

def differ(w,c):
    if type(w) == list and type(c) == list:
        tom = []
        for x in w:
            for y in c:
                if x == y:
                    tom.append(x)    
        print(tom)
        return len(tom) - len(c)
    elif type(w) == str and type(c) == str:
        tom1 = ""
        for x in c:
            if x in w:
                tom1 += x
        print(tom1)
        kk = len(w) - len(tom1)
                
        return kk
        
        
print(differ([2,2,3],[1,2,3]))
"""


def a(f):
    return lambda x, y : f(x) + f(y)

print(sum(map(a(lambda x: 2*x), [1,0,1], [1,2,3])))



#Definiera funktionen lol_check (”list-of-lists check”) 
#som tar en lista av listor som parameter och returnerar 
#True om något element är sant och False annars.

#[[]] tom list in lists

def lol_check(l):
    list(enumerate(l))
    for i in range(len(l)):
        x,y = list(enumerate(l))[i]
        if True in y:
            return True
    else:
        return False 
    
print(lol_check([[]]))
print(lol_check([[True]]))
print(lol_check([[], [False, False]]))
print(lol_check([[], [False, False], [True]]))

#Definiera en funktion.
#Använder enumerate för att indexera listorna i listan
#Itererar över samtliga listor i listan för att undersöka om True finns med i någin vardera


#Skriv en funktion remove_underscore som tar in en sträng 
#och returnerar samma sträng men med alla “underscore” (_) borttagna.


def remove_underscore(s):
    y = s.replace("_","")
    return y

print(remove_underscore("_Hej_"))


#Skriv en funktion underscore_int som tar ett heltal 
#och returnerar talet konverterat till en sträng med 
#underscore insatt för att markera tusental


"""
    
def underscore_int(l):
    l = str(l)
    if len(str(l)) <= 3:
        return str(l)
    elif len(str(l)) > 3:
        emptylist = []
        for x in str(l):
            emptylist.append(x)
        print(emptylist)
        sträng = ""
        
        for x in range(1,len(l), 3):
            emptylist[x] = "_"+emptylist[x]
        
        for x in emptylist:
            sträng += x
            
        return sträng

print(underscore_int(1000000))
"""
"""

l = "1000"      #Strängen 
l_list = []     #Tom lista (Vi vill bryta ner strängen till enskilda strängar och appenda dem till en lista.)
for x in l:     #Itererar 
    l_list.append(x) #Sparar strängarna i l_list
    
for x in range(1, len(l), 3):       #En lista är muterbar. Uttnyttjar det för att ändra innehållet i listan. 
    l_list[x] = "_"+l_list[x]       #Lägger till "_" var tredje kolumn. 
    
sträng = ""
for x in l_list:                    #Skapar en tom sträng
    sträng += x                     #Stoppar in elementen i listan i en sträng
print(sträng)
    
"""

#Skriv en funktion invert_dict som tar en uppslagstabell
# och returnerar en ny uppslagstabell där nycklar och associerade 
#värden har bytt plats. Du kan anta att alla värden i uppslagstabellen 
#är unika och icke muterbara och därför fungerar bra som nycklar.           
    
#d = {’a’:1, ’b’: 2}
#1:’a’, 2:’b’}

"""

a = {"a":1, "b":2}

def invert_dict(d):
    if len(d) == 0:
        return d
    else:
        nycklar = []
        värden = []
        for x,y in d.items():
            nycklar.append(x)
            värden.append(y)
            d_reverse = {}
            
        for x in range(len(nycklar)):
            d_reverse[värden[x]] = nycklar[x]
    return d_reverse 

print(invert_dict(a))

"""


"""


l = [1,2,3,4,5] 
y = 0
l_list = []
for x in l:
    y += x
    l_list.append(y)
print(l_list)

"""

"""

#{’A’: 0, ’C’: 0, ’G’: 0, ’T’: 0}

l = "AACAATT"
l1 = []

for x in l:
    l1.append(x)
l1.sort()
l3 = []
print(l1)

for x in "ACGT":
    l3.append(l1.count(x))

print(l3)

kuk = "ACGT"
d = {}

strängar = ["a", "C", "G", "T"]

for x, v in zip(strängar, l3):
    d[x] = v
    
print(d)

"""
#s = "AAACAAACAAATTTTTTG"
def count_nucleotides(s):
    l = []
    for x in s:
        l.append(x)
        
    l.sort()
    l2 = [] 
    
    for i in "ACGT":
        l2.append(l.count(i))
        
    nucleods = ["A", "C", "G", "T"]   
    
    y = list(zip(nucleods, l2)) 
    
    d = {}
    
    for i,j in y:
        
        d[i] = j
        
    return d

print(count_nucleotides("AAACAAACAAATTTTTTG"))
    
    
#Funktionen capitalize (nedan) tar en sträng s som parameter 
#och returnerar en ny version av s där varje ord börjar med stor bokstav. Det är meningen att funktionen ska fungera så här:
lista = []
bokstav = "mitt namn är Nima Rahimian Esfahani"
y = bokstav.split()

print(y)
nylista = []
for x in y:
    nylista.append(x.capitalize())
print(nylista)



class DNA:
    def __init__(self, s):
        self.s = s
        
    
    def composition(self):
        return count_nucleotides(self.s)
    
    

gene = DNA("ACGTAAAGTC") 

print(gene.composition())


y = list(map(lambda x: x + 2, [x for x in range(10) if x % 2 == 0]))

print(y)

p = [i**2 for i in list(map(lambda x: x + 2, [x for x in range(10) if x % 2 == 0]))]

print(p)



userinput = "GGTA"

value = [1,2,3,4]

dna = "ACGT"
sort = ""

for x in userinput:
    if x in dna:
        sort += x

print(sort)

antal = []

antal.append(sort.count("A"))
antal.append(sort.count("C"))
antal.append(sort.count("G"))
antal.append(sort.count("T"))
print(antal)
print(value)

nylista = []
for j in range(len(value)):
    nylista.append(value[j] * antal[j])


dna_list = []
for i in dna:
    dna_list.append(i)
    
print(dna_list)

y = list(zip(dna_list, nylista))

dna_sum = {}

for u,v in y:
    dna_sum[u] = v
    
print(dna_sum)
print(sum(nylista))
    
    
class Course:
    def __init__(self, code, name, year=2020): 
        self.participants = []
        self.code = code
        self.name = name
        self.year = year
    def number_participants(self):
        return len(self.participants)

    def new_participant(self, name, email):
        self.participants.append((name, email))
       
        
        
da2004 = Course("DA2004", "Programmeringsteknik")
