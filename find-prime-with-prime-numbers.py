"""Find prime numbers with prime numbers"""
"""Slow but funnt for prime geeks"""


p = [2]

def Primes(pp):
    l = [x * pp for x in p if x < pp]
    pl = p[:len(l)]
    test = sum(x for x in range(len(pl)) if l[x] % 2 == 0 or pp * 2 % pl[x] == 0)
    return test

# Print all prime numbers from 1 to 1000. 


for x in range(1, 1000, 2):
    if x != 1 and Primes(x) == 0:
        p.append(x)
        
print(p)
