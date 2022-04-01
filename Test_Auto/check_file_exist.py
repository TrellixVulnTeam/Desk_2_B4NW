import os
import time
file_path = r"C:\Users\jsun\Documents\Desk_2\Test_Slen\Py_Selenium\PythonSelFramework\utilities\check_file_exist.py"
def get_file_size(file_path_server):
    if os.path.isfile(file_path_server):
        st = os.stat(file_path_server)
        return st.st_size, st.st_atime, st.st_dev
    else:
        return -1
# st_mode − protection bits.
# st_ino − inode number.
# st_dev − device.
# st_nlink − number of hard links.
# st_uid − user id of owner.
# st_gid − group id of owner.
# st_size − size of file, in bytes.
# st_atime − time of most recent access.
# st_mtime − time of most recent content modification.
# st_ctime − time of most recent metadata change.

print(get_file_size(file_path))
def is_file_exist(file_path_server,file_path, time_to_wait):
    time_cnter = 0
    while not os.path.exists(file_path): # should just use os.path.isfile()
        time.sleep(1)
        time_cnter+=1
        if time_cnter > time_to_wait:
            print(f"{file_path} does not exist")
            return False
    if os.path.isfile(file_path):
        file_size = get_file_size(file_path_server)
        cnt = 0
        while True:
            download_size = get_file_size(file_path)
            if download_size != file_size:
                time.sleep(1)
                cnt += 1
            else:
                break
            if cnt > 10:
                break
        return download_size == file_size
    else:
        raise ValueError(f"{file_path} doesn't exist")

def download_wait(path_to_downloads):
    seconds = 0
    dl_wait = True
    while dl_wait and seconds < 20:
        time.sleep(1)
        dl_wait = False
        for fname in os.listdir(path_to_downloads):
            if fname.endswith('.crdownload'):
                dl_wait = True
        seconds += 1
    return seconds
