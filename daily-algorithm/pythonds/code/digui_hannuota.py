# coding=utf-8

# 汉诺塔问题，用三个list表示三个pole

def moveTower(height,fromstack,tostack,withstack):
    if height>=1:
        moveTower(height-1,fromstack,withstack,tostack)
        moveDisk(fromstack,tostack)
        moveTower(height-1,withstack,tostack,fromstack)
    print('from:',fromstack)
    print('with:',withstack)
    print('to:',tostack)
    print('*'*15)
        
def moveDisk(fs,ts):
    print(fs,'\tto->\t',ts)
    disk = fs.pop()
    ts.append(disk)
    
def main():
    stack1 = [25,17,9,6,3]
    stack2 = []
    stack3 = []
    moveTower(len(stack1),stack1,stack2,stack3)
    
main()