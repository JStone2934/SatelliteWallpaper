import pystray
from PIL import Image
from pystray import MenuItem
import main


def auto_set():
    main.action(1)

def FY4B():
    main.action(2)

def FY4A():
    main.action(3)

def on_exit(icon, item):
    icon.stop()


def notify(icon: pystray.Icon):
    icon.notify("我是消息类容", "消息标题")


menu = (MenuItem(text='卫星数据更新', action=auto_set), 
        MenuItem(text='FY4B风暴图', action=FY4B),
        MenuItem(text='FY4A云图', action=FY4A),
        MenuItem(text='发送通知', action=notify),
        MenuItem(text='我是点击图标的菜单', action=auto_set, default=True, visible=False),
        MenuItem(text='退出', action=on_exit),
        )
image = Image.open("icon.png")
icon = pystray.Icon("name", image, "鼠标移动到\n托盘图标上\n展示内容", menu)
icon.run()