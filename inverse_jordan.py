def augmented_matrix(mat):
    n = len(mat)
    identity = [[1 if i==j else 0 for j in range(n)] for i in range(n)];
    print(identity);
    
    aug_mat= [mat[i] + identity[i] for i in range(n)];
    print(aug_mat);
    
    for i in range(n):
        max_row = i;
        for key in range(i,n):
            if aug_mat[max_row][i] < aug_mat[key][i]:
                max_row = key;
        
        aug_mat[i] , aug_mat[max_row] = aug_mat[max_row] , aug_mat[i];
        
        pivot = aug_mat[i][i]
        if pivot == 0:
            raise ValueError("Matrix is singular and cannot be inverted.")
        
        for j in range(2 * n):
            aug_mat[i][j] /= pivot
            
        for j in range(i+1,n):
            factor = aug_mat[j][i] / aug_mat[i][i];
            for k in range(i,2*n):
                aug_mat[j][k] -= factor * aug_mat[i][k];
                
    print(aug_mat)
mat = [
        [1,2,3],
        [4,5,6],
        [3,2,1]
    ]
augmented_matrix(mat);
    
    
    
    
    
    
