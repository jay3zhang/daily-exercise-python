# 矩阵顺时针旋转90度

def transformImage1(self, mat, n):
    mat.reverse()
    return zip(*mat)

def transformImage2(self, mat, n):
    for layer in range(0,n/2):
        first = layer
        last = n-1-layer
        for i in range(first,last):
            # save top
            top = mat[first][i]
            
            # left->top
            mat[first][i] = mat[n-1-i][first]
            
            # bottom->left
            mat[n-1-i][first] = mat[last][n-1-i]
            
            # right->bottom
            mat[last][n-1-i] = mat[i][last]
            
            # top->right
            mat[i][last]= top
     
    return mat
    
##***********************************************
def showAsMatrix(mat):
    [print(i) for i in mat]

def rotate(seq):
    orig = list(seq)            # keep a copy of the original sequence
    STEP = END = -1             # access elements N..0 one-by-one
    r = range(len(seq[0])-1, END, STEP) # the length is fixed, calculate it only once
    for idx, _ in enumerate(seq):
        # list 0 consists of elements list[N][0], list[N-1][0], ..., list[0][0]
        # list 1 consists of elements list[N][1], list[N-1][1], ..., list[0][1], etc.
        seq[idx] = [orig[n][idx] for n in r]
    return seq

def rotate2(seq):
    import copy
    size = len(seq)
    matrix_new = copy.deepcopy(seq)
    for i in xrange(size):
        for j in reversed(range(size)):
            matrix_new[i][size-1-j] = seq[j][i]
    return matrix_new

def rotate3(seq):
    return zip(*seq[::-1])

if __name__ == '__main__':
    x = [ ['p00', 'p01', 'p02', 'p03'],
          ['p10', 'p11', 'p12', 'p13'],
          ['p20', 'p21', 'p22', 'p23'],
          ['p30', 'p31', 'p32', 'p33'] ]

    print('original matrix')
    showAsMatrix(x)
    y = rotate(x)
    print()
    print('matrix rotated 90 degrees right')
    showAsMatrix(y)
