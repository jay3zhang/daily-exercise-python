# -*- coding:utf-8 -*-
 
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class TreePrinter:
    def printTree(self, root):
        # write code here
        res = []
        queue = []
        if root == None:
            return res
        last = root
        nlast = root
        queue.append(root)
        temp = []
        while len(queue):
            node = queue.pop(0)
            temp.append(node.val)                
            if node.left != None:
                queue.append(node.left)
                nlast = node.left
            if node.right != None:
                queue.append(node.right)
                nlast = node.right
            if node == last:
                res.append(temp[:])
                temp = []
                last = nlast
        return res