import psutil

# print(psutil.cpu_times())
# print(psutil.cpu_stats())



# for _ in range(3):
#     cap_possessed_by_person = input().strip().split()
#     print((cap_possessed_by_person))
#     cap_possessed_by_person = map(int, input().strip().split())
#     print(list(cap_possessed_by_person))

# 3
# ['3']
# 3
# [3]
# 2 10 100
# ['2', '10', '100']
# 2 10 100
# [2, 10, 100]
# 5 23
# ['5', '23']
# 5 23
# [5, 23]

#!usr/bin/python
import copy

import heapq

# No matter what, heapq only creats a min-priority queue
nums = ['aBc', 'adc', 'bd', 'Ae']

from collections import deque

# transpose a matrix to column matrix
from pprint import pprint


flattened = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,17,18,19,20]
r, c, n = 5, 4, len(flattened)

matrix = [ [flattened[i*c + j] for j in range(c)] for i in range(r)]
"""
[[1, 2, 3, 4],
 [5, 6, 7, 8],
 [9, 10, 11, 12],
 [13, 14, 15, 16],
 [17, 18, 19, 20]
 ]
"""
# pprint(matrix)
# matrix --> row list
row_list = [ row[j] for row in matrix for j in range(len(matrix[0]))]
# print(row_list)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

from selenium import webdriver
from time import sleep

# url = "https://www.yahoo.com"
# driver = webdriver.Chrome()
# driver.get(url)
# print(driver.title)
# # Yahoo | Mail, Weather, Search, Politics, News, Finance, Sports & Videos
# print(driver.current_url)
# # https://www.yahoo.com/
# sleep(1)
# driver.switch_to.
#print(driver.page_source) # Return html page
# driver.close()


def splitIntoFibonacci(num: str) -> list:
    # 12:45, 9/21/22

    def dfs(num, i, res, dic):
        if i == len(num):
            if len(res) > 2 : return True
            return False

        if i in dic:
            return dic[i]

        dic[i] = False

        if len(res) < 2:
            for j in range(i, len(num)):
                if j > i and num[i] == "0":
                    break
                v = int(num[i:j + 1])
                if v > (1 << 31) - 1: break  # return False
                res.append(v)
                if dfs(num, j + 1, res, dic):
                    dic[i] = True
                    break
                else:
                    res.pop()
        else:
            target = res[-1] + res[-2]
            if target <= (1 << 31) - 1:
                len_target = len(str(target))
                if target == int(num[i:i + len_target]):
                    res.append(target)
                    if dfs(num, i + len_target, res, dic):
                        dic[i] = True
                    else:
                        res.pop()

        return dic[i]

    res = []
    dfs(num, 0, res, {})
    return res
num="1101111"
print(splitIntoFibonacci(num))


# 1 10 11 11






































