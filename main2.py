#multiplication
def mult(matrix1, matrix2):
	if len(matrix1[1]) == len(matrix2):
		dimen1 = len(matrix2[1]) #columns matrix2
		dimen2 = len(matrix1) #rows matrix1
		matrixresult = [ [ 0 for i in range(dimen1) ] for j in range(dimen2) ]
		for x in range(0, dimen1):
			for y in range(0, dimen2):
				matrixresult[x][y] = 0
				for z in range(0, dimen1):
					matrixresult[x][y] = matrixresult[x][y] + (matrix1[x][z] * matrix2[z][y])
		return matrixresult
	else:
		return "Impossible do multiplication for those matrices"	
			
#addition
def add(matrix1, matrix2):
	if len(matrix1) == len(matrix2) and len(matrix1[1]) == len(matrix2[1]):
		dimen1 = len(matrix1) #rows matrix1 and matrix2
		dimen2 = len(matrix1[1]) #columns matrix1 and matrix2
		matrixresult = [ [ 0 for i in range(dimen1) ] for j in range(dimen2) ]
		for x in range(0, dimen1):
			for y in range(0, dimen2):
				matrixresult[x][y] = matrix1[x][y] + matrix2[x][y]
		return matrixresult
	else:
		return "Impossible do addition for those matrices"

#transpose
def trans(matrix):
	dimen1 = len(matrix) #rows matrix
	dimen2 = len(matrix[1]) #columns matrix
	matrixresult = [ [ 0 for i in range(dimen1) ] for j in range(dimen2) ]
	for x	in range(0, dimen1):
		for y in range(0, dimen2):
			matrixresult[x][y] = matrix[y][x]
	return matrixresult	
	
	
Matrix = [[1,2],[3,4]]
Matrix1 = [[1,2],[3,4]]

print mult(Matrix, Matrix1)

print add(Matrix, Matrix1)

print trans(Matrix)