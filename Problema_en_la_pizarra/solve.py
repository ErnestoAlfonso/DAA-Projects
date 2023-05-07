from tools import BiGraph

def board_problem_solve(n, tuples : list):
    graph = [[0] * n for i in range(n)]
    for t in tuples:
        for i in range(t[0]-1, t[2]):
            graph[i][t[1]-1 : t[3]] = [1 for i in range(t[1]-1,t[3])]
    
    BG = BiGraph(graph)
    return BG.maxBPM()

print(board_problem_solve(7, [(2,1,2,1), (4,2,4,3), (2,5,2,5), (2,3,5,3), (1,2,1,2), (3,2,5,3)]))