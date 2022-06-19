#查找关键字
import keyword
List=keyword.kwlist  #建立保留字一览表

def printIntro():
    print("该程序是检索一个文件中的关键字个数并输出")
    print("程序运行需要输入一个文件的名字")

def getText(name):
    txt=open(name,"r",encoding='utf-8').read()
    txt=txt.lower()    #将所有大写字母改写为小写
    for ch in'!"#$%()*+,-./:;<=>?@[\\]^_{|}~':
        txt=txt.replace(ch," ")     #将上述特殊字符全部替换为空格
    return txt

def achieve():
    while True:
        try:
            name=input("输入你要查找的代码文件：\character.txt\menu.txt\progressbar.txt\sevenseg.txt")
            TXT=getText(name)
            break
        except Exception:
            print("输入错误！") 
    words=TXT.split()
    counts={}
    for word in words:
        counts[word]=counts.get(word,0)+1
    items=list(counts.items())
    items.sort(key=lambda x:x[1],reverse=True)
    for i in range(50):
        word,count=items[i]
        print("{0:<10}{1:>5}".format(word,count))
def main():
    printIntro()
    achieve()



