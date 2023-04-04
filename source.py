
from itertools import permutations


class Student:
    def __init__(self, suspended : str,  group : int):
        self.suspended = suspended
        self.group = group
    def __repr__(self):
        return str(self.suspended) + ":" + str(self.group)

def BuildMatrix(students: list[Student]):
    amount_groups = 0
    for student in students:
        if student.group > amount_groups:
            amount_groups = student.group
    
    matrix = [[0 for i in range(amount_groups)], 
              [0 for i in range(amount_groups)]]
    
    for student in students:
        if student.suspended == "P":
            matrix[0][student.group-1] += 1
        else:
            matrix[1][student.group-1] += 1

    return matrix

def Solve(students: list[Student], k : int):
    matrix = BuildMatrix(students)
    amount_student_P = 0
    amount_student_R = 0
    for i in range(len(matrix[0])):
        amount_student_P += matrix[0][i]
        amount_student_R += matrix[1][i]

    amount_sets_P, rest_P = amount_student_P // k, amount_student_P % k
    amount_sets_R, rest_R = amount_student_R // k, amount_student_R % k

    if rest_P + rest_R < k:
        return amount_sets_P + amount_sets_R

    columns_to_v = []
    all_fluctuations = []

    for i in range(len(matrix[0])):
            if matrix[0][i] + matrix[1][i] >= k:
                columns_to_v.append([matrix[0][i], matrix[1][i]])
    
    if len(columns_to_v) == 0:
        return amount_sets_P + amount_sets_R

    for i in range(len(columns_to_v)):
        fluctuations_i = []
        for i in range(max(0, k - columns_to_v[i][1]), min(k, k - max(0, k - columns_to_v[i][0]))+1):
            fluctuations_i.append(i)
        all_fluctuations.append(fluctuations_i)
    
    list_of_posible_rest = [[0 for i in range(0,k)] for i in range(len(columns_to_v))]

    for i in range(len(all_fluctuations)):
        for j in range(len(all_fluctuations[i])):
            if all_fluctuations[i][j] == 0 or all_fluctuations[i][j] == k:
                continue
            list_of_posible_rest[i][all_fluctuations[i][j]] = 1
    
    for i in range(1,len(columns_to_v)):
        for j in range(0,k):
            if list_of_posible_rest[i-1][j] == 1:
                list_of_posible_rest[i][j] = 1
                for z in range(0,k):
                    if list_of_posible_rest[i][z] == 1:
                        new_rest = (z + j + 1) % k
                        if list_of_posible_rest[i][new_rest] == 0:
                            list_of_posible_rest[i][new_rest] = 1
    
    for i in range(0,k):
        if list_of_posible_rest[len(list_of_posible_rest)-1][i] == 1:
            if i >= (amount_student_P % k - len(students) % k + k) % k and i <= amount_student_P % k + 1:
                return amount_sets_P + amount_sets_R + 1
    
    return amount_sets_P + amount_sets_R
            
            

    


    
def Solve_bruto(students : list[Student], k : int):

    all_perm = permutations(students)

    max_groups = 0
    for perm in all_perm:
        count = 0
        
        for i in range(len(perm) // k):
            sub_list = perm[i*k : (i*k + k)]
            correct_subject_set = True
            correct_group_set = True

            for j in range(len(sub_list) - 1):
                if sub_list[j].suspended != sub_list[j+1].suspended:
                    correct_subject_set = False
                    break

            for j in range(len(sub_list) - 1):
                if sub_list[j].group != sub_list[j+1].group:
                    correct_group_set = False
                    break

            if correct_subject_set or correct_group_set: 
                count += 1

        max_groups = max(max_groups, count)

    return max_groups




            