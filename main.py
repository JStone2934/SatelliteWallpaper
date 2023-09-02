import urllib.request
import os
import sys
import win32gui,win32con,win32api
import cv2
import time

url = "exp"
file_path = "e:/BDS/卫星壁纸1.0/SatWP_V2.0/1.jpg"
# file_path = "./SatImage/1.jpg"
data_path="./SatImage"
FY4B_SW = "http://img.nsmc.org.cn/CLOUDIMAGE/FY4B/AGRI/SWCI/FY4B_DISK_SWCI.JPG"
FY4A_TURE = "http://img.nsmc.org.cn/CLOUDIMAGE/FY4A/MTCC/FY4A_DISK.JPG"
FY4A_CN = "http://img.nsmc.org.cn/CLOUDIMAGE/FY4A/MTCC/FY4A_CHINA.JPG"
FY4B_CN = "http://img.nsmc.org.cn/CLOUDIMAGE/FY4B/AGRI/GCLR/FY4B_REGC_GCLR.JPG"
urls = [FY4B_SW, FY4A_TURE, FY4B_CN, FY4A_CN]
names = ["FY4B_DISK_SWCI", "FY4A_DISK", "FY4A_CHINA", "FY4B_REGC_GCLR"]
i = 0
'''
app = QApplication(sys.argv)
    tray_icon = QSystemTrayIcon(QIcon('icon.png'),app)
    menu = QMenu()
    action_show = QAction("Display")
    action_quit = QAction("quit")

    menu.addAction(action_show)
    menu.addAction(action_quit)
    tray_icon.setContextMenu(menu)

    action_show.triggered.connect(show_window)
    action_quit.triggered.connect(quit_program)
    
    tray_icon.show()
'''
    

def set_wallpaper(tray_menu):
    t=time.localtime()
    current_time=t.tm_hour
    print(current_time)
    if tray_menu==1:
        if current_time<16 and current_time>9:
            n_img=1
        else:
            n_img=2
    if tray_menu==2:
        n_img=1
    if tray_menu==3:
        n_img=2
    dir_path = os.path.dirname(os.path.abspath(__file__))
    dir_path=dir_path.replace("\\","/")
    current_path=dir_path+"/SatImage/"+str(n_img)+".jpg"
    print(current_path)
    try:
        # 打开指定注册表路径
        reg_key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 10, win32con.KEY_SET_VALUE)
        # 最后的参数:2拉伸,0居中,6适应,10填充,0平铺
        win32api.RegSetValueEx(reg_key, "WallpaperStyle", 0, win32con.REG_SZ, "10")
        # 最后的参数:1表示平铺,拉伸居中等都是0
        win32api.RegSetValueEx(reg_key, "TileWallpaper", 0, win32con.REG_SZ, "0")
        # 刷新桌面与设置壁纸
        win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, current_path, win32con.SPIF_SENDWININICHANGE)
    except:
        print("错误")

def get_image(url):
    global i
    try:
        os.makedirs(data_path)
        print("创建文件夹")
    except:
        print("路径正常"),
    try:
        i=i+1
        image_path = names[i]
        urllib.request.urlretrieve(url, "./SatImage/" + str(i) + ".jpg")
        # print(names[i])
        print("数据获取完成"+"-----"+str(i))
        img = cv2.imread("./SatImage/" + str(i) + ".jpg")
        size = img.shape
        print(size)
        w=size[1]
        h=size[0]
        if(w/h<1.5):
            h=w/1.78
            h=int(h)
        print(h,w)
        cropped = img[0:h, 0:w]  # 裁剪坐标为[y0:y1, x0:x1]
        cv2.imwrite("./SatImage/"+ str(i) +".jpg", cropped)

    except:
        print("数据读取失败")

'''
def print_hi(name):
  
    print(f'Hi, {name}')  


def show_window():
    

def quit_program():
    exit(0)
'''
def action(tray_menu):
    for u in urls:
        get_image(u)
    set_wallpaper(tray_menu)

if __name__ == '__main__':
    action()
   
