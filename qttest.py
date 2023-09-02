import pystray
from PIL import Image
from pystray import MenuItem
import main

def click_menu(icon, item):
    main.action()


def on_exit(icon, item):
    icon.stop()


def notify(icon: pystray.Icon):
    icon.notify("我是消息类容", "消息标题")


menu = (MenuItem(text='卫星数据更新', action=click_menu), 
        MenuItem(text='菜单2', action=click_menu),
        MenuItem(text='菜单3', action=click_menu, enabled=False),
        MenuItem(text='发送通知', action=notify),
        MenuItem(text='我是点击图标的菜单', action=click_menu, default=True, visible=False),
        MenuItem(text='退出', action=on_exit),
        )
image = Image.open("icon.png")
icon = pystray.Icon("name", image, "鼠标移动到\n托盘图标上\n展示内容", menu)
icon.run()