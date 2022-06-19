menu0 = '''
        主菜单
==========================
1：哈希函数

2：绘图（大字书写）

3：7段数码管

4：查找保留字

5：敬请期待！

0：退出程序
==========================
'''
import hash
import character
import findwords
import shumaguan2
import sportmannager
import pachong
import compiler

def Intro():
    print('该程序菜单可以选择菜单栏中所有您想实现的功能并实现运作')
    print('该程序需要您输入您的选择')

def menutype():
        print('\n  主菜单   ')
        print('=' * 12)
        print('1. 实现哈希函数')
        print('2. 书写大字')
        print('3. 查找关键字')
        print('4. 七段数码管显示时间')
        print('5. 体育竞技分析')
        print('6. 网络爬虫')
        print('7. 语法检查器')
        print('=' * 12)

def getInput():
    while True:
        try:
            a=int(input('请输入您所要选择实现的功能'))
            if a>7:
                print('该模式还未开发，请输入1-7之间的数字')
            return a
        except Exception:
            print('输入格式错误请重新输入')

def process(mc):
    if mc==1:
        hash.main()
    elif mc == 2:
        character.main()
    elif mc == 3:
        findwords.main()
    elif mc == 4:
        shumaguan2.main()
    elif mc == 5:
        sportmannager.main()
    elif mc == 6:
        pachong.main()
    elif mc == 7:
        compiler.main()

def main():
    Intro()
    menutype()
    mc=getInput()
    process(mc)

main()

