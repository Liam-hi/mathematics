class RomanNumerals:
    def __init__(self, a):
            self.a = a
             
    def from_roman(self):
        symbols = {"I" : 1, 
                   "V" : 5, 
                   "X" : 10, 
                   "L" : 50, 
                   "C" : 100,
                   "D" : 500, 
                   "M" : 1000}
        
        numerals = self
        
        memoize = []
        
        for i in numerals:
            memoize.append(i)

    
        summation, odd, answer = [], [], []
   
        for i in numerals[::-1]:
            summation.append(symbols[i])
 
        if len(summation) % 2 == 1:
            odd.append(summation[-1])
            del(summation[-1])
        else:
            odd.append(0)
    
        for i in range(0, len(summation), 2):
            if summation[i] <= summation[i + 1]:
                answer.append(summation[i] + summation[i + 1])
            elif summation[i] > summation[i + 1]:
                answer.append(summation[i] - summation[i + 1])
        
        answer.append(odd[0])

        return sum(answer)
    
    def to_roman(self):
        
        num = str(self)
        save, roman = [], []
              
        for i in range(len(num)):
            save.append(int(num[i] + "0"*(len(num) - i - 1)))
               
        for i in save:
            if i >= 1000:
                roman.append((i // 1000) * "M")
            elif i == 900:
                roman.append("CM")       
            elif i == 400:
                roman.append("CD")
            elif 100 <= i < 400:
                roman.append((i // 100) * "C")
            elif 500 <= i < 900:
                roman.append("D" + int((i - 500) / 100)* "C")
            elif 1 <= i <= 3:
                roman.append(i*"I")
            elif i == 4:
                roman.append("IV")
            elif 5 <= i < 9:
                roman.append("V"+(i-5)*"I")
            elif i == 9:
                roman.append("IX")
            elif 10 <= i < 40:
                roman.append(int(i / 10) * "X")
            elif i == 40:
                roman.append("XL")
            elif 50 <= i < 90:
                roman.append("L" + int((i-50)/(i/10)) * "X")
            elif i == 90:
                roman.append("XC")
            

            x = "".join(roman)   
        
        return x
