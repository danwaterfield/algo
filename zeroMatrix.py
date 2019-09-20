#1.8 in cracking the coding interview, understood the pseudocode, struggled with syntax.
#task: if element in m*n matrix == 0, return matrix with cols, rows of element[0] as 0

def zeroMatrix(matrix):
	m = len(matrix)
	n = len(matrix[0])
	rows = []
	cols = []

	for x in range(m):
		for y in range(n):
			if matrix[x][y] == 0:
				rows.append(x)
				cols.append(y)

	for row in rows:
		nullify_row(matrix, row)
	for col in cols: 
		nullify_col(matrix, col)

	return matrix


def nullify_row(matrix, row):
	for i in range(len(matrix[0])):
		matrix[row][i] = 0


def nullify_col(matrix, col):
	for i in range(len(matrix)):
		matrix[i][col] = 0


mat = [ [1, 2, 3, 4 ], 
        [5, 6, 7, 8 ], 
        [9, 10, 0, 12 ], 
        [13, 14, 15, 16 ] ]

print zeroMatrix(mat)