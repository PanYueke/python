#coding:utf-8
import urllib.request
import urllib.parse
import re
import logging  # 引入logging模块
def get_html(url):
    page = urllib.request.urlopen(url)
    htmlcode = page.read()
    htmlCode = htmlcode.decode('utf-8')
    return htmlCode
    # print(htmlcode)
    #写文件操作n
    # pageFile = open('pageCode.txt','wb+')
    # pageFile.write(htmlcode)
    # pageFile.close()
def logFunction():
    # 将信息打印到控制台上
    logging.debug(u"苍井空")
    logging.info(u"麻生希")
    logging.warning(u"小泽玛利亚")
    logging.error(u"桃谷绘里香")
    logging.critical(u"泷泽萝拉")
def myselfLogFunction():
    logging.basicConfig(level=logging.NOTSET)
    logger = logging.getLogger('')
    logger.setLevel(logging.NOTSET)
    logging.debug(u"是否可以显示呢？")
    logging.info(u"这两条信息都应该被显示才对！")
if __name__ == '__main__':
    logFunction()
    myselfLogFunction()
    # reg = r'src="(.+?\.jpg)"width'
    # 加r表示后面的内容不被转义
    # reg = r'src="(.+?\.jpg)" width'
    reg = r'https://[^\s]*?\.jpg'
    reg_img = re.compile(reg)
    imgList = reg_img.findall(get_html('http://tieba.baidu.com/p/1753935195'))
    x = 0
    for img in  imgList:
        print(img)
        urllib.request.urlretrieve(img,'D:\Work\Python\Img\%s.jpg' %x)
        x += 1

