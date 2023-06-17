# from sat import *
import itertools
import random
from random import choice
import numpy as np

def box_claus_tranf(box: list[tuple], i):
    pos_mask = 2**i + 2**(i+1) + 2**(i+2)
    nev_mask = 0
    cl = []
    cl.append({(str(i), True), (str(i+1), True), (str(i+2), True)})
    cl += create_4_clause(box[0][0], box[1][0], i)
    cl += create_4_clause(box[1][0], box[2][0], i+1)
    cl += create_4_clause(box[0][0], box[2][0], i+2)
        
    return cl

def create_4_clause(color1, color2, aux):
    cl = []
    cl.append({(str(aux), False), (str(color1), False), (str(color2), False)})
    cl.append({(str(aux), False), (str(color1), True), (str(color2), False)})
    cl.append({(str(aux), False), (str(color1), True), (str(color2), True)})
    cl.append({(str(aux), True), (str(color1), False), (str(color2), True)})
    return cl



def brute_force(cnf):
    literals = set()
    for conj in cnf:
        for disj in conj:
            literals.add(disj[0])
 
    literals = list(literals)
    n = len(literals)
    for seq in itertools.product([True,False], repeat=n):
        a = set(zip(literals, seq))
        if all([bool(disj.intersection(a)) for disj in cnf]):
            return True, a
 
    return False, None

def walkSat(form, max_flips = 1000):
        check = False
        for i in range(max_flips):
            if unsatisfied_clauses(form): return True, form
            while not check:
                clause = get_random_clause(form)
                if not is_clause_satisfiable(clause): 
                    check = True
            check = False
            var = get_random_variable(clause)
            change_Value(form, var)
        return False


def unsatisfied_clauses(form):
    for clause in form:
        if not is_clause_satisfiable(clause):
            return False
    
    return True



def get_random_clause(form):
    clause = choice(form)
    return clause


def get_random_variable(clause):
    lis=[]
    for item in clause:
        lis.append(item)
    
    var = choice(lis)

    return var
    



def is_clause_satisfiable(clause):
    for tuple in clause:
        if tuple[1] == True:
            return True
    
    return False


def change_Value(form, var):
    for clause in form:
        for tuple in clause:
            if tuple[0] == var[0]:
                if tuple[1]== False:
                    clause.remove(tuple)
                    clause.add((var[0], True))
                else:
                    clause.remove(tuple)
                    clause.add((var[0], False))
     

