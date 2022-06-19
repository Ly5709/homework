
#h哈希函数
import hashlib

def printIntro():
    print("该程序是对一段数字进行加密操作的程序")
    print("程序运行需要输入一段任意的数字")

def getInput():
    while True:
        try:
            a=input("输入任意你想要加密的数字或字母串：")
            break
        except Exception:
            print('输入格式有误，请重新输入')

def secret(data):
    md5 = hashlib.md5()     # 应用MD5算法
    md5.update(data.encode('utf-8'))
    print(md5.hexdigest())

def printSummary():
    print("程序已成功执行")

def main():
    printIntro()
    data=getInput()
    secret(data)
    printSummary()