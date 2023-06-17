from generator import generate
from tools import box_claus_tranf, brute_force, walkSat



def Solve(boxes, k):
    formula = []
    count_var = k + 1
    print(boxes)
    for box in boxes:
        cero, one = False, False
        for hole in box:
            if hole[1] == 0:
                cero = True
            if hole[1] == 1:
                one = True
        if not cero and not one:
            break
    if cero and one:
        return True
    
    for box in boxes:
        formula += box_claus_tranf(box,count_var)
        count_var += 3

    # return brute_force(formula)  
           
    return walkSat(formula)

     


boxes = generate(3,4)

b1 = [[(2,1),(4,1),(3,1)],[(1,0), (3,1),(2,0)],[(3,1),(1,1),(2,1)]]

print(Solve(b1,4))