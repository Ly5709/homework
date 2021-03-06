import turtle
import time

def printIntro():
    print("该程序利用turtle完成对七段数码管日期显示的配置")
    print("程序运行需要笔刷的颜色")

def getInputs():
    while True:
        try:
            a=input("请输入笔刷的颜色(red blue,green)：")
            b=eval(input("请输入运笔速度(10-50)："))
            return a,b
        except Exception:
            print('输入错误请重新输入')
    
def drawGap(): 
    turtle.penup()
    turtle.fd(5)

def drawLine(draw): 
    drawGap()
    turtle.pensize(8) if draw else turtle.pensize(1)
    turtle.pendown()
    turtle.left(45)
    turtle.fd(5)
    turtle.right(45)
    turtle.fd(40)
    turtle.right(45)
    turtle.fd(5)
    turtle.right(90)
    turtle.fd(5)
    turtle.right(45)
    turtle.fd(40)
    turtle.right(45)
    turtle.fd(5)
    turtle.right(135)
    turtle.penup()
    turtle.fd(47)
    turtle.pendown()
    drawGap()
    
def drawDigit(digit):
    
    drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)     
    turtle.right(100)
    drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)     
    turtle.right(80)
    drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)     
    turtle.right(100)
    drawLine(True) if digit in [0,2,6,8] else drawLine(False)       
    
    drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)       
    turtle.right(80)
    drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)       
    turtle.right(100)
    drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)       
    turtle.right(80)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)

def drawDate(date):
    try:
        for i in date:
            if(i=='年'):
                turtle.write('年',font=("Arial",18,"normal"))
                turtle.pencolor("red")
                turtle.fd(40)
            elif i=='月':
                turtle.write('月',font=("Arial",18,"normal"))
                turtle.fd(40)
            elif i=='日':
                turtle.write('日',font=("Arial",18,"normal"))
                turtle.goto(-300,0)
                turtle.right(90)
                turtle.fd(150)
                turtle.left(90)
            
            else:
                drawDigit(eval(i))
    except NameError:
        print("输入格式错误")
        
def draw(color,speed):
    turtle.setup(1000,600,0,0)
    turtle.pencolor(color)
    turtle.speed(speed)
    turtle.hideturtle()
    turtle.penup()
    turtle.fd(-300)
    drawDate(time.strftime('%Y年%m月%d日',time.gmtime()))
    drawDate('abc')
    turtle.done()

def printSummary():
    print("已成功执行上述程序")

def main():
    printIntro()
    color, speed=getInputs()
    draw(color,speed)
    printSummary()
    

