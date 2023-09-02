import urllib.request
import os

url = "exp"
file_path = "./SatImage"
FY4B_SW = "http://img.nsmc.org.cn/CLOUDIMAGE/FY4B/AGRI/SWCI/FY4B_DISK_SWCI.JPG"
FY4A_TURE = "http://img.nsmc.org.cn/CLOUDIMAGE/FY4A/MTCC/FY4A_DISK.JPG"
FY4A_CN = "http://img.nsmc.org.cn/CLOUDIMAGE/FY4A/MTCC/FY4A_CHINA.JPG"
FY4B_CN = "http://img.nsmc.org.cn/CLOUDIMAGE/FY4B/AGRI/GCLR/FY4B_REGC_GCLR.JPG"
urls = [FY4B_SW, FY4A_TURE, FY4B_CN, FY4A_CN]
names = ["FY4B_SW", "FY4A_TURE", "FY4B_CN", "FY4A_CN"]


def get_image(url):
    try:
        os.makedirs(file_path)
        print("创建文件夹")

    except:
        print("路径正常"),
    try:
        i = 0
        if i == 4:
            i = 0
        else:
            pass
        image_path = names[i]
        urllib.request.urlretrieve(url, "./SatImage/" + image_path + ".jpg")
        print(url)
        print("数据获取完成")

    except:
        print("数据读取失败")


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    for u in urls:
        get_image(u)
