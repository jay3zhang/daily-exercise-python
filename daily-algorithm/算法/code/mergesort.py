# coding=utf-8

def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1
            

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

# alist = [54,26,93,17,77,31,44,55,20]
# print(alist)
# mergeSort(alist)
# print(alist)


def mergeSort2(alist):
    if len(alist)>1:
        
        lefthalf = [17, 26, 54, 93]
        righthalf = [20, 31, 44, 55, 77]

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):     #两个合并列表不断比较
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1
            print('1:',alist)
        
        #一个列表合并完成，另一个还有项未合并，
        #哪个列表未合并完就将该列表之后的项依次放入最终列表
        while i < len(lefthalf):    
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1
            print('2:',alist)

        while j < len(righthalf):   #既是一个循环也是一个判断
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
            print('3:',alist)
    print("*"*10)
    print("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20]
print(alist)
mergeSort2(alist)
print(alist)