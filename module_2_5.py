def get_matrix(n, m, value):
    matrix=[]
    for i in range(n):
        b=[]
        for j in range(m):
            b.append(value)
        matrix.append(b)
    return matrix
print(get_matrix(23,25,24))
