def determinant(matrix):
    
    mat = [row[:] for row in matrix]
    n = len(mat)
    
    for i in range(n):
        row = i;
        # max_key = -1;
        max_row = i;
        for key in range(i,n):
            if mat[max_row][i] < mat[key][i]:
                max_row = key;
        # max_row = max(range(i, n), key=lambda r: abs(mat[r][i]))
        mat[i], mat[max_row] = mat[max_row], mat[i]\
        
        if mat[i][i] == 0:
            return 0
        
        for j in range(i + 1, n):
            factor = mat[j][i] / mat[i][i]
            for k in range(i, n):
                mat[j][k] -= factor * mat[i][k]
    
    det = 1
    for i in range(n):
        det *= mat[i][i]
    
    return det

# Example usage
matrix = [
    [4, 3, 1],
    [6, 5, 2],
    [1, 2, 3]
]

print("Determinant:", determinant(matrix))
