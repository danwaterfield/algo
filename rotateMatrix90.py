
def rotateMatrix(m):
	return [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1,-1,-1)]


mat = [ [1, 2, 3, 4 ], 
        [5, 6, 7, 8 ], 
        [9, 10, 11, 12 ], 
        [13, 14, 15, 16 ] ]

print rotateMatrix(mat)