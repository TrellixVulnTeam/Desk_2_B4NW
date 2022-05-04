import os, shutil
print(os.getcwd())

# os.makedirs("tmp/log4")
# os.makedirs("tmp\\log5")
#

# shutil.rmtree("tmp/log5")
os.chdir("tmp/log")
print(os.getcwd())

print(os.getcwd())
path_list = os.path.split(os.getcwd())

print(type(path_list))  # <class 'tuple'>
print(path_list) # ('C:\\Users\\jsun\\Documents\\Desk_2\\Py_op\\File_op\\text_file\\tmp', 'log')

print(path_list[0].split("/")) # ['C:\\Users\\jsun\\Documents\\Desk_2\\Py_op\\File_op\\text_file\\tmp']
print(path_list[0].split("\\")) # ['C:', 'Users', 'jsun', 'Documents', 'Desk_2', 'Py_op', 'File_op', 'text_file', 'tmp']

os_stat = os.stat("../../path_op.py")
print(type(os_stat))
print(os_stat.st_size) # 1178
# <class 'os.stat_result'>
# os.stat_result(st_mode=33206, st_ino=1175439502743703954, st_dev=38182903, st_nlink=1, st_uid=0, st_gid=0, st_size=678, st_atime=1651085410, st_mtime=1651085410, st_ctime=1651083616)


print(os.path.abspath("path_op.py"))
# C:\Users\jsun\Documents\Desk_2\Py_op\File_op\text_file\tmp\log\path_op.py

print(os.getcwd()) # C:\Users\jsun\Documents\Desk_2\Py_op\File_op\text_file\tmp\log
print(os.listdir("../")) # ['log', 'log1', 'log2', 'log3', 'log4']
print("file size is ", os.path.getsize(__file__))
print("file size is ", os.stat(__file__).st_size)
print(f"file name is {__file__}") #file name is C:/Users/jsun/Documents/Desk_2/Py_op/File_op/text_file/path_op.py


if __name__  == "__main__":
    import os
    # print("file size is ", os.path.getsize(__file__))
    # print("file size is ", os.stat(__file__).st_size)
    print(f"abspath is {os.path.abspath(__file__)}")
    # abspath is C:\Users\jsun\Documents\Desk_2\Py_op\File_op\text_file\path_op.py
    # print(getFilesize(__file__))
    print(f"__name__ is {__name__}")

    print("--------------------------------")
    print(os.chdir('../..'))
    print(os.getcwd())
    # print(os.listdir(".")) # list both files and dirs under the path

    import os.path
    import zipfile

    with zipfile.ZipFile('log_all.zip', "w") as zf:
        file_list = os.listdir(".") #
        print(file_list)
        for item in file_list:
            zf.write(item) # can write both files and folders containing files

    with zipfile.ZipFile('log_all.zip', 'r') as zf:
        unzip_folder = 'unzipped_content'
        zf.extractall(unzip_folder)
        zipped_files = os.listdir(unzip_folder)
        print(zipped_files)
