#语法检查器
import keyword
from operator import truediv
List=keyword.kwlist
def printIntro():
    print("该程序是一个针对个别关键字的语法判断程序")
    print("该程序需要输入一个选择打开的程序文本")
    print("该程序需要选择你所要检查的语法")

def getInput():
    while True:
        try:
            name=input("输入你要查找的代码文件：\character.txt\menu.txt\progressbar.txt\sevenseg.txt")
            return name
            break
        except Exception:
            print("请重新输入") 

def getText(name):
    file=open(name,"r",encoding='utf-8')
    lines=file.readlines() 
    return lines        

def judge_try(lines):
    count=0;
    count2=0;
    count3=0;
    for line in lines:
        pos1=line.find('try:')  
        count=count+1;
        if pos1!=-1:    #count所计数的行中包含try语句
            for line2 in lines:  #在try过后进行逐行扫描
                pos2=line2.find('except') #在try过后的行中except的位置
                count2=count2+1;
                if count2>count: #只对位于所对应的Try之后的语句进行查找
                    if pos2!=-1:
                        if pos2==pos1:
                            for line3 in lines:
                                count3=count3+1;
                                pos3=line3.find('try:')
                                if count3>count:
                                    if pos3==pos1:
                                        if count3<count2:
                                            print('第{}行的try存在问题，缺少对应except，请检查'.formar(count))
                                            break
                            pos3=line2.find(':',pos2+1)  #在except所在行查询“：”的位置
                            if pos3==-1:
                                print('第{}行处的except语句存在问题，可能是缺少“:”请检查'.format(count2))
                            else:
                                print('第{}行的try使用正确'.format(count))

def judge_if(lines):
    count=0;
    for line in lines:
        pos1=line.find('if ')
        count=count+1;
        if pos1!=-1:
            pos2=line.find(':',pos1+1)#在if所在行，在if之后，查询是否存在：
            if pos2==-1:
                pos3=line.find('else',pos1+1)
                if pos3==-1:
                    print('第{}行的if语句存在问题，缺少必要的“:”或者“else”'.format(count))
                else:
                    print('第{}行的if使用正确'.format(count))
            else:
                print('第{}行的if使用正确'.format(count))

def judge_for(lines):
    count=0;
    for line in lines:
        count=count+1;
        pos1=line.find('for ')
        if pos1!=-1:
            pos2=line.find(' in ',pos1+1)
            if pos2!=-1:
                pos3=line.find(':',pos2+1)
                if pos3==-1:
                    print('第{}行的for使用错误，缺少“：”'.format(count))
                else:
                    print('第{}行的for使用正确'.format(count))
            else:
                print('第{}行的for使用错误，缺少“in”'.format(count)) 
    
def printSummary():
    print("程序运行结束，已完成三种语法的判断")
    
def main():
    printIntro();
    name=getInput();
    lines=getText(name)
    judge_try(lines)
    judge_if(lines)
    judge_for(lines)
    printSummary();


    
