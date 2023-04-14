def root(eqn, x, y):
    eqnClean = eqn.replace("x", "*" + str(y))
    str1 = " "
    
    for i in range(len(eqnClean)):
        if eqnClean[i] == "*" and eqnClean[i - 1] == " ":
            str1 += ""
        elif eqnClean[i] == '^':
            str1 += "**"    
        else:
            str1 += eqnClean[i]
            
    if str1[1] == "*":
        return eval(str1[2:len(str1)]) % x
    else:
        return eval(str1[1:len(str1)]) % x

def poly(a, b):
    """Faktoruppdelar en ring/kropp/grupp. 

    ----------
    a : string
     representerar polynomet
    b : int
     representerar en grupp, ring eller kropp.
    Returns
    -------
    list :
     listan innehåller muterbara objekt som representerar polynomets rötter.
    Examples
    --------
    >>> (poly("x^5 + 2x^4 + 2x^2 + 1", 3)
    ([2, 4])
    """
    l = []
    for i in range(b):
        if root(a, b, i) == 0:
            l.append(i)
    
    return l
        
    
print(poly("x^5 + 2x^4 + 2x^2 + 1", 3))
# print(poly("x^2 + 4x + 3", 5))
