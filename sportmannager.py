#体育竞技分析
from random import random
from tkinter import N
def printIntro():
    print("该程序模拟两个选手A和B的某种竞技比赛")
    print("程序运行需要A和B的能力值（以0到1之间的小数表示）")
    print("程序运行需要环境和选手状态的判定（以1到4之间的小数表示）")
def getInputs():
    while True:
        try:
            a=eval(input("请输入选手A的能力值（0-1）："))
            if(a>0 and a<1):
                break
            else:
                print("请输入0——1之间的数")
        except Exception:
            print("输入异常")
    while True:
        try:
            b=eval(input("请输入选手B的能力值（0-1）："))
            if(b>0 and b<1):
                break
            else:
                print("请输入0——1之间的数")
        except Exception:
            print("输入异常")
        
    n=eval(input("模拟比赛场次："))
    return a,b,n
    
def power(probA,probB):
    try:
        s=eval(input("请于此处选择该场比赛的风向：若风向利于选手A，请输入“1”\n若风向不利于A，请输入“2”\n"))
        if s==1:
            probA=probA+0.05
        elif s==2:
            probB=probB+0.05
        else:
            print("没有该选项")
    except Exception:
            print("输入异常，请重新输入")

    try:
        q=eval(input("请判断选手A赛前状态，状态极佳请输入“1”\n状态良好请输入“2”\n状态一般请输入“3”\n状态极差请输入“4”\n"))
        if q==1:
            probA=probA*1.1
        elif q==2:
            probA=probA
        elif q==3:
            probA=probA*0.95
        elif q==4:
            probA=probA*0.8
        else:
            print("没有该选项")
    except Exception:
        print("输入异常，请重新输入")

    try:
        p=eval(input("请判断选手B赛前状态，状态极佳请输入“1”\n状态良好请输入“2”\n状态一般请输入“3”\n状态极差请输入“4”\n"))
        if p==1:
            probB=probB*1.1
        elif p==2:
            probB=probB
        elif p==3:
            probB=probB*0.95
        elif p==4:
            probB=probB*0.8
        else:
            print("没有该选项")
    except Exception:
        print("输入异常，请重新输入")
def simNGames(n,probA,probB):
    winsA,winsB=0,0
    for i in range(n):
        scoreA,scoreB=simOneGame(probA,probB)
        if scoreA>scoreB:
            winsA+=1
        else:
            winsB+=1
    return winsA,winsB
def gameOver(a,b):
    return a==15 or b==15
def simOneGame(probA,probB):
    scoreA,scoreB=0,0
    serving="A"
    while not gameOver(scoreA,scoreB):
        if serving=="A":
            if random()<probA:
                scoreA+=1
            else:
                serving="B"
        else:
            if random()<probB:
                scoreB+=1
            else:
                serving="A"
    return scoreA,scoreB
def printSummary(winsA,winsB):
    n=winsA+winsB
    print("竞技分析开始，共模拟{}场比赛".format(n))
    print("选手A获胜{}场比赛，占比{:0.1%}".format(winsA,winsA/n))
    print("选手B获胜{}场比赛，占比{:0.1%}".format(winsB,winsB/n))
    
def main():
    printIntro()
    probA, probB, n=getInputs()
    power(probA,probB)
    winsA, winsB=simNGames(n,probA,probB)
    printSummary(winsA,winsB)


