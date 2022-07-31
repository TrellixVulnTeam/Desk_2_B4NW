import os
from shutil import copy2
# os.path.dirname(file_name or folder_name) --> upper folder
# os.path.abspath(file_name or folder_name) -->
# os.path.join(*list_of_strings) --> concatenate as path

# /
# print(__file__)
# C:/Users/jsun/Documents/Desk_2/Py_op/File_op/Basic_op/test_4/folder_op.py

file_folder_name = os.path.dirname(__file__)
# print(file_folder_name)
# C:/Users/jsun/Documents/Desk_2/Py_op/File_op/Basic_op/test_4
# print(os.path.dirname("C:"))
# C:

# \
path = os.path.abspath(__file__)
# print(path)
# C:\Users\jsun\Documents\Desk_2\Py_op\File_op\Basic_op\test_4\folder_op.py

folder_path = os.path.abspath(file_folder_name)
# print(folder_path)
# C:\Users\jsun\Documents\Desk_2\Py_op\File_op\Basic_op\test_4\folder_op.py

file_dir, file_name = __file__.rsplit("/", maxsplit=1)
# print(f"file_dir={file_dir}\n filename={file_name}")
# file_dir=C:/Users/jsun/Documents/Desk_2/Py_op/File_op/Basic_op/test_4
#  filename=folder_op.py

path_to_join = [file_folder_name, "folder_op.py"]
dir_final = os.path.join(*path_to_join)
print(dir_final)
copy2(dir_final, "test_4.1")


