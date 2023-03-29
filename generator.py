import random
from random import randint
from source import *
from colorama import Fore, Back, Style

def generator(maxLen : int):
    students = []
    arrLen = random.randint(1, maxLen)
    for i in range(arrLen):
        current_stud_failed = random.choice("P""R")
        current_stud_group = random.randint(1,arrLen)
        students.append(Student(current_stud_failed,current_stud_group))
    
    k = random.randint(1,arrLen)

    print(Fore.WHITE, f"Estudiantes: " + str(students))
    print(Fore.WHITE, f"K: " + str(k))
    return students, k

def tester(amount_to_test : int):
    greedy_solution = Solve(*generator(7))
    backtrack_solution = 3

    print(Fore.GREEN, backtrack_solution)

    if greedy_solution == backtrack_solution:
        print(Fore.GREEN, greedy_solution)
    else:
        print(Fore.RED, greedy_solution)
    
    amount_to_test -= 1
    if amount_to_test > 0:
        return tester(amount_to_test)