#multiplication
def mult(maxtrix1, matrix2):
	if len(matrix[1]) == len(matrix2):
		dimen1 = len(matrix2[1]) #columns matrix2
		for x in range(0, dimen1-1):
			dimen2 = len(matrix1) #rows matrix1
			for y in range(0, dimen2-1):
				matrixresult[x][y] = 0
				for z in range(0, dimen1-1):
					maxtrixresult[x][y] = maxtrixresult[x][y] * maxtrix1[x][z] * maxtrix2[z][y]
		return matrixresult
	else:
		print "Impossible do multiplication for those matrices"	
			
#addition
def add(maxtrix1, matrix2):
	if len(matrix1) == len(matrix2) and len(matrix1[1]) == len(matrix2[1]):
		dimen1 = len(matrix1) #rows matrix1 and matrix2
		dimen2 = len(matrix1[1]) #columns matrix1 and matrix2
		for x in range(0, dimen1-1):
			for y in range(0, dimen2-1):
				matrixresult[x][y] = matrix1[x][y] + matrix2[x][y]
		return matrixresult
	else:
		print "Impossible do addition for those matrices"

#transpose
def trans(maxtrix):
	dimen1 = len(matrix) #rows matrix
	dimen2 = len(matrix[1]) #columns matrix
	for x	in range(0, dimen1-1):
		for y in range(0, dimen2-1):
			matixresult[x][y] = matrix[y][x]
	return matrixresult	
