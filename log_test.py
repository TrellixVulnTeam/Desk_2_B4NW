
import re

pattern1 = "[1-9]?\d$"

s = "012"
ret = re.search(pattern1, s)

print(ret.group())
# 12









