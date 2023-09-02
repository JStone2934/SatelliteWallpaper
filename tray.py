import pystray
from PIL import Image
from pystray import MenuItem
import main
import win32gui,win32con,win32api
import time
from threading import Thread
def init():
    win32api.MessageBox(0,"正在连接卫星...距初始化完成还有30秒","风暴眼",win32con.MB_ICONWARNING)
    threads=[]
    t1=Thread(target=timer,name="sat",daemon=True)
    threads.append(t1)
    t2=Thread(target=icon.run,name="tray")
    threads.append(t2)
    print("--------启动-------")
    for t in threads:
        t.start()
    
status = "正在连接卫星.."
sat_status="fghj"

def timer():
    t=time.localtime()
    while True:
        auto_set()
        time.sleep(1200)

def auto_set():
    main.action(1)
    status="卫星数据已更新"
    icon.notify('Hello World!')

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
    icon.stop()


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
        MenuItem(text='退出', action=on_exit),
        )
image = Image.open("icon.png")
icon = pystray.Icon("name", image,"风暴眼", menu)
init()

# icon.run()

