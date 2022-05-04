import os
file = "data.txt"
"""

welcome to python 2
welcome to python 3
welcome to python 4
"""
with open(file, encoding="utf-8") as f:
    lines = f.readlines(30)
    # include the line that passes the # 30 mark
    print(lines)
    # ['\n', 'welcome to python 2\n', 'welcome to python 3\n']
    lines="".join(lines)
    print(len(lines))  # 41
    print(os.stat(file).st_size) # 65

# readline() return a string ended with "\n"
# readline(n) return a string of single line, upto n chars
# if n is bigger than len of current line, only output the whole line.
nums=[]
with open(file, encoding="utf-8") as f:
    line1 = f.readline() #
    nums.append(line1)
    line2 = f.readline()
    nums.append(line2)
    line3 = f.readline(10)
    nums.append(line3)

    print(type(line2))
    print(nums)
    # ['\n', 'welcome to python 2\n', 'welcome to']

nums.clear()
with open(file, encoding = "utf-8") as f:
    line = f.readline(40)
    nums.append(line)
    print(nums)