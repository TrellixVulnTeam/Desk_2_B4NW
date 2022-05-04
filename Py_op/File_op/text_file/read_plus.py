with open("data_1.txt", "r+") as f:

    # r+ : read and write, it can be read first or write first
    # everytime read or write, curson moves to the end
    line = f.read() # curson moved to the first loc after the end of last read
    print(line)
    print(f.tell())
    f.write("This is the fourth row")# start filling starting at the current cur
    print(f.tell()) # curson moved to loc after the last written loc
    txt = f.read() # read from beginning
    print(txt)

    #This is the 3rd rowd line!