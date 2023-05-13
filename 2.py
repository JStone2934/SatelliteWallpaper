import time
import pystray
from PIL import Image
import threading


def on_quit_callback(icon):
    icon.stop()


def my_function():
    # 在这里写你的函数代码
    print("函数被调用了！")


def loop_function():
    my_function()
        # time.sleep(10 * 60)  # 延迟 10 分钟


def main():

    # 创建托盘图标
    image = Image.open("icon.png")
    icon = pystray.Icon("name", image, "tooltip")
    # 设置图标可见
    icon.visible = True

    # 启动图标并让程序在后台持续运行
    icon.run(on_exit=on_quit_callback)


if __name__ == '__main__':
    main()
