# Times out on large inputs
def minimumSwaps(l, arr):
    cnt = 0
    q = [p-1 for p in arr] # Shift all numbers down by one so that they match their index

    indexes = dict() # Map item to slot
    slots = dict() # Map slot to item

    for i in range(l): # 0..7
        if q[i] == i:
            indexes[i] = i
            slots[i] = i
        else:
            idx = q.index(i)
            indexes[i] = idx
            slots[idx] = i

    for i in range(l): # 0..7
        if indexes[i] == i:
            continue
        swapidx = indexes[i]
        swapval = slots[i]
        cnt += 1
        indexes[i] = i
        slots[i] = i
        indexes[swapval] = swapidx
        slots[swapidx] = swapval

    return cn

# This passes all
def minimumSwaps(l, q):
    cnt = 0
    q = [p-1 for p in q] # Shift all numbers down by one so that they match their index
    
    indexes = dict()
    for i,v in enumerate(q):
        indexes[v] = i

    for v in range(l): # 0..7
        if q[v] == v:
            continue
        swapidx = indexes[v]
        swapval = q[v]
        q[swapidx] = swapval
        indexes[swapval] = swapidx
        indexes[v] = i
        q[v] = i
        cnt += 1
    
    return cn
