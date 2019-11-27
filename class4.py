# import cv2
# import tkinter
import selenium
# import socket
# s = socket.socket()  # 创建 socket 对象
# host = socket.gethostname()  # 获取本地主机名
# port = 12345  # 设置端口
# s.bind((host, port))  # 绑定端口
# s.listen(5)  # 等待客户端连接
# while True:
#     c, addr = s.accept()  # 建立客户端连接
#     print('连接地址',addr)
#     data='欢迎访问菜鸟教程！'
#     byt=data.encode()
#     c.send(byt)
#     c.close()  # 关闭连接
import  urllib1.request
from bs4 import BeautifulSoup
from selenium import webdriver
def test():
    # with urllib.request.urlopen('http://home.baidu.com/') as f:
    #    #print(f.read(300))
    #     soup=BeautifulSoup(f,'html.parser')
    #     print(soup.title)
    #     print(soup.title.string)
    #     for a in(soup.find_all('a')):
    #         print(a.text,a.get('href'))
    browser=webdriver.Chrome()
def main():
    test()
if __name__ == '__main__':
    main()