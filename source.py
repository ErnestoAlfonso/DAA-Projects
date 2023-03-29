
class Student:
    def __init__(self, suspended : str,  group : int):
        self.suspended = suspended
        self.group = group
    def __repr__(self):
        return str(self.suspended) + ":" + str(self.group)

def group(seq: list,  k : int):
    if len(seq) == 0:
        return seq
    susp_grouped = []
    i = 0
    k_group = []
    for stud_r in seq:
        if i < k:
            k_group.append(stud_r)
        else:
            k1=k_group.copy()
            susp_grouped.append(k1)
            k_group.clear()
            k_group.append(stud_r)
            i = 0
        i += 1
    susp_grouped.append(k_group)
    return susp_grouped

def get_amount_rest(susp_grouped : list, k):
    if len(susp_grouped) == 0:
        return 0
    a = len(susp_grouped[len(susp_grouped)-1])
    return a if a<k else 0


def count_stud_per_group(students : list[Student]):
    amounts_per_group : dict = {}
    for stud in students:
        amounts_per_group[stud.group] = 0
    for stud in students:
        amounts_per_group[stud.group] +=1
    return amounts_per_group

def create_last_group(amount_poo_group : dict, amount_rec_group : dict, amount_stud_per_group : dict, amount_rest_poo, amount_rest_rec, k):
    for group in amount_stud_per_group:
        try:
            if min(amount_poo_group[group], amount_rest_poo) + min(amount_rec_group[group], amount_rest_rec) >= k:
                return True
        except:
            continue
    
    return False
    



def Solve(students : list[Student], k : int):
    amountOfstud_per_group = count_stud_per_group(students)
    susp_rec = []
    susp_poo = []

    for stud in students:
        if stud.suspended == "P":
            susp_poo.append(stud)
        else:
            susp_rec.append(stud)
    
    amountOfstud_per_group_rec = count_stud_per_group(susp_rec)
    amountOfstud_per_group_poo = count_stud_per_group(susp_poo)
    
    susp_rec_grouped = group(susp_rec, k)
    susp_poo_grouped = group(susp_poo, k)
        
    if (len(susp_rec_grouped) == 0 or len(susp_rec_grouped[len(susp_rec_grouped) - 1]) == k) and (len(susp_poo_grouped)==0 or len(susp_poo_grouped[len(susp_poo_grouped) - 1]) == k):
        return len(susp_poo_grouped) + len(susp_rec_grouped)
    else:
        amount_rest_poo = get_amount_rest(susp_poo_grouped,k)
        amount_rest_rec = get_amount_rest(susp_rec_grouped,k)

        rest = 2 if amount_rest_rec > 0 and amount_rest_poo > 0 else 1

        if amount_rest_rec + amount_rest_poo < k:
            return len(susp_rec_grouped) + len(susp_poo_grouped) - rest
        elif create_last_group(amountOfstud_per_group_poo,amountOfstud_per_group_rec, amountOfstud_per_group, amount_rest_poo, amount_rest_rec,k):
            return len(susp_poo_grouped) + len(susp_rec_grouped) - 1
        else:
            return len(susp_poo_grouped) + len(susp_rec_grouped) - 2 
    
    return 0



            