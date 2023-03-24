import dataclasses

@dataclasses
class Student:
    suspended : str
    group : int

def group(seq: list,  k : int):
    susp_grouped = []
    i = 0
    k_group = []
    for stud_r in seq:
        if i < k:
            k_group.append(stud_r)
        else:
            susp_grouped.append(k_group)
            k_group.clear()
            i = 0
        i += 1
    susp_grouped.append(k_group)
    return susp_grouped

def get_elem_list(susp_grouped : list, susp_rest : list):
    for i in range(len(susp_grouped[len(susp_grouped)-1])):
        susp_rest.append(susp_grouped[len(susp_grouped)-1][i])


def count_stud_per_group(students : list[Student]):
    amounts_per_group = {}
    for stud in students:
        amounts_per_group[stud.group] += 1
    return amounts_per_group

def create_last_group():
    # TODO: create def to find the last group if is posible
    pass



def Solve(students : list[Student], k : int):
    amountOfstud_per_group = count_stud_per_group(students)
    susp_rec = []
    susp_poo = []
    susp_rest = []
    gthan_k = []

    for stud in students:
        if stud.suspended == "POO":
            susp_poo.append(stud)
        else:
            susp_rec.append(stud)
    
    susp_rec_grouped = group(susp_rec, k)
    susp_poo_grouped = group(susp_poo, k)

    if len(susp_rec_grouped[len(susp_rec_grouped) - 1]) == 0 and len(susp_poo_grouped[len(susp_poo_grouped) - 1]) == 0:
        return susp_poo_grouped + susp_rec_grouped
    else:
        get_elem_list(susp_poo_grouped, susp_rest)
        get_elem_list(susp_rec_grouped, susp_rest)

        if len(susp_rest) < k:
            return susp_poo_grouped + susp_rec_grouped
        else:
            create_last_group() # TODO: complete
        return susp_poo_grouped + susp_rec_grouped



            