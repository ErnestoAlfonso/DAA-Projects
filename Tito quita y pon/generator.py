from random import randint, choice

def generate(amount_Box: int, amount_Colors: int):
    list_of_Box = []
    for i in range(amount_Box):
        list_aux = []
        colors = [i for i in range(1, amount_Colors + 1)]
        for i in range(3):
            r = choice(colors)
            colors.remove(r)
            list_aux.append((r,randint(0,1)))
        list_of_Box.append(list_aux)
    
    return list_of_Box