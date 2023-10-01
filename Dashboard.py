import pynvml
import psutil
import bt_com
import time
pynvml.nvmlInit()
handle = pynvml.nvmlDeviceGetHandleByIndex(0)
memory_rate = 0

def set_data():
    gpuTemperature = pynvml.nvmlDeviceGetTemperature(handle, 0)
    print(gpuTemperature)
    bt_com.open_COM()
    memory_rate=int(psutil.virtual_memory().percent)
    bt_com.write_data(str(gpuTemperature)+str(memory_rate))
    time.sleep(1)
    print(int(psutil.virtual_memory().percent))

def stop_dashboard():
    bt_com.write_data("0000")