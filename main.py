import os
import requests
from pathlib import Path
import cv2
import os, win32gui, win32con, win32api
import pystray
from PIL import Image
import time
import getpass
import threading
# 获取当前用户的用户名
def on_quit_callback(icon):
    icon.stop()

def get_image():
    username = getpass.getuser()
    # 创建文件夹
    img_path = os.path.abspath("./SatImage/FY4A_DISK.JPG")
    Path("SatImage").mkdir(parents=True, exist_ok=True)
    while True:
        print(1)

        # 图片链接
    # url = "http://img.nsmc.org.cn/CLOUDIMAGE/FY4A/MTCC/FY4A_DISK.JPG"

    # url = "http://img.nsmc.org.cn/CLOUDIMAGE/FY4A/MTCC/FY4A_CHINA.JPG"
    # http://img.nsmc.org.cn/CLOUDIMAGE/FY4A/MTCC/FY4A_DISK.JPG

    url = "http://img.nsmc.org.cn/CLOUDIMAGE/FY4A/MTCC/FY4A_DISK.JPG"
    # 文件保存路径
    file_path = os.path.join("SatImage", "FY4A_DISK.JPG")

    # 下载图片
    response = requests.get(url)
    with open(file_path, "wb") as file:
        file.write(response.content)
        img = cv2.imread(file_path)
        # cropped = img[0:1080, 150:2070]  # 裁剪坐标为[y0:y1, x0:x1]
        # cv2.imwrite("./SatImage/wallpaper.jpg", cropped)


    # 切换时要检查一下图片是否存在
    if os.path.exists(img_path):
        set_wallpaper(img_path)
    else:
        print('图片不存在，切换失败')

    set_wallpaper(img_path)

    print("已将图片设置为Windows 10桌面壁纸")


def set_wallpaper(img_path):
    # 打开指定注册表路径
    reg_key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)
    # 最后的参数:2拉伸,0居中,6适应,10填充,0平铺
    win32api.RegSetValueEx(reg_key, "WallpaperStyle", 0, win32con.REG_SZ, "0")
    # 最后的参数:1表示平铺,拉伸居中等都是0
    win32api.RegSetValueEx(reg_key, "TileWallpaper", 0, win32con.REG_SZ, "1")
    # 刷新桌面与设置壁纸
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, img_path, win32con.SPIF_SENDWININICHANGE)


def main():
    # 创建托盘图标
    image = Image.open("icon.png")

    icon = pystray.Icon("name", image, "tooltip")
    # 启动新线程运行循环函数
    t = threading.Thread(target=get_image())
    t.daemon = True
    t.start()
    icon.run()

    # 设置退出回调函数
    icon.visible = True
    icon.run(on_exit=on_quit_callback)




if __name__ == '__main__':
    main()



"""
# 将Python脚本复制到启动文件夹中
script_path = os.path.abspath(__file__)
startup_path = os.path.join("C:\\Users", username, "AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup")
startup_script_path = os.path.join(startup_path, "set_wallpaper.py")
if not os.path.exists(startup_path):
    os.makedirs(startup_path)
shutil.copyfile(script_path, startup_script_path)

"""

# 设置为Windows 10桌面壁纸
'''
SPI_SETDESKWALLPAPER = 0x0014
SPIF_UPDATEINIFILE = 0x01
SPIF_SENDCHANGE = 0x02
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, file_path, SPIF_UPDATEINIFILE | SPIF_SENDCHANGE)
'''




# 注意路径书写问题
