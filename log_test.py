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

import requests
import pytest

# @pytest.fixture(scope="class")
# def make_call():
#     print("fixture is called")
#     return 100
#
# @pytest.mark.usefixtures("make_call")
# class Test_MPS:
#     def test_1(self, make_call):
#         print(f" test_1 is {make_call}")
#     #
#     # def test_2(self, make_call):
#     #     print(f" test_2 is {make_call}")
#
#     def test_3(self):
#         print("LIKA")
#         print(f"{make_call}")
#
#     def test_3(self):
#         print("LIKA")
#         print(f"{make_call}")
#         assert 1 == 2
#
#     def test_30(self):
#         print("LIKA")
#         print(f"{make_call}")
#
#     def test_31(self):
#         print("LIKA")
#         print(f"{make_call}")
#         assert 2 == 9
#
#     def test_32(self):
#         print("LIKA")
#         print(f"{make_call}")
#
#
#
#
#
# import log_pytest
# log_pytest.test_1()
#
# if __name__ == "__main__":
#     pytest.main(["-s", "-v", "log_test.py"])


def gcd(x, y):  # Greatest Common Denominator
    return x if y == 0 else gcd(y, x % y)

print(gcd(4,18))








