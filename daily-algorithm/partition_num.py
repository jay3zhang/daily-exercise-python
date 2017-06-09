# 将奇数放到偶数前面
# 保持相对顺序

# 使用额外空间
def reOrderArray(array):
        # write code here
        lo = []
        le = []
        for d in array:
            if d % 2 == 1:
                lo.append(d)
            else:
                le.append(d)
        return lo + le
# 不使用额外空间
def reOrderArray(array):
        # write code here
        if not array:
            return []
        # 不需要额外空间
       	for i in range(0,len(array)):
            for j in range(len(array)-1,i,-1):
                if array[j-1]%2 ==0 and array[j]%2==1:
                    temp = array[j-1]
                    array[j-1] = array[j]
                    array[j] = temp
        return array