#网络爬虫
import requests
from urlextract import URLExtract 

def getHTMLText(url):  #获取网页内容
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status() #如果状态不是200，引发异常
        r.encoding = 'utf-8' #无论原来用什么编码，都改成utf-8
        return r.text
    except:
        return ""

def printurl(text):   #h获取文本中的网页，输出url列表
    extractor = URLExtract()
    urls = extractor.find_urls(text)
    #i=0;  
    if len(urls) !=0:   #if str(urls).isspace==True  如果数据不是url类型，会输出空串，选择当为非0的时候再输出
        #i=i+1
        #print('这是该层网络的第{}个网站'.format(i))
        print(urls) 
    return urls

def recursive(urln):   #不断获取获取新网页数据，输出新的url列表
    #count=0;
    for i in range (len(urln)):  #range(3)  list index out of range
        #count=count+1;
        #print('这是第{}层网络'.format(count))
        textnew = getHTMLText(urln[i])
        recursive(printurl(textnew))
        
    
def main():
    url = "http://www.tju.end.cn/"  #需要爬取数据的网页
    text = getHTMLText(url)        
    urls = printurl(text)
    recursive(urls)
 
