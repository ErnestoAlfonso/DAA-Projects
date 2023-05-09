from random import randint

def generate(n:int, k:int):

    tuples= []
    for i in range(k):

        x1 = randint(0, n-1)
        x2 = randint(x1, n-1)
        y1 = randint(0, n-1)
        y2 = randint(y1, n-1)
        tuples.append((x1, y1, x2, y2))
    
    return tuples


