row0 = input("Enter number of rows: ")

while True:
    if row0 != "" and row0 != "0":
        col0 = input("Enter number of cols: ")
        while True:
            if col0 != "" and col0 != "0":
                rows_a = int(row0)
                column_a = int(col0)
                print("Matrix 1")
                matrix_a = [[int(input("Enter number [" + str(i + 1) + "][" + str(j + 1) + "]: ")) for j in range(column_a)] for i in range(rows_a)]

                print("First Matrix 1 is: ")
                for n in matrix_a:
                    print(n)

                print("Matrix 2")
                matrix_b = [[int(input("Enter number [" + str(i + 1) + "][" + str(j + 1) + "]: ")) for j in range(rows_a)] for i in range(column_a)]
                
                print("First Matrix 2 is: ")
                for n in matrix_b:
                    print(n)
    
                result = [[0 for i in range(rows_a)] for i in range(rows_a)]

                for i in range(len(matrix_a)):
                    for j in range(len(matrix_b[0])):
                        for k in range(len(matrix_b)):
                            result [i][j]+=matrix_a[i][k]*matrix_b[k][j]
                print("\nMatrix 1 x Matrix 2 is: ")
                for r in result:
                    print(r)
                break
            col0 = input("Enter number of cols: ")
        #break
    row0 = input("Enter number of rows: ")