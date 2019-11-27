import os
import  class1
def f(x):
    return x*x
def fn(x,y):
    return x*10+y
def  english(str):
    return str.capitalize()
def test():
    # print('list slice')
    # L=[0,1,2,3,4,5,6,7]
    # print(L)
    # for i in range(8):
    #     L.append(i)
    # print(L)
    # print(L[0],L[4:6])
    # s='hello world'
    # s='南京财经大学'
    # print(s[0:6:2])
    # m={'a':10,'b':5}
    # for i in sorted(m):
    #     print(i,m[i])
    # d={'x':'A','Y':'B','z':'C'}
    # l=['HELLO','WORLD','ibm','APPLe']
    # d1=[s.lower() for s in l]
    # print(l,d1)
    # d2={}
    # for s in d:
    #     d2[s]=d[s].lower()
    # print(d,d2)
    # r=map(f,[1,2,3,5,6,4])
    # for i in r:
    #     print(i)
    # print(reduce(fn,[1,2,3,4,5]))
    result=map(english,['HELLO','WORLD','ibm','APPLe'])
    for i in result:
        print(i)
def main(*args,**kw):
    test()
if __name__ == '__main__':
    main()