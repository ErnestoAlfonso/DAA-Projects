from tools import Graph

def board_problem_solve(n, tuples : list):
    graph = [[0] * n for i in range(n)]
    for t in tuples:
        for i in range(t[0]-1, t[2]):
            graph[i][t[1]-1 : t[3]] = [1 for i in range(t[1]-1,t[3])]
    
    BG = Graph(graph)
    return BG.maxBPM()

print(board_problem_solve(4, [(1,1,1,2), (2,1,2,1), (2,3,3,3)]))