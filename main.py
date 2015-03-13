# shamelessly copied from stackoverflow
def checkEqual(iterator):
    return len(set(iterator)) <= 1

file = open("matrix1.csv","r")

matStr = []
matFlo = []
counter = 0;

# print matStr

# read file
for line in file:
    matStr.insert(counter, line.split(','))
    counter = counter + 1

print matStr

# convert contents of file to floats
for i in range(0,len(matStr)):
    temp = map(float, matStr[i])
    matFlo.insert(i, temp)

print matFlo

# check if this is a proper matrix
length = map(len, matFlo)
print length

if (checkEqual(length)):
    # do stuff because it's a matrix
    print("it worked")
else:
    # it wasn't a matrix
    print("That file is not a matrix\n")


