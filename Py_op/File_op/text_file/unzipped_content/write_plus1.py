with open("data_3.txt", "w+") as f:
    # curson always moves to the end either for read or write
    print(f.tell(), "  before the read")
    print(f"first read  : {f.read()}") # ignore, no read output

   # 0   before the read
#first read  :
    # Need to write first
    f.write("NONONONO OO  row")
    print(f"cursor after write is @ {f.tell()}")
    print(f"2nd read is {f.read()}") # cursor is at the end, so nothing to print




