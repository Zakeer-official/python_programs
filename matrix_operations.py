l1 = [[1,2,3],[4,5,6],[7,8,9]]
l2 = [[1,2,3],[4,5,6],[7,8,9]]

#matrix addition
x = []
for i in range(len(l1)):
    x1 = []
    for j in range(len(l1[0])):
        y = l1[i][j]+l2[i][j]
        x1.append(y)
    x.append(x1.copy())
    x1.clear()
    
print("Matrix addition: ",x)

#matrix subtraction

x = []
for i in range(len(l1)):
    x1 = []
    for j in range(len(l1[0])):
        y = l1[i][j]-l2[i][j]
        x1.append(y)
    x.append(x1.copy())
    x1.clear()
    
print("Matrix subtraction: ",x)

#matrix multiplication

x = []
for i in range(len(l1)):
    x1 = []
    for j in range(len(l1[0])):
        y = 0
        for k in range(len(l1[0])):
            y += l1[i][k]*l2[k][j]
        x1.append(y)
    x.append(x1.copy())
    x1.clear()
    
print("Matrix multiplication: ",x)
