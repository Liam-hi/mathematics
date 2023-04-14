#Koefficienten:
p = [2, 0, 1]
q = [-2, 1, 0, 0, 1]

def eval_poly(p,x):

    degree = []

#Använder for-loop för att generera potenser, till exempel 3^2, 3^1, 3^0. 
#Tar hjälp av lenght-funktionen för att generera rätt antal potenser.   
    
    for i in range(len(p)): 
        degree.append(x ** i)
#Multiplicerar p med degree, det vill säga koefficinten gånger x upphöjt till i 
       
    mult = [p[l]*degree[l] for l in range(len(p))]
    
    return sum(mult)

print('Tester:')
print(eval_poly(p,0))
print(eval_poly(p,1))
print(eval_poly(p,2)) 
print(eval_poly(q,2))
print(eval_poly(p,(-2))) 
