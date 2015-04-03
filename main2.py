#multiplication
def mult(matrix1, matrix2):
	if len(matrix1[1]) == len(matrix2):
		print "Multiplication:"
		matrixresult = [[0 for i in range(len(matrix2[1]))] for j in range(len(matrix1))]
		for x in range(0, len(matrix1)):
			for y in range(0, len(matrix2[1])):
				matrixresult[x][y] = 0
				for z in range(0, len(matrix2)):
					matrixresult[x][y] = matrixresult[x][y] + (matrix1[x][z] * matrix2[z][y])
		return matrixresult
	else:
		return "Impossible do multiplication for those matrices"	
			
#addition
def add(matrix1, matrix2):
	if len(matrix1) == len(matrix2) and len(matrix1[1]) == len(matrix2[1]):
		print "Addition:"
		matrixresult = [[0 for i in range(len(matrix1[1])) ] for j in range(len(matrix1))]
		for x in range(0, len(matrix1)):
			for y in range(0, len(matrix1[1])):
				matrixresult[x][y] = matrix1[x][y] + matrix2[x][y]
		return matrixresult
	else:
		return "Impossible do addition for those matrices"

#transpose
def trans(matrix):
	print "Transpose:"
	matrixresult = [[0 for i in range(len(matrix)) ] for j in range(len(matrix[1]))]
	for x in range(0, len(matrix[1])):
		for y in range(0, len(matrix)):
			matrixresult[x][y] = matrix[y][x]
	return matrixresult	
	
#test
Matrix1 = [[1,2,3],[4,5,6]]
Matrix2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Matrix3 = [[1,2,3],[4,5,6],[7,8,9]]
Matrix4 = [[1,2,3],[4,5,6]]

# print mult(Matrix1, Matrix2)

# print add(Matrix3, Matrix3)

# print trans(Matrix4)
