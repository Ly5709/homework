#turtle函数绘图
import turtle

def printIntro():
    print("该程序是利用turtle函数对汉字“大”进行书写")
    print("程序运行需要笔刷的大小，颜色，圆弧弧度以及笔刷速度")

def getInputs():
    a=eval(input("请输入笔刷的大小(30-50)："))
    b=input("请输入笔刷的颜色(red blue,green)：")
    c=eval(input("圆弧弧度："))
    d=eval(input("请输入运笔速度(1-5)："))
    return a,b,c,d
    #此处我尝试加过try，但是不知道是否是数据类型不同的原因，加上while True和try except后程序一直报错，就进行了删除。

def pen(size,color,seth,speed):
    turtle.setup(0.5,0.5,0,0)
    turtle.pensize(size)
    turtle.pencolor(color)
    turtle.seth(seth)
    turtle.speed(speed)
    
def draw1(length):
    turtle.fd(length)

def draw2(length,angle):
 for i in range(length//4+1):
    turtle.circle(length,angle)

def draw3(length,angle):
 for i in range(length//4+1):
    turtle.circle(-length,angle)

def drawda(length):
 turtle.pendown()
 draw1(length)
 turtle.back(length//2)
 turtle.seth(-90)
 turtle.back(length//5)
 draw1(length//5)
 draw2(length,length//40)
 turtle.penup()
 turtle.goto(length//2,0)
 turtle.pendown()
 turtle.seth(-90)
 draw3(length,length//50)
 
def printSummary():
    print("已成功执行上述程序")
           
def main():
    printIntro()
    size, color, seth, speed=getInputs()
    pen(size,color,seth,speed)
    drawda(100)
    printSummary()
