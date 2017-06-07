# 矩阵顺时针旋转90度

def showAsMatrix(mat):
    [print(i) for i in mat]

def transformImage1(mat, n):
    mat.reverse()   #颠倒行的顺序
    return zip(*mat)

def transformImage2(mat, n):
    for layer in range(0,n//2):
        print('layer:',layer)
        first = layer
        last = n-1-layer
        for i in range(first,last):     #循环，先外圈后内圈
            print('i:',i)
            # save top
            top = mat[first][i]
   
            # left->top
            mat[first][i] = mat[n-1-i][first]
            print('left->top:')
            showAsMatrix(mat)
            # bottom->left
            mat[n-1-i][first] = mat[last][n-1-i]
            print('bottom->left:')
            showAsMatrix(mat)
            # right->bottom
            mat[last][n-1-i] = mat[i][last]
            print('right->bottom:')
            showAsMatrix(mat)
            # top->right
            mat[i][last]= top
            print('top->right:')
            showAsMatrix(mat)
            print('-'*10)
    return mat
    
    
# matx = [ ['p00', 'p01', 'p02', 'p03'],
          # ['p10', 'p11', 'p12', 'p13'],
          # ['p20', 'p21', 'p22', 'p23'],
          # ['p30', 'p31', 'p32', 'p33'] ]    
# tmp = transformImage2(matx,4)
# print("*"*10)
# showAsMatrix(tmp)
##***********************************************


def rotate(seq):
    orig = list(seq)            # 复制了原矩阵，用了缓存矩阵
    STEP = END = -1             # access elements N..0 one-by-one
    r = range(len(seq[0])-1, END, STEP) # the length is fixed, calculate it only once
    for idx, _ in enumerate(seq):
        # list 0 consists of elements list[N][0], list[N-1][0], ..., list[0][0]
        # list 1 consists of elements list[N][1], list[N-1][1], ..., list[0][1], etc.
        seq[idx] = [orig[n][idx] for n in r]    #每一行等于每一列
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

# if __name__ == '__main__':
    # x = [ ['p00', 'p01', 'p02', 'p03'],
          # ['p10', 'p11', 'p12', 'p13'],
          # ['p20', 'p21', 'p22', 'p23'],
          # ['p30', 'p31', 'p32', 'p33'] ]

    # print('original matrix')
    # showAsMatrix(x)
    # y = rotate(x)
    # print()
    # print('matrix rotated 90 degrees right')
    # showAsMatrix(y)
