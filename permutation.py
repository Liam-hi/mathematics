
st = '(12)'

α = {1 : 2, 2 : 1, 3 : 3}

ß = {1 : 3, 2 : 2, 3 : 1}

print(len(α))
print(ß)

for x, y in α.items():
    print(ß[α[x]])
