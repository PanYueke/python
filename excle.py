#-*- coding=utf-8 -*-
import xlrd
import functools
def open_excel(file):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception as e:
        print(str(e))

def excle_table_byname(file = u'D:\python\keke\chatterBox.xlsx',colNameIndex = 0,by_name = u'Sheet1'):
    data = open_excel(file)
    table = data.sheet_by_name(by_name)
    nrows = table.nrows
    colnames = table.row_values(colNameIndex)
    list  = []
    for rownum in range(1,nrows):
        row = table.row_values(rownum)
        if row:
            app = {}
            for i in range(len(colnames)):
                app[colnames[i]] = row[i]
            list.append(app)
        return list
def fact(num):
    if(num == 1):
        return 1
    return num * fact(num-1)
def jishu():
    L = []
    n = 1
    while n <= 99:
        L.append(n)
        n = n + 2
    return L
def dict():
    d = {'name':'keke','age':24,'project':u'互动视频'}
    for key,value in d.items():
        print(key,value)
        print(key,':',value)
def liangceng():
    L = [m + n for m in 'ABC' for n in 'XYZ']
    print(L)
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        # print(b)
        yield b
        a,b = b,a + b
        n = n + 1
    return 'done'
def func(x,y):
    return x + y
m = map(func,range(1,8),range(3,6))
print(list(m))
def int2(x,base=2):
    return int(x,base)
int2 = functools.partial(int,base = 2)
def main():
    tables = excle_table_byname()
    for row in tables:
        print(row)
    jiecheng = fact(10)
    print("10的阶乘是：%d"%(jiecheng))
    jsList = jishu()
    print(jsList)
    # for num in jsList:
    #     print(num)
    dict()
    liangceng()
    g = fib(6)
    # while True:
    #     try:
    #         x = next(g)
    #         print('g:',x)
    #     except StopAsyncIteration as e:
    #         print('Generator return value:',e.value)
    #         break
    func(3,5)
    i = int2('10000')
    print(i)
if __name__ == '__main__':
    main()
