
# 快排，以列表第一项为对比值

def quicksort(alist):
    quicksortHelper(alist,0,len(alist)-1)
    
def quicksortHelper(alist,start,end):
    if start<end:
        # 对目前列表排序，返回区分点位置
        splitindex = realsort(alist,start,end)
        # 对左半部分排序，需要传入左半部分的开始，结束索引
        quicksortHelper(alist,start,splitindex-1)
        # 对右半部分排序
        quicksortHelper(alist,splitindex+1,end)
        
def realsort(alist,start,end):
    print('start:',start,'\t end:',end)
    diffvalue = alist[start]    #选取第一个值为对比值
    '''
    num1 = alist[start]
    num2 = alist[end]
    num3 = alist[start+(end-start)/2]
    temp = [num1,num2,num3]
    #1
    temp.remove(max(temp))
    temp.remove(min(temp))
    diffvalue = temp.pop()
    #2
    for i in temp:
    if i!=max(temp) and i!=min(temp):
        diffvalue =i
    '''
    
    leftmark = start+1
    rightmark = end
    done = False
    
    while not done:
        # leftmark与rightmark的比较要放在前面，否则会出现数组越界（先执行前面的表达式）
        while leftmark <= rightmark and alist[leftmark] <= diffvalue:
            leftmark += 1   # 找到左侧大于对比值的位置
            
        while rightmark >= leftmark and alist[rightmark] >= diffvalue:
            rightmark -= 1  ## 找到右侧小于对比值的位置
            
        if rightmark < leftmark:    # 右标记小于左标记时，大小区分完成
            done = True
        else:               #将右侧的小值与左侧的大值交换
            temp = alist[leftmark]      
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp
            print(alist)
    
    # 所有交换都完成，将对比值放入区分点位置
    alist[start] = alist[rightmark]
    alist[rightmark] = diffvalue
    print(alist)
    
    return rightmark
            
# alist = [31,26,93,17,77,54,44,55,20]
# quicksort(alist)
# print(alist)

test=[54,35,48,36,27,12,44,44,8,14,26,17,28]
quicksort(test)
print(test)
    
    
