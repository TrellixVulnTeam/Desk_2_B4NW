with open("data_1.txt", "w+") as f:
    # curson always moves to the end either for read or write

    # w+, does NOT allow read first
    print(f"first read  : {f.read()}") # ignore, no read output






