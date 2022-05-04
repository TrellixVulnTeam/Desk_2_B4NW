data = ["\n\n","welcome to python 1\n", "welcome to python 2\n", "welcome to python 3\n", "welcome to python 4\n"]
with open("data.txt","w") as fout:
    fout.writelines(data)

with open("data.txt") as fin:
    print(fin.read())

"""

welcome to python 1
welcome to python 2
welcome to python 3
welcome to python 4
"""

with open('data.txt','r+') as f:
    f.write("new line")
    print(f.read())

with open('data.txt') as fin:
    print(fin.read())