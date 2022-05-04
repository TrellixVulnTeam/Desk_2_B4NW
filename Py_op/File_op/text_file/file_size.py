with open("path_op.py") as f:
    f.seek(0,2)
    print(f.tell())