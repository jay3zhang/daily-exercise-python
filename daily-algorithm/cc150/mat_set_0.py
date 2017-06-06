# coding=utf-8

# 传入一个矩阵，将矩阵中0所在的行和列都置为0
# for example
# 输入：[[1,2,3],[0,1,2],[0,0,1]]
# 返回：[[0,0,3],[0,0,0],[0,0,0]]

def zeroProcess(self,mat):
    print(mat)
    n=len(mat)   #行
    m=len(mat[0])    #列

    columnstozero=[]    #记录set为0的列
    rowstozero=[]
    for rowcount,row in enumerate(mat):
        for cellcount, cell in enumerate(row):  #cellcount等于cell所处的列
            if cell == 0:
                columnstozero.append(cellcount)     #记住0所在的列
                rowstozero.append(rowcount)
    for rownum in rowstozero:
        mat[rownum]=[0]*m
        # newRow=[]
        # for x in range(0,m):
            # newRow.append(0)
        # mat[rownum]=newRow
        
    for colnum in columnstozero:
        for row in mat:     #每一行的该列为0
            row[colnum]=0
            
    print("*"*10)
    print(mat)
                     
            
zeroProcess([[1,2,3],[4,5,0],[7,8,9],[0,11,12]])
