# Python program to find
# maximal Bipartite matching.

class BiGraph:
	def __init__(self,graph):
		self.graph = graph
		self.rows = len(graph)
		self.columns = len(graph[0])

	def bpm(self, u, matchR, seen):
		for v in range(self.columns):
			if self.graph[u][v] and seen[v] == False:				
				seen[v] = True

			if matchR[v] == -1 or self.bpm(matchR[v],
											matchR, seen):
					matchR[v] = u
					return True
		return False

	def maxBPM(self):
		matchR = [-1] * self.columns
		
		result = 0
		for i in range(self.rows):
			
			seen = [False] * self.columns
			
			if self.bpm(i, matchR, seen):
				result += 1
		return result

