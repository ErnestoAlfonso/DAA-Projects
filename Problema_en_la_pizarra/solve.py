from tools import BiGraph
from generator import generate

def board_problem_solve(n, tuples : list):
    graph = [[0] * n for i in range(n)]
    for t in tuples:
        for i in range(t[0]-1, t[2]):
            graph[i][t[1]-1 : t[3]] = [1 for i in range(t[1]-1,t[3])]
    
    BG = BiGraph(graph)
    return BG.maxBPM()

tuples = generate(50, 5)

print(board_problem_solve(50, tuples))