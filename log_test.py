from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.support.select import Select
from time import time

# driver = webdriver.Chrome(executable_path="C:\\Users\\jsun\\Documents\\Desk_2\\libs\\chromedriver.exe")
# driver.set_window_size(1920,1200)
# url="https://yahoo.com"
# driver.get(url)

# convert a list of str to a single string


# from collections import defaultdict, deque
#
# dic = defaultdict(lambda: {1})
# dic['a'].add(2)
#
# print(list(dic.items())) # [('a', {1, 2})]
#
# dic = defaultdict(lambda: set([1]))
# dic['a'].add(2)
#
# print(list(dic.items())) # [('a', {1, 2})]
#
# dic = defaultdict(lambda: deque([100]))
# dic["a"].append(200)
# print(dic["a"]) # deque([100, 200])


# nums = ["4","100", " 20"] # ['4', '100', ' 20']
# print(1,2,3, sep=": ")

def wordCount(startWords=["g","vf","ylpuk","nyf","gdj","j","fyqzg","sizec"], targetWords=["r","am","jg","umhjo","fov","lujy","b","uz","y"] ) :
    # 8:33 5/12/22
    from collections import Counter, defaultdict
    dic = defaultdict(list)
    for v in startWords:
        dic[len(v)].append(Counter(v))
    res = 0

    for v in targetWords:
        print(v)
        cnt_v = Counter(v)
        len_v = len(v)
        if len_v - 1 in dic:
            for src in dic[len_v - 1]:
                flag = False
                cnt = 0
                for k, c in src.items():
                    if k not in cnt_v or c != cnt_v[k]:
                        flag = True
                        break
                if not flag and len(src) < 26:
                    res += 1
                    break
    return res
print(wordCount())