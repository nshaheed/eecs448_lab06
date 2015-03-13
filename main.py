# shamelessly copied from stackoverflow
def checkEqual(iterator):
    return len(set(iterator)) <= 1

file1 = open("matrix1.csv","r")
file2 = open("matrix2.csv","r")

matStr1 = []
matStr2 = []
matFlo1 = []
matFlo2 = []
counter = 0;

# print matStr

# read file
for line in file1:
    matStr1.insert(counter, line.split(','))
    counter = counter + 1

counter = 0
for line in file2:
    matStr2.insert(counter, line.split(','))
    counter = counter + 1



# convert contents of file to floats
for i in range(0,len(matStr1)):
    temp = map(float, matStr1[i])
    matFlo1.insert(i, temp)

for i in range(0,len(matStr2)):
    temp = map(float, matStr2[i])
    matFlo2.insert(i, temp)


# check if this is a proper matrix
length1 = map(len, matFlo1)
length2 = map(len, matFlo2)
# print length

if (checkEqual(length)):
    # do stuff because it's a matrix
    print("it worked")
else:
    # it wasn't a matrix
    print("That file is not a matrix\n")


