from collections import defaultdict

cities = [(1,2),(2,3),(2,5),(4,5),(6,7)]

setIdx = 0
sets = defaultdict(list)
for x in cities:
    foundIt = False
    for c in sets:
        for s in sets[c]:
            if not set(s).isdisjoint(x):
                foundIt = True
                break
        if foundIt:
            break
    if foundIt:
        sets[c].append(x)
    else:
        setIdx += 1
        sets[setIdx].append(x)


print(sets)
print(x)
