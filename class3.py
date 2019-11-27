import sys
import json
import types
import PIL
class student:
    _s=10
    name='a'
    def __init__(self,a):
        self.name=a
    def gets(self):
        return self._s
    def getname(self):
        return self.name
def test():
    # print(dir(sys))
    # print(sys.__doc__)
    # print(sys.path)
    # print(sys.argv)
    # print(sys.__name__)
    # print(dir(types))
    # print(isinstance('a',str))
    m=student('a')
    print(m.name)
    print(m.getname())
    print(m.gets())
    m = student('b')
    print(m.name)
    print(m.getname())
    print(m.gets())
def main(*args,**kw):
    test()
    '''
    本程序执行时会调用main函数，被别的程序调用时不执行
    '''
if __name__ == '__main__':
    main()