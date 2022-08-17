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

nums = [1, 3, 7, 5, 12, 33, 9, 88,0]
res = heapq.nsmallest(5, nums, key=lambda x: -x)
print(res) # [88, 33, 12, 9, 7]

arr = [1, 3, 7, 5, 12, 33, 9, 88,0]
res = heapq.nlargest(5, arr, key=lambda x: -x)
print(res) # [0, 1, 3, 5, 7]

def compare(x: str, y: str) -> int:
    return int(x) - int(y)

print(compare(10, 100))

#









