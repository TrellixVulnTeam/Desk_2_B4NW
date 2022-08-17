#!/usr/bin/python

if {'a','b','c'} == {'b','a','c'}:
    print("True")
else:
    print('False')

word1="abbzzca"
word2="babzzcz"
from collections import Counter

cnter1,cnter2 = Counter(word1), Counter(word2)

print(type(cnter1.values()))
# print(cnter1.values())
print(sum(list(cnter2.values())))


def closeStrings( word1 , word2 )  :
    if set(word1) != set(word2): return False
    from collections import Counter
    cnter1, cnter2 = Counter(word1), Counter(word2)

    sum1, sum2 = sum(list(cnter1.values())), sum(list(cnter2.values()))
    print(f"sum1 = {sum1}")
    print(f"sum2 = {sum2}")
    if sum1 == sum2:
        return True
    return False

print(closeStrings(word1, word2))
