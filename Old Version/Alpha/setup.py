import wget
import requests
import sys
import time
import random
import os
import zipfile
import subprocess
import webbrowser

repo_owner = 'chezzakowo'
repo_name = 'ChezCoinMasterToolDatabase'
typing_speed = 305  # wpm
current_directory = os.getcwd()
extract_to_path = os.path.join(current_directory, 'extracted_folder')
yt = 'https://youtu.be/XhpCtGfWywo?t=71'


def download_release_files(repo_owner, repo_name, filenames):
    url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest'
    response = requests.get(url)

    if response.status_code == 200:
        release_info = response.json()
        assets = release_info['assets']

        for asset in assets:
            asset_name = asset['name']
            if asset_name in filenames:
                asset_url = asset['browser_download_url']
                asset_download_path = os.path.join(current_directory, asset_name)

                print(f"Downloading {asset_name}...")
                asset_response = requests.get(asset_url)

                if asset_response.status_code == 200:
                    with open(asset_download_path, 'wb') as f:
                        f.write(asset_response.content)
                    print(f"{asset_name} Đã được tải hoàn tất.")
                else:
                    print(f"Lỗi khi tải {asset_name}. Mã lỗi: {asset_response.status_code} \n Nếu file còn bị lỗi, vui lòng IB Discord: chezzakowo")
    else:
        print(f"Mã lỗi khi tìm file cần thiết: {response.status_code} \n Nếu file còn bị lỗi, vui lòng IB Discord: chezzakowo ")


def run(repo_owner, repo_name, file_main):
    url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest'
    response = requests.get(url)

    if response.status_code == 200:
        release_info = response.json()
        assets = release_info['assets']

        for asset in assets:
            asset_name = asset['name']
            if asset_name in file_main:
                asset_url = asset['browser_download_url']
                asset_download_path = os.path.join(current_directory, asset_name)

                print(f"Downloading {asset_name}...")
                asset_response = requests.get(asset_url)

                if asset_response.status_code == 200:
                    with open(asset_download_path, 'wb') as f:
                        f.write(asset_response.content)
                    print(f"{asset_name} Đã được tải hoàn tất.")
                else:
                    print(f"Lỗi khi tải {asset_name}. Mã lỗi: {asset_response.status_code}")
    else:
        print(f"Lỗi khi tìm {asset_name}. Mã lỗi: {asset_response.status_code} \n Nếu còn lỗi, vui lòng IB Discord: chezzakowo")


def download_scrcpy(filenames):
    url = f'https://api.github.com/repos/Genymobile/scrcpy/releases/latest'
    response = requests.get(url)

    if response.status_code == 200:
        release_info = response.json()
        assets = release_info['assets']

        for asset in assets:
            asset_name = asset['name']
            if asset_name in filenames:
                asset_url = asset['browser_download_url']
                asset_download_path = os.path.join(current_directory, asset_name)

                print(f"Downloading {asset_name}...")
                asset_response = requests.get(asset_url)

                if asset_response.status_code == 200:
                    with open(asset_download_path, 'wb') as f:
                        f.write(asset_response.content)
                    print(f"{asset_name} Đã được tải hoàn tất.")
                else:
                    print(f"Lỗi khi tải {asset_name}. Mã lỗi: {asset_response.status_code} \n Nếu file còn bị lỗi, vui lòng IB Discord: chezzakowo")
    else:
        print(f"Mã lỗi khi tìm file cần thiết: {response.status_code} \n Nếu file còn bị lỗi, vui lòng IB Discord: chezzakowo")


def unzip_file(zip_file_path, extract_to_path):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to_path)


def dynamic_color_for_ascii_art(ascii_art):
    for line in ascii_art.split('\n'):
        for char in line:
            color_code = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            sys.stdout.write(f"\033[38;2;{color_code[0]};{color_code[1]};{color_code[2]}m{char}\033[0m")
            sys.stdout.flush()
            time.sleep(random.random() * 10.0 / typing_speed)
        print()


def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random() * 10.0 / typing_speed)
    print('\n')


ascii_art = r'''
   ____ _               ____ __  __ _____           _ 
  / ___| |__   ___ ____/ ___|  \/  |_   _|__   ___ | |
 | |   | '_ \ / _ \_  / |   | |\/| | | |/ _ \ / _ \| |
 | |___| | | |  __// /| |___| |  | | | | (_) | (_) | |
  \____|_| |_|\___/___|\____|_|  |_| |_|\___/ \___/|_| 
'''

print('\n \n \n')

dynamic_color_for_ascii_art(ascii_art)

slow_type('Chào mừng bạn đã đến với bộ cài ChezCMTool - 1 công cụ chạy spin coin master của Chez \n Support: https://discord.com/users/903942978278662194')
slow_type('Nhấn enter để tiếp tục')
input('')
print('Bây giờ tôi sẽ bắt đầu cài tool nhá')
slow_type('......')
print('Bắt đầu kiểm tra ADB đã cài chưa!')


