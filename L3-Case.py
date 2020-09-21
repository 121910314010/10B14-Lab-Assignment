#Case
from array import *
n=int(input("Enter the your choice 1. Display the matrix, 2. Sum of the matrix, 3. Product of Sparse matrix,4.Transpose of matrix "))
if n==1:
    normalMatrix = [[1, 0, 0, 0],
                     [0, 2, 0, 0],
                     [0, 29, 3, 0],
                     [0, 0, 4, 4],
                     [5, 0, 0, 0]]
    for row in normalMatrix:
        for element in row:
            print(element, end=" ")
        print()

    sparseMatrix = []
    for i in range(len(normalMatrix)):
        for j in range(len(normalMatrix[0])):
            if normalMatrix[i][j] != 0:
                temp = []
                temp.append(i)
                temp.append(j)
                temp.append(normalMatrix[i][j])
                sparseMatrix.append(temp)

    print("\nSparse Matrix: ")
    for row in sparseMatrix:
        for element in row:
            print(element, end=" ")
        print()


elif n==2:

    normalMatrix1 = [[1, 0, 0, 0],
                     [0, 2, 0, 0],
                     [0, 29, 3, 0],
                     [0, 0, 4, 4],
                     [5, 0, 0, 0]]
    normalMatrix2 = [[2, 0, 0, 0],
                     [0, 5, 0, 0],
                     [0, 2, 3, 0],
                     [0, 0, 4, 4],
                     [5, 0, 0, 0]]
    print("normal matrix1")
    for row in normalMatrix1:
        for element in row:
            print(element, end=" ")
        print()
    print("normal matrix2")
    for row in normalMatrix2:
        for element in row:
            print(element, end=" ")
        print()

    sparseMatrix = []
    for i in range(len(normalMatrix1)):
        for j in range(len(normalMatrix1[0])):
            if normalMatrix1[i][j] != 0:
                temp = []
                temp.append(i)
                temp.append(j)
                temp.append(normalMatrix1[i][j])
                sparseMatrix.append(temp)

    sparseMatrix2 = []
    for i in range(len(normalMatrix1)):
        for j in range(len(normalMatrix1[0])):
            if normalMatrix2[i][j] != 0:
                temp = []
                temp.append(i)
                temp.append(j)
                temp.append(normalMatrix1[i][j])
                sparseMatrix2.append(temp)

    print("\nSparse Matrix1: ")
    for row in sparseMatrix:
        for element in row:
            print(element, end=" ")
        print()
    print("\nSparse Matrix2: ")
    for row in sparseMatrix2:
        for element in row:
            print(element, end=" ")
        print()
    print("Sum of sparse matrix")
    result = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0],
              [0, 0, 0],
              [0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
    for i in range(len(sparseMatrix)):
        # iterate through columns
        for j in range(len(sparseMatrix[0])):
            result[i][j] = sparseMatrix[i][j] + sparseMatrix2[i][j]
    print(result)

elif n==3:
    normalMatrix1 = [[1, 0, 0, 0],
                     [0, 2, 0, 0],
                     [0, 29, 3, 0],
                     [0, 0, 4, 4],
                     [5, 0, 0, 0]]
    normalMatrix2 = [[2, 0, 0, 0],
                     [0, 5, 0, 0],
                     [0, 2, 3, 0],
                     [0, 0, 4, 4],
                     [5, 0, 0, 0]]
    print("normal matrix1")
    for row in normalMatrix1:
        for element in row:
            print(element, end=" ")
        print()
    print("normal matrix2")
    for row in normalMatrix2:
        for element in row:
            print(element, end=" ")
        print()

    sparseMatrix = []
    for i in range(len(normalMatrix1)):
        for j in range(len(normalMatrix1[0])):
            if normalMatrix1[i][j] != 0:
                temp = []
                temp.append(i)
                temp.append(j)
                temp.append(normalMatrix1[i][j])
                sparseMatrix.append(temp)

    sparseMatrix2 = []
    for i in range(len(normalMatrix1)):
        for j in range(len(normalMatrix1[0])):
            if normalMatrix2[i][j] != 0:
                temp = []
                temp.append(i)
                temp.append(j)
                temp.append(normalMatrix1[i][j])
                sparseMatrix2.append(temp)

    print("\nSparse Matrix1: ")
    for row in sparseMatrix:
        for element in row:
            print(element, end=" ")
        print()
    print("\nSparse Matrix2: ")
    for row in sparseMatrix2:
        for element in row:
            print(element, end=" ")
        print()
    print("Product of sparse matrix")
    result = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0],
              [0, 0, 0],
              [0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
    for i in range(len(sparseMatrix)):
        # iterate through columns
        for j in range(len(sparseMatrix[0])):
            result[i][j] = sparseMatrix[i][j] * sparseMatrix2[i][j]
    print(result)

elif n==4:
    normalMatrix = [[12, 0, 0],
                    [0, 2, 0],
                    [0, 29, 0],
                    ]
    for row in normalMatrix:
        for element in row:
            print(element, end=" ")
        print()

    sparseMatrix = []
    for i in range(len(normalMatrix)):
        for j in range(len(normalMatrix[0])):
            if normalMatrix[i][j] != 0:
                temp = []
                temp.append(i)
                temp.append(j)
                temp.append(normalMatrix[i][j])
                sparseMatrix.append(temp)

    print("\nSparse Matrix: ")
    for row in sparseMatrix:
        for element in row:
            print(element, end=" ")
        print()

    B = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0],
         [0, 0, 0],
         [0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            B[i][j] = sparseMatrix[j][i]
    print("Result matrix is")
    for i in range(3):
        for j in range(3):
            print(B[i][j], " ", end='')
        print()

else:
    print("Enter the value from the choices given")
