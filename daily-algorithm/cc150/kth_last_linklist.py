# coding=utf-8

# 查找链表的倒数第k个节点

def FindKthToTail(self, head, k):   #传入头结点
    if k<=0:    #倒数是从1开始数的，所有k=0也是None
        return None
    
    if not head:
        return None
    front = head
    later = head
    for i in range(0,k-1):  #倒数从1开始数，所以倒数第k个节点距离尾部k-1
        if front.next != None:
            front = front.next
        else:
            return None
         
    while front.next != None:
        front = front.next
        later = later.next
         
    return later
    