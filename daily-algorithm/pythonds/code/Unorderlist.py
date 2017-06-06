# coding=utf-8

# 无序列表，类似链表

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class UnorderList:
    def __init__(self):
        self.head = None
    
    # def __init__(self,data):
        # self.head = Node(data)
        # self.tail = self.head
    
    def add(self,data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp
    
    # def add(self,data):
        # temp = Node(data)
        # self.tail.next = temp
        # self.tail = temp
    
    def isEmpty(self):
        return self.head == None
        
    def search(self,item):  #搜索是否在列表中
        current = self.head
        Found = False
        while current!=None and not Found:
            if current.data == item:
                Found = True
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

    # 剩下的方法——追加（append），插入（insert），索引（index），弹出（pop）,都将作为你的
    # 练习。记住任何一个操作中都要同时考虑对象在列表头部和其他位置这两种情况。同样，插入、索
    # 引、弹出需要我们给列表中的位置命名。我们假定列表中位置的名称是从 0 开始的整数。 
    # 牛刀小试 
    # 1.实现无序列表的 append 方法。并给出你的程序的时间复杂度。 
    # 2.在上一个问题中，你很有可能给出一个时间复杂度为 O（n）的算法。但如果你给“无序表”类添
    # 加一个变量，你可以写出时间复杂度为 O（1）的算法。将你的算法的时间复杂度简化为 O（1）。注
    # 意！这时你需要考虑非常多的特殊情况，同时要修改 add 方法。 
    def index(self,item):
        current = self.head
        pos = 0
        while current!=None:
            if current.data == item:
                return pos
            else:
                pos = pos+1
                current = current.next
        return pos
        
    def append(self,item):
        temp = Node(item)
        #找到最后一个节点
        while self.head.next!=None:
            self.head = self.head.next
        last = self.head
        temp.next = last.next
        last.next = temp
        
    def insert(self,pos,item):
        if pos==0:
            add(item)
        else:
            temp = Node(item)
            current = self.head
            index = 0
            while current!=None:
                if index==pos-1:
                    temp.next = current.next
                    current.next = temp
                else:
                    index = index+1
                    current = current.next
        
    def pop(self,pos=0):
        current = self.head
        index = 0
        while current!=None:
            if index==pos:
                item = current.data
                remove(current.data)
            else:
                index = index+1
                current = current.next
        return item
        