def run_adb_command(command):
    adb_executable = "adb.exe"

    try:
        subprocess.run([adb_executable, "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except FileNotFoundError:
        print("Không tìm thấy adb, tiến hành tải và giải nén...")

        # Download ADB
        download_release_files(repo_owner, repo_name, ['adb.zip'])

        # Extract ADB
        unzip_file('adb.zip', current_directory)

        # Check if ADB executable exists
        if not os.path.isfile(adb_executable):
            print("Lỗi: Không thể tìm thấy tệp thực thi ADB sau khi cài đặt.")
        else:
            print("ADB đã được cài đặt thành công.")
    except subprocess.CalledProcessError:
        print("Lỗi: Không thể chạy ADB sau khi cài đặt.")
    else:
        print('ADB đã được cài đặt!')

# Example usage:
adb_command = ["adb"]
run_adb_command(adb_command)

scrcpy_input = input('Bạn muốn cài scrcpy không? (dùng để xem màn hình khi tool chạy) [y/n]: ')

if scrcpy_input.lower() == 'y':
    scrcpy_installed = False

    try:
        subprocess.run(["scrcpy", "--version"], check=True)
        scrcpy_installed = True
    except FileNotFoundError:
        pass
    except subprocess.CalledProcessError:
        pass

    if not scrcpy_installed:
        print("Không tìm thấy Scrcpy. Đang tải xuống và cài đặt...")

        # Kiểm tra kiến trúc hệ thống (32-bit hoặc 64-bit)
        is_64_bit = sys.maxsize > 2**32

        scrcpy_filename = f"scrcpy-win{'64' if is_64_bit else '32'}-v2.3.1.zip"
        download_scrcpy([scrcpy_filename])
        zip_file = scrcpy_filename
        slow_type('Đang giải nén scrcpy')
        unzip_file(scrcpy_filename, current_directory)
    else:
        print("Scrcpy đã được cài đặt.")


elif scrcpy_input.lower() == 'n':
    print("Bỏ qua quá trình cài đặt Scrcpy.")
else:
    print("Đầu vào không hợp lệ. Vui lòng nhập 'y' hoặc 'n'.")

typeoffile = input('Bạn muốn cài loại file nào? exe hay py? \n Loại file py: Có mã nguồn có thể tùy biến \n Loại exe: Có thể custom bằng mã JSON [py/exe]')

if typeoffile.lower() == 'py':
    file_name = 'py_runtime'  # Define a default value for py files
    run(repo_owner, repo_name, file_name)
elif typeoffile.lower() == 'exe':
    file_name = 'exe_runtime.zip'  # Define a default value for exe files
    run(repo_owner, repo_name, file_name)
else:
    print("Đầu vào không hợp lệ. Vui lòng nhập 'py' hoặc 'exe'.")


slow_type('Đã tải hoàn tất, bây giờ tôi sẽ kiểm tra tài nguyên')

# ...

full_path = os.path.join(current_directory, file_name)

slow_type('Đã tải hoàn tất, bây giờ tôi sẽ kiểm tra tài nguyên')

if os.path.exists(full_path):
    print(f"File {file_name} đã được xác minh thành công!")
else:
    print(f"Lỗi: {file_name} đã không được tìm thấy, tiến thành tải lại!")
    run(repo_owner, repo_name, file_name)

# Update the file_name to full_path in the unzip_file function call
zip_file_path = full_path

slow_type('Bắt đầu giải nén file........')
unzip_file(zip_file_path, extract_to_path)
print('Đã giải nén hoàn tất')

# ...


zip_file_path = file_name

slow_type('Bắt đầu giải nén file........')
unzip_file(zip_file_path, extract_to_path)
print('Đã giải nén hoàn tất')

slow_type('Đã tải và cài đặt hoàn tất!')
yt_ask = input('Bạn có muốn xem video cách để sử dụng không? [y/n hoặc bấm enter (skip)]')

if yt_ask.lower() == 'y':
    webbrowser.open(yt, new=0, autoraise=True)
if yt_ask.lower() == 'n':
    pass
else:
    pass

time.sleep(5)
os.remove('adb.zip')
os.remove(file_name)
os.remove(scrcpy_filename)


def run_the_runtime(file_name):
    if file_name.lower() == 'exe':
        exe_file_path = os.path.join(extract_to_path, 'demo.exe')
        if os.path.exists(exe_file_path):
            subprocess.run([exe_file_path])
        else:
            print("Lỗi: File demo.exe không tồn tại.")
    elif file_name.lower() == 'py':
        bat_file_path = os.path.join(extract_to_path, 'setup.bat')
        if os.path.exists(bat_file_path):
            subprocess.run([bat_file_path])
            py_file_path = os.path.join(extract_to_path, 'main.py')
            if os.path.exists(py_file_path):
                subprocess.run(['python', py_file_path])
            else:
                print("Lỗi: File main.py không tồn tại.")
        else:
            print("Lỗi: File setup.bat không tồn tại.")
    else:
        print("Lỗi: Loại file không hợp lệ.")


run_or_not = input('Bạn có muốn chạy file ngay bây giờ không? [y/n hoặc bấm enter (skip)]')

if run_or_not.lower() == 'y':
    run_the_runtime(typeoffile)
if run_or_not.lower() == 'n':
    pass
else:
    pass
slow_type('Cảm ơn bạn đã sử dụng ChezCMTool! Bây giờ tôi sẽ xóa các file thừa sau khi tải')
input('Bấm enter để thoát')

