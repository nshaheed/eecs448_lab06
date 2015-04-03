import main2

# shamelessly copied from stackoverflow
def checkEqual(iterator):
    return len(set(iterator)) <= 1

def readFile(fileVal):
    elements = []
    counter = 0;
    for line in fileVal:
        elements.insert(counter, line.split(','))
        counter = counter + 1
    return elements

def toFloat(strLst):
    elements = []
    for i in range(0,len(strLst)):
        temp = map(float, strLst[i])
        elements.insert(i, temp)
    return elements

file1 = open("matrix1.csv","r")
file2 = open("matrix2.csv","r")
file3 = open("matrix3.csv","r")
file4 = open("matrix4.csv","r")

matStr1 = []
matStr2 = []
matStr3 = []
matStr4 = []
matFlo1 = []
matFlo2 = []
matFlo3 = []
matFlo4 = []

# read files
matStr1 = readFile(file1)
matStr2 = readFile(file2)
matStr3 = readFile(file3)
matStr4 = readFile(file4)

# convert contents of file to floats
matFlo1 = toFloat(matStr1)
matFlo2 = toFloat(matStr2)
matFlo3 = toFloat(matStr3)
matFlo4 = toFloat(matStr4)

# check if this is a proper matrix
length1 = map(len, matFlo1)
length2 = map(len, matFlo2)
length3 = map(len, matFlo3)
length4 = map(len, matFlo4)


if checkEqual(length1) and checkEqual(length2) and checkEqual(length3) and checkEqual(length4):
    print(main2.mult(matFlo1,matFlo2))

    print(main2.add(matFlo3,matFlo4))

    print(main2.trans(matFlo1))
else: 
    print("One of the files is not a matrix")
