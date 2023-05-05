import random
from source import *
from colorama import Fore

def generator(maxLen : int, n : int):
    students = []
    arrLen = random.randint(n, maxLen)
    groups = [i for i in range(1, n+1)]
    for i in range(arrLen):
        if len(groups) == 0:
            groups = [i for i in range(1, n+1)]
        current_stud_failed = random.choice("P""R")
        current_stud_group = random.choice(groups)
        groups.remove(current_stud_group)
        students.append(Student(current_stud_failed,current_stud_group))
    
    k = random.randint(1,arrLen)

    print(Fore.WHITE, f"Estudiantes: " + str(students))
    print(Fore.WHITE, f"K: " + str(k))
    return students, k

def tester(amount_to_test : int):
    stud ,group = generator(7, 3) 
    greedy_solution = Solve(stud,group)
    print("GREEDY: -----> ", greedy_solution)
    backtrack_solution = Solve_bruto(stud,group)

    print(Fore.GREEN,f"Bruto Solution: " + str(backtrack_solution))

    if greedy_solution == backtrack_solution:
        print(Fore.GREEN,"Good Solution: " + str(greedy_solution))
    else:
        print(Fore.RED, "Good Solution: " + str(greedy_solution))
    
    amount_to_test -= 1
    if amount_to_test > 0:
        return tester(amount_to_test)