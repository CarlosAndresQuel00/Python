import numpy as nupy

row0 = input("Enter number of rows (\"Enter\" to exit): ")

while True:
    if row0 == "":
        break
    elif row0 != "" and row0 != "0":
        col0 = input("Enter number of cols (\"Enter\" to exit): ")
        while True:
            if col0 == "":
                exit()
            elif col0 != "" and col0 != "0":
                rows_a = int(row0)
                column_a = int(col0)
                print("Matrix 1")
                arrayNumpy1 = nupy.array([[int(input("Enter number [" + str(i + 1) + "][" + str(j + 1) + "]: ")) for j in range(column_a)] for i in range(rows_a)])
                print("First Matrix 1 is: ")
                print(arrayNumpy1)
                print("Matrix 2")
                arrayNumpy2 = nupy.array([[int(input("Enter number [" + str(i + 1) + "][" + str(j + 1) + "]: ")) for j in range(rows_a)] for i in range(column_a)])
                print("First Matrix 2 is: ")
                print(arrayNumpy2)
                result = nupy.dot(arrayNumpy1, arrayNumpy2)
                print("\nMatrix 1 x Matrix 2 is: ")
                print(result)
                break
            col0 = input("Enter number of cols (\"Enter\" to exit): ")
    row0 = input("Enter number of rows (\"Enter\" to exit): ")