def ch_board():
    row = int(input("Enter number of rows: "))
    column = int(input("Enter number of columns: "))

    matrix = []

    for i in range(row) :
        m =[]
        n =[]
        
        for j in range(column):
            m.append("$")
            m.append("*")
            n.append("*")
            n.append("$")

        matrix.append(m)
        matrix.append(n)
    
    for i in range(row):
        for j in range(column) :
            print(matrix[i][j],end="")
        print()
ch_board ()