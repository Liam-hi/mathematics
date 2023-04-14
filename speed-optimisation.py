print("Problem 1")

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.


start = time.time()
def Problem1(x):
    l = []
    for i in range(x):
        if i % 3 == 0 or i % 5 == 0:
            l.append(i)
            
    return sum(l)

print(Problem1(1000))

end = time.time()
print("Time:", end - start)

# Faster algorithm

start = time.time()
def ImprovedProblem1(x):
    return sum(i for i in range(x) if i % 3 == 0 or i % 5 == 0)

print(ImprovedProblem1(1000))
end = time.time()
print("Time:", end - start)

print("Problem 4")

l = []
y = []

for i in range(100, 1000):
    l.append(i)

for j in range(100, 1000):
    y.append(j)
    
    
for i in l:
    print(i * y)
