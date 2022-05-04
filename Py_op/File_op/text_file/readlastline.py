import os
file = "data_1.txt"
with open(file, 'rb') as f:
    print(f.read()) # b'this is a test\r\nthis is another test\r\n'
    f.seek(-1, os.SEEK_END)
    print(f.tell())
    print(f.read(1)) # b'\n'
    # while f.read(1) != b'\n':
    #     f.seek(-2, os.SEEK_CUR)
    #
    # last_line = f.readline().decode()
    # print(last_line)

with open(file,'rb') as f:
    print(f.readline()) # b'this is a test\r\n'

with open(file,'rb') as f:
    print(f.readline().decode()) #this is a test
