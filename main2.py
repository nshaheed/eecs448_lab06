#multiplication
def multiplication(maxtrix1, matrix2, dimen):
	for x in range(0, dimen-1):
		for y in range(0, dimen-1):
			matrixresult[x][y] = 0
			for z in range(0, dimen-1):
				maxtrixresult[x][y] = maxtrixresult[x][y] * maxtrix1[x][z] * maxtrix2[z][y]
	return matrixresult
			
#addition
def multiplication(maxtrix1, matrix2, dimen):
	for x in range(0, dimen-1):
		for y in range(0, dimen-1):
			matrixresult[x][y] = matrix1[x][y] + matrix2[x][y]
	return matrixresult

#transpose
def multiplication(maxtrix1, matrix2, dimen):
	for x	in range(0, dimen-1):
		for y in range(0, dimen-1):
			matixresult[x][y] = matrix[y][x]
	return matrixresult	
