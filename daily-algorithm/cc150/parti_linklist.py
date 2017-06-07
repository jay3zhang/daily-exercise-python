# coding=utf-8

#字符串分割，大的排后面

## 分割后原来数据顺序改变
def partition(linkedlist, x):
    if linkedlist.head != None:
        p1 = linkedlist.head
        p2 = linkedlist.head.next
        while p2 != None:
            if p2.value < x:    #将小数放到头部
                p1.next = p2.next
                p2.next = linkedlist.head
                linkedlist.head = p2
                p2 = p1.next
            else:
                p1 = p1.next
                p2 = p1.next
                
# partition(L, x)
# print L 

## 分割后数据顺序不变，要用的额外的两个链表

def partition(self, pHead, x):
    sHead = ListNode(0)
    lHead = ListNode(0)     #新建两个链表的头部
    small = sHead
    large = lHead
    
    while pHead:
        if pHead.val<x:
            small.next = pHead
            small = small.next
        else:
            large.next = pHead
            large = large.next
        pHead = pHead.next
        
    large.next = None
    samll.next = lHead.next     #两个链表合并
        
    return sHead.next
