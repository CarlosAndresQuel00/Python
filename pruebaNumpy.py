import numpy as np

ci = input("Enter CI.: ")
dimentions = (100, 100)
matrix = np.full(dimentions, ci)
print(matrix)
print("1.- Sum and multiply column")
print("2.- Sum and multiply row")
print("3.- Sum and multiply diagonal")
print("0.- Exit")
num = int(input("Enter an option: "))

while num != 0:
    if num == 1:
        col = int(input("Enter column number: "))

        value_copyCol = matrix[0][col - 1]
        value_copyCol1 = matrix[1][col - 1]
        matrixSumCol = list(map(int, value_copyCol))
        newMatrixCol = np.copy(matrixSumCol)
        matrixSumCol1 = list(map(int, value_copyCol1))
        newMatrixCol1 = np.copy(matrixSumCol)
        sumElementsCol = newMatrixCol.sum()
        mulElementsCol = np.dot(newMatrixCol, newMatrixCol1)

        print("The sum of the elements of the column is: " + str(sumElementsCol))
        print("The multiply of the elements of the column is: " + str(mulElementsCol))
    elif num == 2:
        row = int(input("Enter row number: "))

        value_copyRow = matrix[row - 1][0]
        value_copyRow1 = matrix[1][col - 1]
        matrixSumRow = list(map(int, value_copyRow))
        newMatrixRow = np.copy(matrixSumRow)
        matrixSumRow1 = list(map(int, value_copyRow1))
        newMatrixRow1 = np.copy(matrixSumRow1)
        sumElementsRow = newMatrixRow.sum()
        mulElementsRow = np.dot(newMatrixRow, newMatrixRow1)

        print("The sum of the elements of the row is: " + str(sumElementsRow))
        print("The multiply of the elements of the row is: " + str(mulElementsRow))
    elif num == 3:
        value_copyDiag = matrix[0][0]
        value_copyDiag1 = matrix[1][1]
        matrixSumDiag0 = list(map(int, value_copyDiag))
        newMatrixDiag0 = np.copy(matrixSumDiag0)
        matrixSumDiag1 = list(map(int, value_copyDiag1))
        newMatrixDiag1 = np.copy(matrixSumDiag1)
        sumElementsDiag = newMatrixDiag0.sum() + newMatrixDiag1.sum()
        mulElementsDiag = np.dot(newMatrixDiag0, newMatrixDiag1)

        print("The sum of the elements of the diagonal is: " + str(sumElementsDiag))
        print("The multiply of the elements of the diagonal is: " + str(mulElementsDiag))
    print("1.- Sum and multiply column")
    print("2.- Sum and multiply row")
    print("3.- Sum and multiply diagonal")
    print("0.- Exit")
    num = int(input("Enter an option: "))
print("Bye-B")