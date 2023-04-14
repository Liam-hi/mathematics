#Python-representation av ett polynom

p = [1, 2, 0, 7, 1, 1]
q = [1, 2]

def add_poly(p,q):
    
    #Med hjälp av nedanstående kodsnutt får p & q samma längd. 
    if len(p) > len(q):
        q += ([0] * (len(p) - (len(q))))
    elif len(p) < len(q):
        p += ([0] * (len(q) - (len(p))))
        
    #Utnyttjar For-loop och rangefunktionen för att addera listorna med varandra. 
    add = [p[x] + q[x] for x in range(len(q))]
    return add

print(add_poly(p,q))

#B

def sub_poly(p,q):
    #Med hjälp av nedanstående kodsnutt får p & q samma längd. 
    if len(p) > len(q):
        q += ([0] * (len(p) - (len(q))))
    elif len(p) < len(q):
        p += ([0] * (len(q) - (len(p))))
        
        
    #Utnyttjar For-loop och rangefunktionen för att addera listorna med varandra. 
    sub = [p[x] - q[x] for x in range(len(q))]
    return sub

print(sub_poly(p,q))
print(sub_poly(p,p))

#C

def eq_poly(x, y):
    if x == y:
        return ('True')
    else:
        return ('False')
    
print(eq_poly(add_poly(p,q),add_poly(q,p)))
