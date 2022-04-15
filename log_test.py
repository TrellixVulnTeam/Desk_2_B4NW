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

my_set = {1,2,3}
my_set.add({5,6})
print(my_set)
