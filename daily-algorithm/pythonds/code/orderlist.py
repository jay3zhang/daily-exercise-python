# coding=utf-8

# 有序列表

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class OrderList:
    def __init__(self):
        self.head = None
    
    def add(self,item):
        current = self.head
        previous = None
        stop = False
        while not stop and current != None:
            if current.data > item:
                stop = True
            else:
                previous = current
                current = current.next
                
        # stop为True以后 
        temp = Node(item)
        if previous==None:  #item在队首
            self.head = temp
        else:
            previous.next=temp
        temp.next = current
    
    def isEmpty(self):
        return self.head == None
        
    def search(self,item):  #搜索是否在列表中
        current = self.head
        Found = False
        stop = False
        while current!=None and not Found and not stop:
            if current.data == item:
                Found = True
            elif current.data > item:
                stop = True
            else:
                current = current.next
        return Found
    
    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.data == item:
                found = True
            else:
                previous = current
                current = current.next
                
        # found为True以后      
        if previous==None:  #item在队首
            self.head = current.next
        else:
            previous.next=current.next
  
      
    def size(self):
        current = self.head
        count =0
        while current!= None:
            count = count +1
            current = current.next
        return count   

    
    def index(self,item):
        current = self.head
        pos =0
        while current!= None:
            if current.data==item:
                return pos
            else:
                pos = pos +1
                current = current.next
        return None
        
    # 有序列表不需要append(),insert()函数，add()函数包括了相关功能
    
    def pop(self,pos=0):
        current = self.head
        index = 0
        item = None
        while current!=None:
            if index==pos:
                item = current.data
                remove(current.data)
            else:
                index = index+1
                current = current.next
        return item
        
