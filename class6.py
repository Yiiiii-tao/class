import numpy as np
def test():
    a = np.arange(15).reshape(3, 5)
    # a=np.array([[1,2,3],[4,5,6]],dtype=np.int16)
    # a=np.linspace(0,10,11)
    # a=np.zeros((3,5))#[[1,2,3]] != [1,2,3]
    # a=np.ones((3,5))
    # a=np.eye(3)*2
    # a=np.diag([2,3,4])
    # print(type(a))
    print(a)
    # print(a.shape,a.size,a.itemsize)
    # print(a*10+4)
    print(a[:2,1::2])
def main():
    test()
if __name__ == '__main__':
    main()