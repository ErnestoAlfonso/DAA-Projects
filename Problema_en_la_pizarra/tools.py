# Python program to find
# maximal Bipartite matching.

class Graph:
	def __init__(self,graph):
		
		# residual graph
		self.graph = graph
		self.rows = len(graph)
		self.columns = len(graph[0])

	# A DFS based recursive function
	# that returns true if a matching
	# for vertex u is possible
	def bpm(self, u, matchR, seen):

		for v in range(self.columns):

			# If row u is interested
			# in column v and v is not seen
			if self.graph[u][v] and seen[v] == False:
				
				# Mark v as visited
				seen[v] = True

				'''If column 'v' is not assigned to
				an row OR previously assigned
				row for column v (which is matchR[v])
				has an alternate column available.
				Since v is marked as visited in the
				above line, matchR[v] in the following
				recursive call will not get column 'v' again'''
				if matchR[v] == -1 or self.bpm(matchR[v],
											matchR, seen):
					matchR[v] = u
					return True
		return False

	# Returns maximum number of matching
	def maxBPM(self):
		'''An array to keep track of the
		rows assigned to columns.
		The value of matchR[i] is the
		row number assigned to column i,
		the value -1 indicates nobody is assigned.'''
		matchR = [-1] * self.columns
		
		# Count of columns assigned to rows
		result = 0
		for i in range(self.rows):
			
			# Mark all columns as not seen for next row.
			seen = [False] * self.columns
			
			# Find if the row 'u' can get a column
			if self.bpm(i, matchR, seen):
				result += 1
		return result

a = [1,2,3,4,5,6,7]
a[2:5] = [0,0,0]
print(a)
