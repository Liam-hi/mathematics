#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 11:16:16 2021

@author: nimarahimian
"""

#Skriv en funktion f för att skriva ut alla nycklar och längder 
#på nycklarnas associerade värden i en uppslagstabell (eng: dictionary), 
#en nyckel och dess värde per rad. Du ska anta att både nycklar och dess 
#värden är strängar. Ex: Med uppslagstabellen

barr_fakta = {"gran" : "korta barr","tall" : "långa barr"}

#gran 10
#tall 10

for i,j in barr_fakta.items():
    print(i,len(j))
    
#Skriv en funktion n_vowels som tar en sträng s som indata och 
#returnerar antalet vokaler i s. Det räcker att känna igen dessa 
#vokaler: a, e, i, o, u, y.
    
exempelmening = "Nima Rahimian"
tom = ""
for x in range(len(exempelmening)):
    if exempelmening[x] in "aeiouy":
        tom += exempelmening[x]

print(tom)
        
#Om du vill instantiera ett objekt av klass A i exempelkoden på sista sidan (sid 7), 
#hur skriver då?
 
class A:
    def __init__(self):
        self.attr_x = 0
    def work(self):
        self.attr_x += 1
    def get_x(self):
        return self.attr_x
class B(A):
    def __init__(self):
        super().__init__()
        self.attr_x = 7
        
#Instantiering ges av anropet A(). Om du vill spara objektet i en variabel så 
#kan du tex skriva a=A().

#Skriv en funktion merge_dicts vars parametrar är två uppslagstabeller (dictionaries) 
#och returnerar en ny uppslagstabell innehållande informationen från de två givna uppslagstabellerna. 
#I händelse av överlappande nycklar så används värdet från den andra uppslagstabellen. Exempel:

#d1 = {’a’: 1, ’b’: 2}
#d2 = {’b’: 3, ’c’: 4}
#d3 = merge_dicts(d1, d2)
#d3 = {’a’: 1, ’b’: 3, ’c’: 4}
        
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

d2_keys = []
d2_values = []

for i,j in d2.items():
    d2_keys.append(i)
    d2_values.append(j)

for x in range(len(d1)):
    d1[d2_keys[x]] = d2_values[x]

print(d1)


#Skriv en funktion diff som räknar och returnerar antalet skillnader, 
#positionsvis, för två strängar, listor, eller liknande datastruktur.
#Du kan anta att de två parametrarna har samma längd.



def n_vowels(s): 
    n=0
    for x in s:
        if x in "aeiouy":
            n += 1
    return n

print(n_vowels("Nima Rahimian"))

print("d")

d = {1: 30, 2: 500, 5: 10, 9: 1000, 18: 45, 23: 20}

l = [1, 5, 18]
l2 = []

#{(1, 5): 530, (5, 18): 1010}

for x in range(len(l) -1):
    x, y = (l[x],  l[x+1])
    if x < y:
        l2.append((x,y))

print(l2)

keys = []


for c in range(len(l2)):
    x, y = l2[c]
    for i, j in d.items():
        if x - 1 < i < y:
            keys.append(i)

print(keys)

d = { 'hej' : 'du', (1, 2, 3) : 'a' }
print(d["hej"])
print(len(d[(1, 2, 3)]))

print (not False)
