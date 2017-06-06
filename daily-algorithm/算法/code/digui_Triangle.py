import turtle
import time

def drawTriangle(points,color,mT):  # 画图函数
    mT.fillcolor(color)
    mT.up()
    mT.goto(points[0][0],points[0][1])
    mT.down()
    mT.begin_fill()
    mT.goto(points[1][0],points[1][1])
    mT.goto(points[2][0],points[2][1])
    mT.goto(points[0][0],points[0][1])
    mT.end_fill()
    
def getMid(p1,p2):  #计算边的中点
    return ((p1[0]+p2[0])/2,(p1[1]+p2[1])/2)
    
def recur(points,degree,mT):
    colormap = ['blue','red','green','white','yellow','violet','orange']
    drawTriangle(points,colormap[degree],mT)    # 调用画图函数
    time.sleep(1)
    if degree>0:    # 以两个边的中点为新顶点画图，画三个三角形空出来一个中间的三角形
        recur([points[0],getMid(points[0],points[1]),getMid(points[0],points[2])],degree-1,mT)
        recur([points[1],getMid(points[0],points[1]),getMid(points[1],points[2])],degree-1,mT)
        recur([points[2],getMid(points[2],points[1]),getMid(points[0],points[2])],degree-1,mT)
        
        
def main():
    mT = turtle.Turtle()
    myWin = turtle.Screen()
    myPoints = [[-100,-50],[0,100],[100,-50]]
    recur(myPoints,3,mT)
    myWin.exitonclick()  #点击退出
    
main()
    