import os
import requests
from pathlib import Path
import ctypes
import cv2
import os, win32gui, win32con, win32api

# 创建文件夹
Path("SatImage").mkdir(parents=True, exist_ok=True)

# 图片链接
# url = "http://img.nsmc.org.cn/CLOUDIMAGE/FY4A/MTCC/FY4A_DISK.JPG"

url = "http://img.nsmc.org.cn/CLOUDIMAGE/FY4A/MTCC/FY4A_CHINA.JPG"
# 文件保存路径
file_path = os.path.join("SatImage", "FY4A_DISK.JPG")

# 下载图片
response = requests.get(url)
with open(file_path, "wb") as file:
    file.write(response.content)
    img = cv2.imread(file_path)
    cropped = img[0:1080, 80:2000]  # 裁剪坐标为[y0:y1, x0:x1]
    cv2.imwrite("./SatImage/wallpaper.jpg", cropped)

# 设置为Windows 10桌面壁纸
    '''
    SPI_SETDESKWALLPAPER = 0x0014
    SPIF_UPDATEINIFILE = 0x01
    SPIF_SENDCHANGE = 0x02
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, file_path, SPIF_UPDATEINIFILE | SPIF_SENDCHANGE)
    '''



def set_wallpaper(img_path):
    # 打开指定注册表路径
    reg_key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)
    # 最后的参数:2拉伸,0居中,6适应,10填充,0平铺
    win32api.RegSetValueEx(reg_key, "WallpaperStyle", 0, win32con.REG_SZ, "0")
    # 最后的参数:1表示平铺,拉伸居中等都是0
    win32api.RegSetValueEx(reg_key, "TileWallpaper", 0, win32con.REG_SZ, "0")
    # 刷新桌面与设置壁纸
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, img_path, win32con.SPIF_SENDWININICHANGE)


# 注意路径书写问题
img_path = os.path.abspath("./SatImage/wallpaper.jpg")

# 切换时要检查一下图片是否存在
if os.path.exists(img_path):
    set_wallpaper(img_path)
else:
    print('图片不存在，切换失败')

set_wallpaper(img_path)

print("已将图片设置为Windows 10桌面壁纸")
