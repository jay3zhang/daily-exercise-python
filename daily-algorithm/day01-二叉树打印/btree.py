# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class node():  
    def __init__(self,d=None,l=None,r=None):  
        self.data=d 
        self.left=l 
        self.right=r
  
def create(root):  
    
    a=raw_input('enter a data:')
    if a is '#':  
        root=None;  
    else:  
        root=node(d=a)
        root.left=create(root.left)
        root.right=create(root.right) 
    return root
  
def preorder(root):      #先序遍历  
    if root is None:  
        print '#!',
        return ;  
    else :  
        print root.data+'!',
        preorder(root.left) 
        preorder(root.right) 
  
def inorder(root):     #中序遍历  
    if root is None: 
        print '#!',
        return 0
    else:  
        inorder(root.left) 
        print root.data+'!', 
        inorder(root.right)
  
def postorder(root):   # 后序遍历  
    if root is None:  
        print '#!',
        return 0
    else :  
        postorder(root.left)
        postorder(root.right) 
        print root.data+'!',
  

def level_queue(root):
       # """利用队列实现树的层次遍历"""
        if root is None:
            return 0
        myQueue = []
        node = None
        last = root
        nlast = root
        myQueue.append(root)
        while myQueue:
            node = myQueue.pop(0)
            print node.data,
            if node.left != None:
                nlast = node.left
                myQueue.append(node.left)
            if node.right != None:
                nlast = node.right
                myQueue.append(node.right)  
            if node==last:
                print ''    #自动打印回车
                last = nlast
        
  
root=None    # 测试代码  
print "<先序建立二叉树>"
root=create(root)
print "\n先序遍历----------------------"
preorder(root)
print "\n中序遍历----------------------"
inorder(root) 
print "\n后序遍历----------------------"
postorder(root) 

print "\n按层遍历----------------------"
level_queue(root)
