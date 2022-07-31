from shutil import copy2, copy, copytree, copyfile
from shutil import rmtree
import os, glob
import fnmatch
import shutil

#   os.path.exists will also return True if there's a regular file with that name.
#   os.path.isdir will only return True if that path exists and is a directory.


# copy2 need des. folder exists
# copy2 src_file can't be dir.
# if file exists, copy2 will overwirte the file with same name.
# copy,copytree doesn't preserve meta data of copied files, copy2 does
# copy() copies the file data and the file's permission mode (see os.chmod()).
# Other metadata, like the file's creation and modification times, is not preserved.

## 1. copy2 a file to a differnt folder
file_src = "subprocess_log.py"
dir_des = r"C:\Users\jsun\Documents\Desk_2\Py_op\File_op\Basic_op\test_1"

# copy2 "subprocess_log.py" to folder test_1, the copy has the same name
# shutil.copy2(file_src, dir_des)

new_file = "subprocess_log.txt"
# copy2 a file to be same file but different name
# shutil.copy2(file_src, os.path.join(dir_des,new_file))
# os.remove(os.path.join(dir_des, file_src))


# 2. copy a folder
# 2.1 Copy only content of a folder to new non-existing folder
# copytree does not work if destine folder exists
base_dir  = os.getcwd()
sub_dir = "test_2"
folder_src = os.path.join(base_dir, sub_dir)
folder_des = os.path.join(base_dir, "test_5")

if os.path.isdir(folder_des):
    print("dst_dir exists, and need to be rmoved")
    # rmtree(folder_des)
else: # dst_dir can't exist
    # copytree(folder_src, folder_des)
    # Create folder_des folder, copy content under folder_src to it
    print("dst_dir has been created!")

# 2.2 copy whole folder to an existing folder
base_dir  = os.getcwd()
sub_dir = "test_2"
folder_src = os.path.join(base_dir, sub_dir)
folder_des = os.path.join(base_dir, "test_4")
# only work for python 3.8+
# copytree(folder_src, folder_des, dirs_exist_ok=True)

# 3. rename
f_name = "test_5"
new_name = "test_5_cpy"
# os.rename(f_name, new_name) # rename a folder

file_name = "subprocess_log.py"
file_new_name = "subprocess_log_cpy.py"
# os.rename(file_name , file_new_name)

# 4. folder access
## basic dir/files ops
# import time, datetime
# test_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
cur_dir = os.getcwd()
folder_to_move = ['test_2', 'test_3','copy_folder']
folder_to_move = os.path.join(cur_dir, *folder_to_move)
# print(folder_to_move)

# os.chdir(folder); can be file_name, needs to be folder_name
# os.chdir(folder_to_move)
# C:\Users\jsun\Documents\Desk_2\Py_op\File_op\Basic_op\test_2\test_3\copy_folder
# os.chdir("..")
# print(os.getcwd())
# C:\Users\jsun\Documents\Desk_2\Py_op\File_op\Basic_op\test_2\test_3\copy_folder

# 5. Create folder
base_dir = os.getcwd()
# create nested dirs with os.makedirs()
nested_dir = "test_9/test_10"
# os.makedirs(nested_dir)

# create single folder with os.mkdir()
# os.chdir("test_9")
# print(os.getcwd())
# C:\Users\jsun\Documents\Desk_2\Py_op\File_op\Basic_op\test_9
# os.mkdir('test_time')
# print(os.listdir()) # print current dir
# ['test_10', 'test_time']

# print(os.listdir(".")) # also current dir
# ['test_10', 'test_time']


# 5. remove files or folder
#os.remove() removes a file.
#os.rmdir() removes an empty directory.
#shutil.rmtree() deletes a directory and all its contents or an empty folder

# copytree('test_5_cpy', 'test_5_delete')
os.chdir('test_5_delete')
file_to_rm = os.path.join(os.getcwd(), *['test_3', 'copy_folder', "QA_Auto.txt"])
print(file_to_rm)
# C:\Users\jsun\Documents\Desk_2\Py_op\File_op\Basic_op\test_5_delete\test_3\copy_folder\QA_Auto.txt

# Remove a single file
# os.remove(file_to_rm)

# Remove an empty folder or nested folder_src
# shutil.rmtree("folder_name")
# print(os.getcwd())
# C:\Users\jsun\Documents\Desk_2\Py_op\File_op\Basic_op\test_5_delete
os.chdir("..")
# C:\Users\jsun\Documents\Desk_2\Py_op\File_op\Basic_op
# print(os.getcwd())

# rmtree('test_5_delete')
