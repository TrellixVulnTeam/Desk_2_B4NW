with open("data_2.txt", "w+") as f:
    # curson always moves to the end either for read or write
    f.write("this is the first row")
    print(f"cursor after write is @ {f.tell()}")
    print(f"first read is {f.read()}") # cursor is at the end, so nothing to print
    f.write("writing 2nd time")
    print(f"after 2nd write {f.tell()}")
    print(f.read())
    print(f"expected to see nothing")


