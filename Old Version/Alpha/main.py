import os
import psutil
import time

def is_process_running(process_name):
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == process_name:
            return True
    return False



def adbstart():
    os.system('adb.exe')
    adbusb()

def adbusb():
    os.system('adb.exe usb')

def adbrun(command):
    os.system(f'adb.exe {command}')

def adbgetready():
    print('Đang khởi động ADB - Android Debuging Bridge')
    adbstart()

def getin4():
    link = input('Vui lòng nhập link: \n')
    while True:
        times = input('Vui lòng nhập số lượng: ')
        if times.isdigit():
            times = int(times)
            break
        else:
            print('Vui lòng nhập số lượng hợp lệ.')

def adbexecute():
    adbrun('shell monkey -p com.moonactive.coinmaster -c android.intent.category.LAUNCHER 1')
    

def main():
    if is_process_running("adb.exe"):
        pass
    else:
        adbgetready()



if __name__ == "__main__":
    main()

