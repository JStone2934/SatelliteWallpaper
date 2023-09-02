import pystray
from PIL import Image
from pystray import MenuItem
import main

status = "正在连接卫星.."

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


menu = (MenuItem(text='卫星数据更新', action=auto_set), 
        MenuItem(text='FY4B风暴图', action=FY4B),
        MenuItem(text='FY4A云图', action=FY4A),
        MenuItem(text='中国区域云图', action=CN),
        MenuItem(text='卫星数据状态', action=auto_set),
        MenuItem(text='退出', action=on_exit),
        )
image = Image.open("icon.png")
icon = pystray.Icon("name", image,"风暴眼", menu)
icon.run()
