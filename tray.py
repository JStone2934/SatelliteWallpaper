import pystray
from PIL import Image
from pystray import MenuItem
import main
import win32gui,win32con,win32api
import time
from threading import Thread
import os
import sys
import base64
from icon_png import img as one
import cv2
import Dashboard

class AutoRun():
 
    def __init__(self):
        zdynames = "风暴眼.exe"    # 当前文件名的名称如：newsxiao.py
        name = os.path.splitext(zdynames)[0]      # 获得文件名的前部分,如：newsxiao
        path = "\""+os.path.dirname(os.path.realpath(sys.executable))+'\\'+zdynames+"\""
        # path = os.path.abspath(os.path.dirname(__file__))+'\\'+zdynames # 要添加的exe完整路径如：
        # 注册表项名
        KeyName = 'Software\\Microsoft\\Windows\\CurrentVersion\\Run'
        # 异常处理
        try:
            key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER,  KeyName, 0,  win32con.KEY_ALL_ACCESS)
            # win32api.RegSetValueEx(key, name, 0, win32con.REG_SZ, "NULL")
            win32api.RegSetValueEx(key, name, 0, win32con.REG_SZ, path)
            # win32api.RegDeleteKey(key, 'tray')
            win32api.RegCloseKey(key)
        except IOError as e:
            print(e)
        print('添加成功！')

class Stop_AutoRun():
 
    def __init__(self):
        zdynames = "风暴眼.exe"     # 当前文件名的名称如：newsxiao.py
        name = os.path.splitext(zdynames)[0]      # 获得文件名的前部分,如：newsxiao
        # path = os.path.abspath(os.path.dirname(__file__))+'\\'+zdynames # 要添加的exe完整路径如：
        # 注册表项名
        KeyName = 'Software\\Microsoft\\Windows\\CurrentVersion\\Run'
        # 异常处理
        try:
            key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER,  KeyName, 0,  win32con.KEY_ALL_ACCESS)
            win32api.RegSetValueEx(key, name, 0, win32con.REG_SZ, "NULL")
            # win32api.RegSetValueEx(key, name, 0, win32con.REG_SZ, path)
            # win32api.RegDeleteKey(key, 'tray')
            win32api.RegCloseKey(key)
        except IOError as e:
            print(e)
        print('添加成功！')



def init():
    
    win32api.MessageBox(0,"正在连接卫星...距初始化完成还有30秒","风暴眼",win32con.MB_ICONWARNING)
    threads=[]
    t1=Thread(target=timer,name="sat",daemon=True)
    
    t2=Thread(target=icon.run,name="tray")
    threads.append(t2)
    threads.append(t1)
    print("--------启动-------")
    
    for t in threads:
        t.start()
    
status = "正在连接卫星.."
sat_status="fghj"

def timer():
    t=time.localtime()
    p=0
    
    while True:
        for dsb in range(1100):
            try:
                Dashboard.set_data()
            except:
                pass
            time.sleep(1)
        main.sat_status="卫星状态\n-----初始化-----\n"
        auto_set()

def auto_set():
    status="连接卫星...."
    icon.notify(status)
    main.action(1)
    
    status="卫星数据已更新"
    icon.notify(status)

def FY4B():
    main.action(2)
    status="正在使用FY4B卫星数据..."
    icon = pystray.Icon("name", image, status, menu)
    

def FY4A():
    main.action(3)
    status="正在使用FY4A卫星数据..."
    icon = pystray.Icon("name", image, status, menu)
    

def CN():
    main.action(4)

def on_exit(icon, item):
    try:
        Dashboard.stop_dashboard()
    except:
        pass
    icon.stop()

def SatrtAutoRun():
    sat_status="警告：\n\n开机自启动功能可能引起杀毒软件报毒，这是正常现象\n\n此功能仍在测试阶段，可能对您的系统产生不良影响\n\n若开机自动启动功能对你造成了麻烦，可以在注册表中手动删除\"tray\"\n\n欢迎您使用未来更加稳定的版本或直接参与开发"
    ar=win32api.MessageBox(0,sat_status,"开机自启",win32con.MB_YESNO|win32con.MB_ICONWARNING|win32con.MB_SYSTEMMODAL|win32con.MB_DEFBUTTON2)
    print(ar)
    # AutoRun()
    if ar==6:
        AT =AutoRun()
        status="开机自动启动已打开"
        icon.notify(status)
        
    elif ar==7:
        SAT=Stop_AutoRun()
        status="开机自动启动已关闭"
        icon.notify(status)
        

def StopAutoRun():
    Stop_AutoRun()
    status="开机自动启动已关闭"
    icon.notify(status)

def notify(icon: pystray.Icon):
    icon.notify("我是消息类容", "消息标题")

def show_window():
    sat_status=main.sat_status
    win32api.MessageBox(0,sat_status,"卫星数据状态",win32con.MB_ICONWARNING)



menu = (MenuItem(text='卫星数据更新', action=auto_set), 
        MenuItem(text='FY4B风暴图', action=FY4B),
        MenuItem(text='FY4A云图', action=FY4A),
        MenuItem(text='中国区域云图', action=CN),
        MenuItem(text='卫星数据状态', action=show_window),
        MenuItem(text='开机自动启动', action=SatrtAutoRun),
        # MenuItem(text='关闭开机自动启动', action=StopAutoRun),
        MenuItem(text='退出', action=on_exit),
        )
try:
    try:
        os.makedirs("./SatImage")
        tmp = open('SatImage/one.png', 'wb')        #创建临时的文件
        tmp.write(base64.b64decode(one))    ##把这个one图片解码出来，写入文件中去。
        tmp.close()                
        image=Image.open("./SatImage/one.png") 
        icon = pystray.Icon("name", image,"风暴眼  V2.0", menu)
    except:
        tmp = open('SatImage/one.png', 'wb')        #创建临时的文件
        tmp.write(base64.b64decode(one))    ##把这个one图片解码出来，写入文件中去。
        tmp.close()                
        image=Image.open("./SatImage/one.png") 
        icon = pystray.Icon("name", image,"风暴眼  V2.0", menu)
    init()
except:
    time.sleep(300)
    try:
        try:
            os.makedirs("./SatImage")
            tmp = open('SatImage/one.png', 'wb')        #创建临时的文件
            tmp.write(base64.b64decode(one))    ##把这个one图片解码出来，写入文件中去。
            tmp.close()                
            image=Image.open("./SatImage/one.png") 
            icon = pystray.Icon("name", image,"风暴眼  V2.0", menu)
        except:
            tmp = open('SatImage/one.png', 'wb')        #创建临时的文件
            tmp.write(base64.b64decode(one))    ##把这个one图片解码出来，写入文件中去。
            tmp.close()                
            image=Image.open("./SatImage/one.png") 
            icon = pystray.Icon("name", image,"风暴眼  V2.0", menu)
        init()
    except:
        SAB=Stop_AutoRun()
        sys.exit()
# time.sleep(5)
# image = Image.open("./icon.png")
# image = imageio.imread("./icon.png")


# icon.run()

