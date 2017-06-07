# coding=utf-8

def plusAB(self, a, b):
    sum = ListNode(0)
    stemp = sum
    carry = 0
    while a and b:
        singleSum = (a.val+b.val+carry)%10
        carry = (a.val+b.val+carry)//10
        stemp.next = ListNode(singleSum)
        stemp = stemp.next
        a,b = a.next,b.next
     
    last = a if a else b
    while last:
        singleSum = (last.val+carry)%10
        carry = (last.val+carry)//10
        stemp.next = ListNode(singleSum)
        last,stemp = last.next,stemp.next
         
    if carry:
        stemp.next = ListNode(carry)
        stemp = stemp.next
    stemp.next = None
     
    return sum.next