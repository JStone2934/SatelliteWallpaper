import serial
import serial.tools.list_ports
 
# 获取所有串口设备实例。
# 如果没找到串口设备，则输出：“无串口设备。”
# 如果找到串口设备，则依次输出每个设备对应的串口号和描述信息。
gpu_rate=89
ser = serial.Serial("COM12", 115200)
'''
ports_list = list(serial.tools.list_ports.comports())
if len(ports_list) <= 0:
    print("无串口设备。")
else:
    print("可用的串口设备如下：")
    for comport in ports_list:
        print(list(comport)[0], list(comport)[1])
'''
def open_COM():
        # 打开COM17，将波特率配置为115200，其余参数使用默认值
    if ser.isOpen():                        # 判断串口是否成功打开
        print("打开串口成功。")
        print(ser.name)    # 输出串口号
    else:
        print("打开串口失败。")


def write_data(gpu_rate):
    if(ser.isOpen()):
        gp=str(gpu_rate)
        ser.write(gp.encode('ascii'))
        print("发送成功")
    else:
        print("发送失败！")