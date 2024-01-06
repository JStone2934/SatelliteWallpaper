import pystray
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
Image.MAX_IMAGE_PIXELS = None
import win32com.client as client
from pystray import MenuItem
import main
import getpass
import win32com.client
import win32gui,win32con,win32api
import time
from threading import Thread
import os,shutil
import sys
import base64
from icon_png import img as one
import winshell
from win32com.client import Dispatch

import pythoncom
yes_no=0
N_select=1 #默认开启弹窗



class AutoRun():
 
    def __init__(self):
        script_path = sys.argv[0]
        zdynames = "风暴眼.exe"    # 当前文件名的名称如：newsxiao.py
        name = os.path.splitext(zdynames)[0]      # 获得文件名的前部分,如：newsxiao
        path = "\""+os.path.dirname(os.path.realpath(sys.executable))+'\\'+zdynames+"\""
        # path = os.path.abspath(os.path.dirname(__file__))+'\\'+zdynames # 要添加的exe完整路径如：
        # 注册表项名
        KeyName = 'Software\\Microsoft\\Windows\\CurrentVersion\\Run'
        # 异常处理
        #remove_shortcut_on_desktop()
        try:
            create_shortcut_on_desktop()
            #key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER,  KeyName, 0,  win32con.KEY_ALL_ACCESS)
            # win32api.RegSetValueEx(key, name, 0, win32con.REG_SZ, "NULL")
            #win32api.RegSetValueEx(key, name, 0, win32con.REG_SZ, path)
            # win32api.RegDeleteKey(key, 'tray')
            #win32api.RegCloseKey(key)
            
        except IOError as e:
            print(e)
        print('添加成功！')

def create_shortcut_on_desktop():
    try:

        # 获取当前脚本的路径
        script_path = os.path.abspath(sys.argv[0])
        
        # 获取桌面路径
        desktop = winshell.desktop()
        sysName = os.getenv("SystemDrive")
        # 获取用户名
        username = getpass.getuser()	
        startupDir = os.path.join(sysName,r"/users",username,r"AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup")
        print("自启动目录：",startupDir)
        # 创建快捷方式的路径和名称
        path = os.path.join(startupDir, "风暴眼.exe.lnk")  # 这里的 YourShortcutName 是你希望的快捷方式名称
        desktop2start=desktop+"\\风暴眼.exe.lnk"
        #
        # 创建快捷方式
        shell = Dispatch('WScript.Shell')
        """
        time.sleep(1)
        shortcut = client.Dispatch("WScript.Shell").CreateShortCut(path)
        shortcut.TargetPath = script_path
        shortcut.save()
        """
        winshell.CreateShortcut(
            Path=path,
            Target=script_path,
            #Icon=(script_path, 0),
		)

        '''
        shortcut = shell.CreateShortCut(path)
        shortcut.Targetpath = script_path
        shortcut.save()
        '''
        #shutil.move(desktop2start,startupDir)
        print("Shortcut created successfully on the desktop.")
    except Exception as e:
        print(f"An error occurred: {e}")

def remove_shortcut_on_desktop():
    try:
        # 获取当前脚本的路径
        script_path = os.path.abspath(sys.argv[0])
        
        # 获取桌面路径
        desktop = winshell.desktop()
        sysName = os.getenv("SystemDrive")
        # 获取用户名
        username = getpass.getuser()	
        startupDir = os.path.join(sysName,r"/users",username,r"AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/风暴眼.exe.lnk")
        os.remove(startupDir)
        print("Shortcut removed successfully on the desktop.")
    except Exception as e:
        print(f"An error occurred: {e}")

class Stop_AutoRun():
    
    def __init__(self):
        zdynames = "风暴眼.exe"     # 当前文件名的名称如：newsxiao.py
        name = os.path.splitext(zdynames)[0]      # 获得文件名的前部分,如：newsxiao
        # path = os.path.abspath(os.path.dirname(__file__))+'\\'+zdynames # 要添加的exe完整路径如：
        # 注册表项名
        KeyName = 'Software\\Microsoft\\Windows\\CurrentVersion\\Run'
        # 异常处理
        try:
            remove_shortcut_on_desktop()
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

def timer():
    t=time.localtime()
    p=0
    try:
        pass
    except:
        pass
    while True:
        auto_set()
        for dsb in range(1100):
            try:
                pass
            except:
                pass
            time.sleep(1)
        main.sat_status="卫星状态\n-----初始化-----\n"
        

def auto_set():
    status="连接卫星...."
    if(N_select==1):
        icon.notify(status)
    main.action(1)
    
    status="卫星数据已更新"
    if(N_select==1):
        icon.notify(status)

def FY4B():
    main.action(2)
    status="正在使用FY4B卫星数据..."
    if(N_select==1):
        icon.notify(status)
    

def FY4A():
    main.action(3)
    status="正在使用FY4A卫星数据..."
    if(N_select==1):
        icon = pystray.Icon("name", image, status, menu)
    

def CN():
    main.action(4)

def on_exit(icon, item):
    yes_no=1
    icon.stop()

def SatrtAutoRun():
    #sat_status="-----警告-----\n\n\n由于涉及敏感权限\n\n开机自动启动功能可能引起杀毒软件的提示,这是正常现象。\n\n这也可能对您的系统产生不利影响,请您谨慎使用此功能。\n\n\n\n\n选择“是”完成设置,选择“否”放弃设置\n\n"
    #ar=win32api.MessageBox(0,sat_status,"开机自启",win32con.MB_YESNO|win32con.MB_ICONWARNING|win32con.MB_SYSTEMMODAL|win32con.MB_DEFBUTTON2)
    # print(ar)
    #AutoRun()
    #status="开机自动启动已打开"
    #icon.notify(status)
    AT =AutoRun()
    status="开机自动启动已打开"
    icon.notify(status)
    '''
    if ar==6:
        AT =AutoRun()
        status="开机自动启动已打开"
        icon.notify(status)
        
    elif ar==7:
        SAT=Stop_AutoRun()
        status="开机自动启动已关闭"
        icon.notify(status)
    '''
    

def StopAutoRun():
    SAT=Stop_AutoRun()
    status="开机自动启动已关闭"
    icon.notify(status)

def Notify_select():
    global N_select
    if(N_select==1):
        N_select=0
    else:
        N_select=1
        status="已开启弹窗通知"
        icon.notify(status)
    print("NSELECT",N_select)

def notify(icon: pystray.Icon):
    icon.notify("我是消息类容", "消息标题")

def show_window():
    sat_status=main.sat_status
    win32api.MessageBox(0,sat_status,"卫星数据状态",win32con.MB_ICONWARNING)



menu = (MenuItem(text='图源自动切换', action=auto_set), 
        MenuItem(text='FY4B风暴图', action=FY4B),
        MenuItem(text='FY4A云图', action=FY4A),
        MenuItem(text='中国区域云图', action=CN),
        MenuItem(text='卫星数据状态', action=show_window),
        MenuItem(text='开机自动启动', action=SatrtAutoRun),
        MenuItem(text='关闭开机自启', action=StopAutoRun),
        MenuItem(text='开启/关闭弹窗通知', action=Notify_select),
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


